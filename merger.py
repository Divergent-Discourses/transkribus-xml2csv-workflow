"""
CSV Merge Module
Merges multiple CSV files into a single file
"""
import os
import pandas as pd
from typing import List


def merge_csv_files(input_dir: str, output_file: str, verbose: bool = True) -> str:
    """
    Merge all CSV files in the specified input directory.
    
    Args:
        input_dir: Directory containing CSV files to merge
        output_file: Path to save the merged CSV file
        verbose: Whether to print progress messages
        
    Returns:
        Path to the merged CSV file, or None if merge failed
    """
    input_dir = os.path.abspath(input_dir)
    output_file = os.path.abspath(output_file)

    if verbose:
        print(f"\nMerging CSV files from: {input_dir}")
        print(f"Output file: {output_file}")

    if not os.path.exists(input_dir):
        if verbose:
            print(f"✗ Error: Input folder does not exist - {input_dir}")
        return None
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find all CSV files
    all_files = [
        os.path.join(input_dir, f) 
        for f in os.listdir(input_dir) 
        if f.endswith('.csv')
    ]

    if not all_files:
        if verbose:
            print("✗ No CSV files found in the input directory.")
        return None

    if verbose:
        print(f"Found {len(all_files)} CSV files to merge")

    df_list = []
    for file in all_files:
        try:
            df = pd.read_csv(file)
            df_list.append(df)
            if verbose:
                print(f"  ✓ Read: {os.path.basename(file)} ({len(df)} rows)")
        except Exception as e:
            if verbose:
                print(f"  ✗ Error reading {os.path.basename(file)}: {e}")

    if df_list:
        merged_df = pd.concat(df_list, ignore_index=True)
        merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')

        if verbose:
            print(f"\n✓ Successfully merged {len(df_list)} files into {os.path.basename(output_file)}")
            print(f"  Total rows: {len(merged_df)}")
        
        return output_file
    else:
        if verbose:
            print("✗ No valid CSV files to merge.")
        return None
