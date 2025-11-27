# Transkribus XML to CSV Workflow - Project Summary

## Overview

This unified workflow combines three previously separate tools into a single, configurable pipeline:
1. **Paragraph Extractor** - Extracts text regions from Transkribus PageXML
2. **Text Normalizer** - Applies Tibetan text normalization rules
3. **CSV Merger** - Combines all processed files into a master CSV

## Key Features

✓ **Integrated Pipeline**: All three steps run in sequence automatically
✓ **Configurable**: Control every aspect via `workflow_config.ini`
✓ **Preserves Intermediate Results**: Each step outputs to its own directory
✓ **Optimal Processing Order**: Extract → Normalize → Merge
✓ **Modular Design**: Each component can be used independently
✓ **Comprehensive Logging**: Track progress and debug issues easily

## What's Different from Original Tools?

### Original Setup
- **3 separate scripts** that had to be run manually in sequence
- Manual file management between steps
- Limited configuration options
- Had to remember correct order of operations

### New Unified Workflow
- **Single command** runs entire pipeline: `python workflow.py`
- Automatic file management and directory creation
- Comprehensive configuration file
- Guaranteed correct execution order
- Built-in error handling and validation

## Directory Structure

```
transkribus-workflow/
│
├── workflow.py              # Main orchestrator (NEW)
├── extractor.py            # Extraction module (refactored)
├── normalizer.py           # Normalization module (refactored)
├── merger.py               # Merge module (refactored)
├── workflow_config.ini     # Central configuration (NEW)
├── requirements.txt        # Python dependencies
├── README.md              # Full documentation
├── QUICKSTART.md          # Quick start guide (NEW)
│
├── data/                           # All data files
│   ├── to_process_xml/            # INPUT: Place XML files here
│   ├── step1_extracted_csv/       # OUTPUT: Extracted paragraphs
│   ├── step2_normalized_csv/      # OUTPUT: Normalized text
│   └── step3_merged_csv/          # OUTPUT: Final merged CSV
│
├── tables/                         # Normalization tables
│   ├── abbreviations.tsv          # Abbreviation expansions
│   ├── table1.tsv                 # Character replacements
│   ├── table2.tsv                 # Regex replacements
│   └── table3.tsv                 # Context-aware replacements
│
└── logs/                           # Processing logs (NEW)
    └── workflow.log
```

## Workflow Execution Order

The workflow has been optimized to process in this order:

### Step 1: Extraction
- **Input**: PageXML files from `data/to_process_xml/`
- **Process**: Extract text regions, metadata, and reading order
- **Output**: Individual CSV files in `data/step1_extracted_csv/`
- **Columns Created**: paragraph, paragraph_idx, readingorder_idx, region_type, filename, newspaper, year, month, date, page_num

### Step 2: Normalization
- **Input**: Extracted CSV files from Step 1
- **Process**: Apply Tibetan text normalization using 4 TSV tables
- **Output**: CSV files with normalized text in `data/step2_normalized_csv/`
- **Columns Added**: normalised_paragraph (inserted after 'paragraph')

### Step 3: Merge
- **Input**: Normalized CSV files from Step 2
- **Process**: Concatenate all CSV files into one master file
- **Output**: Single file `data/step3_merged_csv/merged_pages.csv`
- **Final Columns**: paragraph, normalised_paragraph, paragraph_idx, readingorder_idx, region_type, filename, newspaper, year, month, date, page_num

## Configuration Options

The `workflow_config.ini` file controls all aspects:

```ini
[workflow]
enable_extraction = True       # Toggle extraction step
enable_normalization = True    # Toggle normalization step
enable_merge = True           # Toggle merge step

[paths]
xml_input_dir = ./data/to_process_xml
extracted_csv_dir = ./data/step1_extracted_csv
normalized_csv_dir = ./data/step2_normalized_csv
merged_csv_dir = ./data/step3_merged_csv
table_path = ./tables

[extraction]
namespace_uri = http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15
excluded_files = mets.xml,metadata.xml

[normalization]
flag = 1                      # Controls which normalization rules to apply

[merge]
merged_filename = merged_pages.csv

[logging]
verbose = True
log_file = ./logs/workflow.log
```

## Usage Examples

### Basic Usage
```bash
# Run complete workflow
python workflow.py

# Use custom config
python workflow.py --config custom_config.ini
```

