"""
Transkribus XML to CSV Workflow
A unified pipeline for extracting, normalizing, and merging Transkribus PageXML data

Workflow Steps:
1. Extract paragraphs from PageXML files -> CSV files
2. Normalize Tibetan text in CSV files
3. Merge all normalized CSV files into a single master CSV

Author: Modified for Divergent Discourses project
"""
import os
import sys
from configparser import ConfigParser
from datetime import datetime
import argparse

from extractor import XMLParagraphExtractor
from normalizer import load_tables, normalize_csv_files
from merger import merge_csv_files


class WorkflowManager:
    """
    Manages the complete workflow pipeline.
    """
    
    def __init__(self, config_path: str = 'workflow_config.ini'):
        """
        Initialize the workflow manager with configuration.
        
        Args:
            config_path: Path to the configuration file
        """
        self.config = ConfigParser()
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        self.config.read(config_path)
        self.verbose = self.config.getboolean('logging', 'verbose', fallback=True)
        
        # Initialize logging
        self.log_file = self.config.get('logging', 'log_file', fallback=None)
        if self.log_file:
            os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
    
    def log(self, message: str):
        """
        Log a message to console and optionally to file.
        
        Args:
            message: Message to log
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"[{timestamp}] {message}"
        
        if self.verbose:
            print(log_msg)
        
        if self.log_file:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_msg + '\n')
    
    def run_extraction(self) -> bool:
        """
        Step 1: Extract paragraphs from PageXML files.
        
        Returns:
            True if successful, False otherwise
        """
        if not self.config.getboolean('workflow', 'enable_extraction', fallback=True):
            self.log("⊘ Extraction step is disabled in config")
            return True
        
        self.log("\n" + "="*60)
        self.log("STEP 1: EXTRACTING PARAGRAPHS FROM PAGEXML")
        self.log("="*60)
        
        xml_dir = self.config.get('paths', 'xml_input_dir')
        output_dir = self.config.get('paths', 'extracted_csv_dir')
        namespace_uri = self.config.get('extraction', 'namespace_uri')
        excluded_files = [
            f.strip() 
            for f in self.config.get('extraction', 'excluded_files').split(',')
        ]
        
        if not os.path.exists(xml_dir):
            self.log(f"✗ Error: XML input directory does not exist: {xml_dir}")
            return False
        
        extractor = XMLParagraphExtractor(namespace_uri, excluded_files)
        csv_files = extractor.extract_all(xml_dir, output_dir, self.verbose)
        
        if csv_files:
            self.log(f"\n✓ Extraction complete: {len(csv_files)} CSV files created")
            self.log(f"  Output directory: {output_dir}")
            return True
        else:
            self.log("✗ Extraction failed or no files processed")
            return False
    
    def run_normalization(self) -> bool:
        """
        Step 2: Normalize text in extracted CSV files.
        
        Returns:
            True if successful, False otherwise
        """
        if not self.config.getboolean('workflow', 'enable_normalization', fallback=True):
            self.log("⊘ Normalization step is disabled in config")
            return True
        
        self.log("\n" + "="*60)
        self.log("STEP 2: NORMALIZING TEXT")
        self.log("="*60)
        
        input_dir = self.config.get('paths', 'extracted_csv_dir')
        output_dir = self.config.get('paths', 'normalized_csv_dir')
        table_path = self.config.get('paths', 'table_path')
        flag = self.config.getint('normalization', 'flag')
        
        if not os.path.exists(input_dir):
            self.log(f"✗ Error: Input directory does not exist: {input_dir}")
            return False
        
        if not os.path.exists(table_path):
            self.log(f"✗ Error: Table directory does not exist: {table_path}")
            return False
        
        # Load normalization tables
        tables = load_tables(table_path, flag, self.verbose)
        
        if not tables:
            self.log("✗ No normalization tables loaded")
            return False
        
        # Normalize CSV files
        normalized_files = normalize_csv_files(input_dir, output_dir, tables, self.verbose)
        
        if normalized_files:
            self.log(f"\n✓ Normalization complete: {len(normalized_files)} files normalized")
            self.log(f"  Output directory: {output_dir}")
            return True
        else:
            self.log("✗ Normalization failed or no files processed")
            return False
    
    def run_merge(self) -> bool:
        """
        Step 3: Merge normalized CSV files into a single file.
        
        Returns:
            True if successful, False otherwise
        """
        if not self.config.getboolean('workflow', 'enable_merge', fallback=True):
            self.log("⊘ Merge step is disabled in config")
            return True
        
        self.log("\n" + "="*60)
        self.log("STEP 3: MERGING CSV FILES")
        self.log("="*60)
        
        input_dir = self.config.get('paths', 'normalized_csv_dir')
        output_dir = self.config.get('paths', 'merged_csv_dir')
        merged_filename = self.config.get('merge', 'merged_filename')
        output_file = os.path.join(output_dir, merged_filename)
        
        if not os.path.exists(input_dir):
            self.log(f"✗ Error: Input directory does not exist: {input_dir}")
            return False
        
        result = merge_csv_files(input_dir, output_file, self.verbose)
        
        if result:
            self.log(f"\n✓ Merge complete")
            self.log(f"  Output file: {result}")
            return True
        else:
            self.log("✗ Merge failed")
            return False
    
    def run_workflow(self):
        """
        Execute the complete workflow pipeline.
        """
        self.log("\n" + "#"*60)
        self.log("# TRANSKRIBUS XML TO CSV WORKFLOW")
        self.log("# Divergent Discourses Project")
        self.log("#"*60)
        self.log(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Track success of each step
        steps_status = {}
        
        # Step 1: Extraction
        steps_status['extraction'] = self.run_extraction()
        
        # Step 2: Normalization
        if steps_status['extraction']:
            steps_status['normalization'] = self.run_normalization()
        else:
            self.log("\n⊘ Skipping normalization due to extraction failure")
            steps_status['normalization'] = False
        
        # Step 3: Merge
        if steps_status['normalization']:
            steps_status['merge'] = self.run_merge()
        else:
            self.log("\n⊘ Skipping merge due to normalization failure")
            steps_status['merge'] = False
        
        # Final summary
        self.log("\n" + "="*60)
        self.log("WORKFLOW SUMMARY")
        self.log("="*60)
        
        for step, status in steps_status.items():
            status_icon = "✓" if status else "✗"
            self.log(f"{status_icon} {step.capitalize()}: {'Success' if status else 'Failed'}")
        
        all_success = all(steps_status.values())
        self.log("\n" + ("✓ WORKFLOW COMPLETED SUCCESSFULLY" if all_success else "✗ WORKFLOW COMPLETED WITH ERRORS"))
        self.log(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        return all_success


def main():
    """
    Main entry point for the workflow.
    """
    parser = argparse.ArgumentParser(
        description="Transkribus XML to CSV Workflow - Extract, Normalize, and Merge",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run complete workflow with default config
  python workflow.py

  # Run with custom config file
  python workflow.py --config my_config.ini

  # Run specific steps only (modify config file to enable/disable steps)
        """
    )
    
    parser.add_argument(
        '--config',
        default='workflow_config.ini',
        help='Path to configuration file (default: workflow_config.ini)'
    )
    
    args = parser.parse_args()
    
    try:
        manager = WorkflowManager(args.config)
        success = manager.run_workflow()
        sys.exit(0 if success else 1)
    
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
