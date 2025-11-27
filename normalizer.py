"""
Text Normalization Module
Applies normalization rules to Tibetan text using replacement tables
"""
import glob
import os
import pandas as pd
import re
from typing import Dict, List


def load_tables(table_path: str, flag: int, verbose: bool = True) -> Dict[str, pd.DataFrame]:
    """
    Load normalization tables from TSV files.
    
    Args:
        table_path: Directory containing TSV table files
        flag: Flag value for conditional filtering
        verbose: Whether to print progress messages
        
    Returns:
        Dictionary where keys are filenames and values are DataFrames
    """
    tables = {}
    pattern = os.path.join(table_path, '*.tsv')
    files = [file for file in glob.glob(pattern, recursive=True) if os.path.isfile(file)]
    flag_tables = ['abbreviations', 'table3']

    if verbose:
        print(f"Loading normalization tables from: {table_path}")

    for file in files:
        file_name = os.path.basename(file).split('.')[0]
        df = pd.read_csv(file, sep='\t', escapechar='\\', index_col=None)
        
        if file_name in flag_tables:
            df['flag'] = df['flag'].apply(pd.to_numeric, errors='coerce').astype('Int64')
            tables[file_name] = df[df['flag'] == flag]  # Apply flag filter
            if verbose:
                print(f"  ✓ Loaded {file_name}.tsv (filtered by flag={flag}): {len(tables[file_name])} rules")
        else:
            tables[file_name] = df
            if verbose:
                print(f"  ✓ Loaded {file_name}.tsv: {len(tables[file_name])} rules")

    return tables


def norm_text(text, tables: Dict[str, pd.DataFrame]) -> str:
    """
    Apply all normalization steps sequentially to a single text string.
    
    Args:
        text: Input text string
        tables: Dictionary of normalization tables
        
    Returns:
        Normalized text string
    """
    if not isinstance(text, str):
        return text  # Ensure NaN or other types are not processed

    def apply_replacements(text: str, table_name: str) -> str:
        """
        Generic function to apply replacements using a given normalization table.
        
        Args:
            text: Input text
            table_name: Name of the table to use
            
        Returns:
            Text with replacements applied
        """
        if table_name not in tables:
            return text
        
        table = tables[table_name].set_index('transcription')['normalisation'].to_dict()
        
        for key, value in table.items():
            if table_name == 'table2':
                # Use regex replacement for table2
                text = re.sub(key, value, text)
            else:
                # Use string replacement for other tables
                text = text.replace(key, value)
        
        return text

    # Apply normalisations in sequence
    text = apply_replacements(text, 'abbreviations')
    text = apply_replacements(text, 'table1')
    text = apply_replacements(text, 'table2')

    # Handling table3 with exceptions
    if 'table3' in tables:
        table3 = tables['table3']
        text_list = list(text)
        
        for _, row in table3.iterrows():
            transcription = row['transcription']
            norm = row['normalisation']
            exc = row['exception']
            exc_len = row['exc_len']
            scope = row['scope']
            exception = re.compile(exc)

            for i in range(len(text_list)):
                pos_end = i + len(transcription)
                start = max(0, i - exc_len)
                end = min(len(text_list), pos_end + exc_len)
                
                # Determine the range to check based on scope
                if scope == 'left':
                    str_range = ''.join(text_list[start:i])
                elif scope == 'right':
                    str_range = ''.join(text_list[pos_end:end])
                else:  # 'both'
                    str_range = ''.join(text_list[start:i]) + ''.join(text_list[pos_end:end])
                
                # Check if exception pattern is NOT found
                if not exception.search(str_range):
                    if len(transcription) > 1 and text_list[i:pos_end] == list(transcription):
                        # Multi-character replacement
                        text_list[i:pos_end] = [norm] + [''] * (pos_end - i - 1)
                    elif text_list[i] == transcription:
                        # Single-character replacement
                        text_list[i] = norm
        
        text = ''.join(text_list)

    return text


def normalize_csv_files(input_dir: str, output_dir: str, tables: Dict[str, pd.DataFrame], 
                        verbose: bool = True) -> List[str]:
    """
    Normalize all CSV files in the input directory.
    
    Args:
        input_dir: Directory containing CSV files to normalize
        output_dir: Directory to save normalized CSV files
        tables: Dictionary of normalization tables
        verbose: Whether to print progress messages
        
    Returns:
        List of paths to normalized CSV files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Find all CSV files
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    if not csv_files:
        if verbose:
            print(f"No CSV files found in {input_dir}")
        return []

    if verbose:
        print(f"\nNormalizing {len(csv_files)} CSV files...")

    normalized_files = []
    
    for csv_file in csv_files:
        input_path = os.path.join(input_dir, csv_file)
        output_path = os.path.join(output_dir, csv_file)
        
        try:
            df = pd.read_csv(input_path)

            if 'paragraph' not in df.columns:
                if verbose:
                    print(f"  ⚠ Skipping {csv_file}: no 'paragraph' column found")
                continue

            # Apply normalization and insert normalized column after paragraph column
            df.insert(
                df.columns.get_loc('paragraph') + 1, 
                'normalised_paragraph', 
                df['paragraph'].apply(lambda text: norm_text(text, tables))
            )

            df.to_csv(output_path, index=False, encoding='utf-8-sig')
            normalized_files.append(output_path)
            
            if verbose:
                print(f"  ✓ Normalized: {csv_file}")

        except Exception as e:
            if verbose:
                print(f"  ✗ Error normalizing {csv_file}: {e}")

    return normalized_files
