# Transkribus XML to CSV Workflow - Documentation Index

Welcome to the unified Transkribus processing workflow! This index will help you find the right documentation for your needs.

## 📚 Documentation Files

### For Getting Started
1. **[QUICKSTART.md](QUICKSTART.md)** ⭐ START HERE
   - Installation (5 minutes)
   - Basic usage (3 steps)
   - Common scenarios
   - Troubleshooting quick fixes

2. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)**
   - One-page cheat sheet
   - Command quick reference
   - Configuration snippets
   - Common problems & solutions

### For Understanding the System
3. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**
   - Complete project overview
   - Key features and improvements
   - Workflow execution order
   - Comparison with original tools

4. **[WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)**
   - Visual workflow representation
   - Data flow diagrams
   - Configuration control overview
   - Step-by-step process maps

5. **[README.md](README.md)**
   - Comprehensive documentation
   - Detailed feature descriptions
   - Advanced usage examples
   - Module-level API documentation
   - Complete troubleshooting guide

## 🔧 Core Files

### Python Modules
- **`workflow.py`** - Main orchestrator script
- **`extractor.py`** - PageXML extraction module
- **`normalizer.py`** - Text normalization module
- **`merger.py`** - CSV merging module

### Configuration
- **`workflow_config.ini`** - Central configuration file
- **`requirements.txt`** - Python dependencies

## 📁 Directory Structure

```
transkribus-workflow/
│
├── 📖 Documentation
│   ├── QUICKSTART.md          ← Start here!
│   ├── QUICK_REFERENCE.md     ← Cheat sheet
│   ├── PROJECT_SUMMARY.md     ← Overview
│   ├── WORKFLOW_DIAGRAM.md    ← Visual guide
│   └── README.md              ← Complete docs
│
├── 🐍 Python Modules
│   ├── workflow.py            ← Main script
│   ├── extractor.py           ← Step 1: Extract
│   ├── normalizer.py          ← Step 2: Normalize
│   └── merger.py              ← Step 3: Merge
│
├── ⚙️ Configuration
│   ├── workflow_config.ini    ← Settings
│   └── requirements.txt       ← Dependencies
│
├── 📊 Data Directories
│   ├── to_process_xml/        ← INPUT: Put XML files here
│   ├── step1_extracted_csv/   ← OUTPUT: Extracted paragraphs
│   ├── step2_normalized_csv/  ← OUTPUT: Normalized text
│   └── step3_merged_csv/      ← OUTPUT: Final merged CSV
│
├── 📋 Normalization Tables
│   ├── abbreviations.tsv      ← Abbreviation rules
│   ├── table1.tsv             ← Character replacements
│   ├── table2.tsv             ← Regex patterns
│   └── table3.tsv             ← Context-aware rules
│
└── 📝 Logs
    └── workflow.log           ← Processing log
```

## 🚀 Quick Navigation by Task

### I want to...

#### Get started quickly
→ Read **[QUICKSTART.md](QUICKSTART.md)** (5 min read)
→ Follow the 3 steps to run your first workflow

#### Understand what this does
→ Read **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** (10 min read)
→ See the workflow diagram in **[WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)**

#### Configure the workflow
→ Edit **`workflow_config.ini`**
→ Check configuration examples in **[README.md](README.md)** § Configuration File

#### Run the workflow
```bash
python workflow.py
```
→ See usage examples in **[QUICKSTART.md](QUICKSTART.md)** § Running the Workflow

#### Run only certain steps
→ Edit `workflow_config.ini` [workflow] section
→ Set `enable_extraction`, `enable_normalization`, or `enable_merge` to True/False

#### Troubleshoot problems
→ Check **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** § Troubleshooting
→ Review **`logs/workflow.log`** for detailed error messages
→ See full troubleshooting in **[README.md](README.md)** § Troubleshooting

#### Use modules independently
→ See module usage examples in **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** § Module Independence
→ Read API documentation in **[README.md](README.md)** § Advanced Usage

#### Understand the input format
→ Check **[README.md](README.md)** § Input File Requirements
→ See filename format in **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** § Filename Format

#### Understand the output format
→ Check **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** § Workflow Execution Order
→ See column descriptions in **[README.md](README.md)** § Output Format

## 📖 Reading Paths by Role

### Researcher/End User
1. Start: **[QUICKSTART.md](QUICKSTART.md)**
2. Reference: **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)**
3. Detailed info: **[README.md](README.md)** (as needed)

### Project Manager/PI
1. Overview: **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**
2. Visual guide: **[WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)**
3. Capabilities: **[README.md](README.md)**

### Developer/Programmer
1. Architecture: **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** § Module Independence
2. Code modules: **`extractor.py`**, **`normalizer.py`**, **`merger.py`**
3. API: **[README.md](README.md)** § Advanced Usage
4. Configuration: **`workflow_config.ini`**

### System Administrator
1. Installation: **[QUICKSTART.md](QUICKSTART.md)** § Installation
2. Configuration: **`workflow_config.ini`**
3. Troubleshooting: **[README.md](README.md)** § Troubleshooting
4. Logs: **`logs/workflow.log`**

## 🎯 Common Scenarios

| Scenario | Quick Solution | Documentation |
|----------|----------------|---------------|
| First time user | Install & run with defaults | [QUICKSTART.md](QUICKSTART.md) |
| Need help fast | Check one-page reference | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) |
| Want to skip normalization | Set `enable_normalization = False` | [README.md](README.md) § Configuration |
| Processing fails | Check `logs/workflow.log` | [README.md](README.md) § Troubleshooting |
| Custom paths needed | Edit `[paths]` section | `workflow_config.ini` |
| Different normalization rules | Change `flag` parameter | [README.md](README.md) § Normalization |
| Integrate with other code | Import modules | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) § Module Usage |

## 🔗 External Resources

- **Transkribus Platform**: https://www.transkribus.org/
- **Project Information**: Divergent Discourses (SOAS & Leipzig)
- **Funding**: AHRC (UK) & DFG (Germany)

## 📬 Support

1. Check the **[QUICKSTART.md](QUICKSTART.md)** troubleshooting section
2. Review **`logs/workflow.log`** for error details
3. Consult the **[README.md](README.md)** comprehensive guide
4. Contact project maintainers

## ⚡ TL;DR - Absolute Quickest Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Put your XML files in data/to_process_xml/

# 3. Run the workflow
python workflow.py

# 4. Get your results from data/step3_merged_csv/merged_pages.csv
```

That's it! For more details, read [QUICKSTART.md](QUICKSTART.md).

---

**Last Updated**: November 2025  
**Version**: 1.0  
**Project**: Divergent Discourses  
**Copyright**: SOAS University of London & Leipzig University