### Selective Processing

**Run only extraction:**
```ini
[workflow]
enable_extraction = True
enable_normalization = False
enable_merge = False
```

**Skip normalization:**
```ini
[workflow]
enable_extraction = True
enable_normalization = False
enable_merge = True
```

**Re-normalize with different flag:**
```ini
[workflow]
enable_extraction = False
enable_normalization = True
enable_merge = True

[normalization]
flag = 0  # Changed from 1
```

## Testing

A sample PageXML file is included for testing:
- Location: `data/to_process_xml/0001_QTN_1959_10_03_001_SB_Zsn128163MR.xml`
- Contains 3 text regions (1 heading, 2 paragraphs)
- Demonstrates complete workflow

**Test Results:**
```
✓ Extraction: 1 CSV file created (3 paragraphs)
✓ Normalization: Text normalized with 6,583 total rules
✓ Merge: Final CSV with 3 rows, 11 columns
```

## Module Independence

Each module can be used independently in your own Python scripts:

```python
# Use extraction only
from extractor import XMLParagraphExtractor
extractor = XMLParagraphExtractor(namespace_uri, excluded_files)
csv_files = extractor.extract_all(xml_dir, output_dir)

# Use normalization only
from normalizer import load_tables, normalize_csv_files
tables = load_tables(table_path, flag=1)
normalized = normalize_csv_files(input_dir, output_dir, tables)

# Use merge only
from merger import merge_csv_files
merge_csv_files(input_dir, output_file)
```

## File Requirements

### PageXML Files
Filename format: `XXXX_NEWSPAPER_YEAR_MONTH_DAY_PAGE_[optional].xml`
Example: `0001_QTN_1959_10_03_001_SB_Zsn128163MR.xml`

### Normalization Tables
Required TSV files in `./tables/`:
- `abbreviations.tsv` - Must have 'flag' column
- `table1.tsv` - Simple character replacements
- `table2.tsv` - Regex pattern replacements
- `table3.tsv` - Context-aware with exceptions, must have 'flag' column

## Output Format

Final CSV columns:
1. **paragraph** - Original text from PageXML
2. **normalised_paragraph** - Normalized text (NEW)
3. **paragraph_idx** - Unique paragraph ID
4. **readingorder_idx** - Reading sequence number
5. **region_type** - Type: heading, paragraph, caption, etc.
6. **filename** - Source image filename
7. **newspaper** - Newspaper code (parsed from filename)
8. **year** - Publication year
9. **month** - Publication month
10. **date** - Publication day
11. **page_num** - Page number

## Performance Notes

- **Small datasets** (< 100 files): ~seconds to process
- **Medium datasets** (100-1000 files): ~minutes to process
- **Large datasets** (1000+ files): May take hours depending on file size
- Progress is logged in real-time to console and log file

## Error Handling

The workflow includes comprehensive error handling:
- Missing directories are created automatically
- Invalid XML files are skipped with error messages
- Failed steps prevent subsequent steps from running
- All errors are logged to `logs/workflow.log`
- Exit code 0 on success, 1 on failure

## Advantages Over Original Setup

| Feature | Original | New Workflow |
|---------|----------|--------------|
| Commands to run | 3 separate | 1 unified |
| Configuration | Hardcoded | Config file |
| Order enforcement | Manual | Automatic |
| Progress tracking | Limited | Comprehensive |
| Error handling | Basic | Robust |
| Intermediate results | Optional | Automatic |
| Logging | Console only | Console + file |
| Reusability | Scripts only | Modules + scripts |

## Credits

**Divergent Discourses Project**
- SOAS University of London & Leipzig University
- Funded by AHRC (UK) and DFG (Germany)

**Development**:
- Original Paragraph Extractor: James Engels, modified by Christina Sabbagh
- Text Normalizer: Developed for Tibetan text processing
- Workflow Integration: Created for unified processing pipeline

## Support

For issues or questions:
1. Check `logs/workflow.log` for detailed error messages
2. Review `QUICKSTART.md` for common solutions
3. Verify configuration in `workflow_config.ini`
4. Consult full documentation in `README.md`

## License

Copyright: SOAS University of London & Leipzig University
Please acknowledge the Divergent Discourses project in any use of these materials.
