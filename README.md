# Transkribus XML to CSV Workflow

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Project](https://img.shields.io/badge/project-Divergent%20Discourses-orange.svg)](https://www.soas.ac.uk/)

A unified pipeline for processing Transkribus PageXML outputs with integrated text normalization for Tibetan text. This tool combines paragraph extraction, text normalization, and CSV merging into a single configurable workflow. The workflow integrates [transkribus_XML2CSV](https://github.com/Divergent-Discourses/transkribus_xml2csv), developed by James Engels and Christina Sabbagh, with [TibNormCSV](https://github.com/Divergent-Discourses/TibNormCSV), developed by Yuki Kyogoku and Franz Xaver Erhard, and adapted by Christina Sabbagh.

**Developed for the Divergent Discourses Project**  
SOAS University of London & Leipzig University | Funded by AHRC (UK) & DFG (Germany)

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Features](#features)
- [Workflow Steps](#workflow-steps)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration-file)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place PageXML files in data/to_process_xml/

# 3. Run the workflow
python workflow.py

# 4. Get results from data/step3_merged_csv/merged_pages.csv
```

📖 For detailed instructions, see [QUICKSTART.md](QUICKSTART.md)

## Features

- **Multi-step Pipeline**: Extract → Normalize → Merge
- **Fully Configurable**: All parameters controlled via `workflow_config.ini`
- **Preserves Intermediate Results**: Each step saves outputs to dedicated folders
- **Tibetan Text Normalization**: Integrated normalization using custom replacement tables
- **Progress Logging**: Detailed console output and optional log file
- **Modular Design**: Each step can be enabled/disabled independently

## Workflow Steps

### Step 1: Paragraph Extraction
Extracts text regions (paragraphs) from Transkribus PageXML files with metadata.

**Input**: PageXML files (`.xml`)  
**Output**: Individual CSV files with extracted paragraphs  
**Output Location**: `./data/step1_extracted_csv/`

### Step 2: Text Normalization
Applies Tibetan text normalization rules to each CSV file.

**Input**: Extracted CSV files from Step 1  
**Output**: Normalized CSV files with additional `normalised_paragraph` column  
**Output Location**: `./data/step2_normalized_csv/`

### Step 3: CSV Merging
Merges all normalized CSV files into a single master CSV.

**Input**: Normalized CSV files from Step 2  
**Output**: Single merged CSV file  
**Output Location**: `./data/step3_merged_csv/merged_pages.csv`

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone or download this repository**

```bash
git clone <repository-url>
cd transkribus-workflow
```

2. **Create a virtual environment (recommended)**

```bash
# Using conda
conda create -n transkribus-workflow python=3.12
conda activate transkribus-workflow

# Or using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Directory Structure

```
transkribus-workflow/
├── workflow.py              # Main workflow orchestrator
├── extractor.py            # Paragraph extraction module
├── normalizer.py           # Text normalization module
├── merger.py               # CSV merge module
├── workflow_config.ini     # Configuration file
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── data/
│   ├── to_process_xml/           # Place your PageXML files here
│   ├── step1_extracted_csv/      # Extracted paragraphs (auto-created)
│   ├── step2_normalized_csv/     # Normalized text (auto-created)
│   └── step3_merged_csv/         # Final merged CSV (auto-created)
│
├── tables/                        # Normalization tables
│   ├── abbreviations.tsv
│   ├── table1.tsv
│   ├── table2.tsv
│   └── table3.tsv
│
└── logs/                          # Log files (auto-created)
    └── workflow.log
```

## Usage

### Quick Start

1. **Place your PageXML files** in `./data/to_process_xml/`

2. **Ensure normalization tables** are in `./tables/`

3. **Run the workflow**:

```bash
python workflow.py
```

That's it! The workflow will:
- Extract paragraphs from all XML files
- Normalize the Tibetan text
- Merge everything into a single CSV

### Custom Configuration

Run with a custom config file:

```bash
python workflow.py --config my_config.ini
```

### Running Specific Steps

Edit `workflow_config.ini` to enable/disable steps:

```ini
[workflow]
enable_extraction = True      # Set to False to skip
enable_normalization = True   # Set to False to skip
enable_merge = True          # Set to False to skip
```

## Configuration File

The `workflow_config.ini` file controls all aspects of the workflow:

```ini
[workflow]
# Enable/disable workflow steps (executed in this order)
enable_extraction = True
enable_normalization = True
enable_merge = True

[paths]
# Input directories
xml_input_dir = ./data/to_process_xml

# Output directories for each step
extracted_csv_dir = ./data/step1_extracted_csv
normalized_csv_dir = ./data/step2_normalized_csv
merged_csv_dir = ./data/step3_merged_csv

# Normalization tables
table_path = ./tables

[extraction]
# XML namespace for PageXML parsing
namespace_uri = http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15

# Files to exclude from processing
excluded_files = mets.xml,metadata.xml

[normalization]
# Flag parameter for conditional normalization rules
flag = 1

[merge]
# Name of the merged output file
merged_filename = merged_pages.csv

[logging]
# Enable verbose logging
verbose = True
log_file = ./logs/workflow.log
```

## Input File Requirements

### PageXML Files

Files should follow the naming convention:
```
XXXX_NEWSPAPER_YEAR_MONTH_DAY_PAGE_[optional].xml
```
or (see [Bug fixes applied](BUG_FIXES_APPLIED.md))
```
NEWSPAPER_YEAR_MONTH_DAY_PAGE_[optional].xml
```

Example: `0001_QTN_1952_07_05_001_SB_Zsn128163MR.xml` or `QTN_1952_07_05_001_SB_Zsn128163MR.xml`

Where:
- `XXXX`: Transkribus-assigned ID (4 digits)
- `NEWSPAPER`: Newspaper code (e.g., QTN)
- `YEAR`: Publication year (e.g., 1952)
- `MONTH`: Publication month (e.g., 07)
- `DAY`: Publication day (e.g., 05)
- `PAGE`: Page number (e.g., 001)
- `[optional]`: Additional metadata (ignored)

For detailed information on the naming convention, see [Erhard, Franz Xaver 2025. "The Divergent Discourses Corpus. A Digital Collection of Early Tibetan Newspapers from the 1950s and 1960s." In F.X. Erhard, R. Barnett, and N.W. Hill (eds.) “From Print to Pixels: Building Digital Tools for Modern Tibetan Textual Analysis.” Special issue, Revue d'études tibétaines (RET). (74), 77–80.](https://d1i1jdw69xsqx0.cloudfront.net/digitalhimalaya/collections/journals/ret/pdf/ret_74_02.pdf)

### Normalization Tables

Four TSV files are required in the `./tables/` directory:

1. **abbreviations.tsv**: Abbreviation expansions (with flag column)
2. **table1.tsv**: Character replacements
3. **table2.tsv**: Regex-based replacements
4. **table3.tsv**: Context-aware replacements with exceptions (with flag column)

## Output Format

### CSV Columns

The final merged CSV contains:

- `paragraph`: Original extracted text
- `normalised_paragraph`: Normalized text (added in Step 2)
- `paragraph_idx`: Paragraph ID (e.g., tr_1718110017)
- `readingorder_idx`: Reading order index
- `region_type`: Type of text region (e.g., paragraph, heading, caption)
- `filename`: Original image filename
- `newspaper`: Newspaper code
- `year`: Publication year
- `month`: Publication month
- `date`: Publication day
- `page_num`: Page number

## Advanced Usage

### Modifying the Workflow

Each module (`extractor.py`, `normalizer.py`, `merger.py`) can be imported and used independently:

```python
from extractor import XMLParagraphExtractor
from normalizer import load_tables, normalize_csv_files
from merger import merge_csv_files

# Use individual components
extractor = XMLParagraphExtractor(namespace_uri, excluded_files)
csv_files = extractor.extract_all(xml_dir, output_dir)

# Load and apply normalization
tables = load_tables(table_path, flag=1)
normalized = normalize_csv_files(input_dir, output_dir, tables)

# Merge
merge_csv_files(input_dir, output_file)
```

### Customizing Normalization

Modify the `flag` parameter in `workflow_config.ini` to use different normalization rule sets:

```ini
[normalization]
flag = 1  # Use rules where flag=1
```

### Batch Processing

The workflow recursively searches for XML files, so you can organize your files in subdirectories:

```
data/to_process_xml/
├── batch1/
│   ├── file1.xml
│   └── file2.xml
└── batch2/
    ├── file3.xml
    └── file4.xml
```

## Troubleshooting

### No XML files found
- Check that XML files are in `./data/to_process_xml/`
- Ensure files have `.xml` extension
- Verify they're not in the excluded list

### Normalization errors
- Verify all required TSV files exist in `./tables/`
- Check TSV files are tab-separated and properly formatted
- Ensure `flag` column exists in `abbreviations.tsv` and `table3.tsv`

### Memory issues with large files
- Process in smaller batches
- Disable merge step and merge manually using external tools

### Encoding issues
- All files use UTF-8 encoding
- Output CSVs use UTF-8-sig for Excel compatibility

## 📚 Documentation

- **[INDEX.md](INDEX.md)** - Documentation navigation guide
- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - One-page cheat sheet
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview
- **[WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)** - Visual workflow diagrams
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting issues
- Suggesting enhancements
- Contributing code
- Development setup

## 📄 License

Copyright © 2025 SOAS University of London & Leipzig University

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Please acknowledge the Divergent Discourses project in any use of these materials.

## 👥 Credits

**Development**:
- **Original Paragraph Extractor**: James Engels, modified by Christina Sabbagh (SOAS University of London)
- **Text Normalizer**: Developed for Tibetan text processing by Yuki Kyogoku and Franz Xaver Erhard
- **Workflow Integration**: Unified processing pipeline by Franz Xaver Erhard

**Project**: Divergent Discourses  
**Institutions**: SOAS University of London & Leipzig University  
**Funding**: AHRC (UK) & DFG (Germany)

## 📧 Support

For issues or questions:
1. Check the [documentation](INDEX.md)
2. Review [existing issues](../../issues)
3. Create a [new issue](../../issues/new) if needed
4. Check `logs/workflow.log` for detailed error messages

---

**Star ⭐ this repository if you find it helpful!**

