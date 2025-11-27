"""
XML Paragraph Extractor Module
Extracts text regions from Transkribus PageXML files
"""
import os
from xml.etree import ElementTree as ET
import pandas as pd
import re
from typing import Dict, List


class XMLParagraphExtractor:
    """
    Extracts paragraphs and metadata from Transkribus PageXML files.
    """

    def __init__(self, namespace_uri: str, excluded_files: List[str]):
        """
        Initialize the XMLParagraphExtractor.
        
        Args:
            namespace_uri: XML namespace URI for PageXML
            excluded_files: List of filenames to exclude from processing
        """
        self.namespaces = {'ns': namespace_uri}
        self.excluded_files = excluded_files

    def parse_filename(self, fstring: str) -> Dict[str, str]:
        """
        Parse metadata from the filename.
        
        Expected format: 0001_QTN_1952_07_05_001_SB_Zsn128163MR.jpg
        Elements: transkribus_id_newspaper_year_month_date_page_[other info]
        
        Args:
            fstring: File path string
            
        Returns:
            Dictionary containing parsed metadata
        """
        filename = os.path.basename(fstring)
        f_attributes = filename.split('_')

        if len(f_attributes) < 6:
            raise ValueError(f"Unexpected filename format: {filename}")

        return {
            'newspaper': f_attributes[1],
            'year': f_attributes[2],
            'month': f_attributes[3],
            'date': f_attributes[4],
            'page_num': f_attributes[5]
        }

    def extract_xml(self, fname: str) -> pd.DataFrame:
        """
        Extract text paragraphs from a PAGE XML file.
        
        Args:
            fname: Path to the XML file
            
        Returns:
            DataFrame containing extracted paragraphs and metadata
        """
        with open(fname, 'r', encoding='utf-8') as f:
            data = f.read()

        root = ET.fromstring(data)
        
        content_keys = [
            'paragraph', 'paragraph_idx', 'readingorder_idx', 
            'region_type', 'filename', 'newspaper', 
            'year', 'month', 'date', 'page_num'
        ]
        contents = {k: [] for k in content_keys}

        # Extract the imageFilename attribute
        page_elem = root.find('.//ns:Page', self.namespaces)
        if page_elem is not None:
            image_filename = page_elem.get('imageFilename')
        else:
            image_filename = None

        # Parse metadata from the IMAGE filename (not the XML filename)
        if image_filename:
            file_metadata = self.parse_filename(image_filename)
        else:
            raise ValueError(f"No imageFilename found in XML file: {fname}")

        # Process each text region
        for text_region in root.findall('.//ns:TextRegion', self.namespaces):
            # Extract paragraph_idx
            region_idx = text_region.get('id')

            # Extract region_type by parsing 'custom' attribute
            custom_attribute = text_region.get('custom')
            match = re.search(r'type:([^;}]+)', custom_attribute)
            region_type = match.group(1) if match else None

            # Extract readingorder_num by parsing 'custom' attribute
            match = re.search(r'readingOrder\s*\{index:(\d+);', custom_attribute)
            readingorder_num = int(match.group(1)) if match else None

            # Extract region_text by concatenating text lines
            region_text = ''
            for text_equiv in text_region.findall('.//ns:TextEquiv/ns:Unicode', self.namespaces):
                content = text_equiv.text
                if content:
                    region_text = region_text + content
                    region_text = region_text.replace('\n', '')
                    region_text = region_text.replace('\t', ' ')

            contents['paragraph'].append(region_text)
            contents['paragraph_idx'].append(region_idx)
            contents['readingorder_idx'].append(readingorder_num)
            contents['region_type'].append(region_type)
            contents['filename'].append(image_filename)

            # Collect metadata in the correct order: newspaper, year, month, date, page_num
            contents['newspaper'].append(file_metadata['newspaper'])
            contents['year'].append(file_metadata['year'])
            contents['month'].append(file_metadata['month'])
            contents['date'].append(file_metadata['date'])
            contents['page_num'].append(file_metadata['page_num'])

        return pd.DataFrame(contents)

    def extract_all(self, xml_dir: str, output_dir: str, verbose: bool = True) -> List[str]:
        """
        Extract all XML files in the specified directory.
        
        Args:
            xml_dir: Directory containing XML files
            output_dir: Directory to save CSV outputs
            verbose: Whether to print progress messages
            
        Returns:
            List of paths to created CSV files
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Find all XML files
        xml_files = []
        for root, _, files in os.walk(xml_dir):
            for file in files:
                if file.endswith('.xml') and file not in self.excluded_files:
                    xml_files.append(os.path.join(root, file))

        if not xml_files:
            if verbose:
                print(f"No XML files found in {xml_dir}")
            return []

        if verbose:
            print(f"Found {len(xml_files)} XML files to process")

        csv_files = []
        for fname in xml_files:
            try:
                data = self.extract_xml(fname)

                # Save CSV in the output directory
                csv_filename = os.path.join(output_dir, os.path.basename(fname).replace('.xml', '.csv'))
                data.to_csv(csv_filename, index=False, encoding='utf-8-sig')

                csv_files.append(csv_filename)
                
                if verbose:
                    print(f'✓ Extracted: {os.path.basename(csv_filename)}')

            except Exception as e:
                if verbose:
                    print(f'✗ Error processing {os.path.basename(fname)}: {e}')

        return csv_files
