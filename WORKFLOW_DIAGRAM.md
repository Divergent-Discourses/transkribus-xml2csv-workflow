# Workflow Diagram

## Complete Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TRANSKRIBUS XML TO CSV WORKFLOW                   │
│                      Divergent Discourses Project                    │
└─────────────────────────────────────────────────────────────────────┘

                              ┌──────────────────┐
                              │  Configuration   │
                              │workflow_config.ini│
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Workflow Manager │
                              │   workflow.py    │
                              └────────┬─────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────────┐
│                           STEP 1: EXTRACTION                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  INPUT:                             MODULE:                          │
│  ┌───────────────────┐              extractor.py                    │
│  │ PageXML Files     │              XMLParagraphExtractor            │
│  │ (.xml)            │                                               │
│  └─────────┬─────────┘                                               │
│            │                                                          │
│            ▼                                                          │
│  ┌────────────────────┐                                              │
│  │ Parse XML Structure│──► Extract text regions                     │
│  │ Extract Metadata   │──► Parse reading order                      │
│  │ Parse Filenames    │──► Extract region types                     │
│  └────────┬───────────┘                                              │
│            │                                                          │
│            ▼                                                          │
│  OUTPUT:                                                             │
│  ┌───────────────────────────────────────────┐                      │
│  │ Individual CSV Files                      │                      │
│  │ data/step1_extracted_csv/*.csv            │                      │
│  │                                           │                      │
│  │ Columns:                                  │                      │
│  │ • paragraph                               │                      │
│  │ • paragraph_idx                           │                      │
│  │ • readingorder_idx                        │                      │
│  │ • region_type                             │                      │
│  │ • filename, newspaper, year, month, date  │                      │
│  └───────────────────┬───────────────────────┘                      │
│                      │                                               │
└──────────────────────┼───────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        STEP 2: NORMALIZATION                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  INPUT:                             MODULE:                          │
│  ┌───────────────────┐              normalizer.py                   │
│  │ Extracted CSVs    │              load_tables()                   │
│  │ (from Step 1)     │              normalize_csv_files()           │
│  └─────────┬─────────┘                                               │
│            │                        ┌──────────────────┐            │
│            │                        │ Normalization    │            │
│            ├────────────────────────┤ Tables (TSV)     │            │
│            │                        │ • abbreviations  │            │
│            │                        │ • table1         │            │
│            │                        │ • table2         │            │
│            │                        │ • table3         │            │
│            ▼                        └──────────────────┘            │
│  ┌────────────────────┐                                              │
│  │ Apply Normalization│──► Load tables with flag filter            │
│  │ Rules:             │──► Apply abbreviations                     │
│  │ 1. Abbreviations   │──► Apply character replacements            │
│  │ 2. Table1 (chars)  │──► Apply regex replacements                │
│  │ 3. Table2 (regex)  │──► Apply context-aware rules               │
│  │ 4. Table3 (context)│                                             │
│  └────────┬───────────┘                                              │
│            │                                                          │
│            ▼                                                          │
│  OUTPUT:                                                             │
│  ┌───────────────────────────────────────────┐                      │
│  │ Normalized CSV Files                      │                      │
│  │ data/step2_normalized_csv/*.csv           │                      │
│  │                                           │                      │
│  │ New Column Added:                         │                      │
│  │ • normalised_paragraph ⭐                 │                      │
│  │                                           │                      │
│  │ (All original columns preserved)          │                      │
│  └───────────────────┬───────────────────────┘                      │
│                      │                                               │
└──────────────────────┼───────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────────┐
│                           STEP 3: MERGE                               │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  INPUT:                             MODULE:                          │
│  ┌───────────────────┐              merger.py                       │
│  │ Normalized CSVs   │              merge_csv_files()               │
│  │ (from Step 2)     │                                               │
│  └─────────┬─────────┘                                               │
│            │                                                          │
│            ▼                                                          │
│  ┌────────────────────┐                                              │
│  │ Concatenate Files  │──► Read all CSV files                       │
│  │                    │──► Combine into single DataFrame            │
│  │                    │──► Reset index                              │
│  │                    │──► Write to output                          │
│  └────────┬───────────┘                                              │
│            │                                                          │
│            ▼                                                          │
│  OUTPUT:                                                             │
│  ┌───────────────────────────────────────────┐                      │
│  │ Single Merged CSV File                    │                      │
│  │ data/step3_merged_csv/merged_pages.csv    │                      │
│  │                                           │                      │
│  │ All Columns:                              │                      │
│  │ • paragraph                               │                      │
│  │ • normalised_paragraph ⭐                 │                      │
│  │ • paragraph_idx                           │                      │
│  │ • readingorder_idx                        │                      │
│  │ • region_type                             │                      │
│  │ • filename                                │                      │
│  │ • newspaper, year, month, date, page_num  │                      │
│  │                                           │                      │
│  │ ✓ Ready for analysis!                     │                      │
│  └───────────────────────────────────────────┘                      │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘

                              ┌──────────────────┐
                              │   Log File       │
                              │ logs/workflow.log│
                              │ (All steps       │
                              │  logged here)    │
                              └──────────────────┘


┌──────────────────────────────────────────────────────────────────────┐
│                          KEY ADVANTAGES                               │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ✓ Single command execution (python workflow.py)                    │
│  ✓ Automatic directory creation                                     │
│  ✓ Preserves all intermediate results                               │
│  ✓ Comprehensive error handling                                     │
│  ✓ Configurable via workflow_config.ini                             │
│  ✓ Can enable/disable any step                                      │
│  ✓ Progress logging to console + file                               │
│  ✓ Modular design - use components independently                    │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────┐
│                      CONFIGURATION CONTROL                            │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Enable/Disable Steps:                                               │
│  ┌────────────────────────────────────────────────────────┐         │
│  │ [workflow]                                             │         │
│  │ enable_extraction = True/False                         │         │
│  │ enable_normalization = True/False                      │         │
│  │ enable_merge = True/False                              │         │
│  └────────────────────────────────────────────────────────┘         │
│                                                                       │
│  Control Normalization:                                              │
│  ┌────────────────────────────────────────────────────────┐         │
│  │ [normalization]                                        │         │
│  │ flag = 1  (controls which rules apply)                 │         │
│  └────────────────────────────────────────────────────────┘         │
│                                                                       │
│  Customize Paths:                                                    │
│  ┌────────────────────────────────────────────────────────┐         │
│  │ [paths]                                                │         │
│  │ xml_input_dir = ./data/to_process_xml                  │         │
│  │ extracted_csv_dir = ./data/step1_extracted_csv         │         │
│  │ normalized_csv_dir = ./data/step2_normalized_csv       │         │
│  │ merged_csv_dir = ./data/step3_merged_csv               │         │
│  │ table_path = ./tables                                  │         │
│  └────────────────────────────────────────────────────────┘         │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

## Data Flow Summary

```
PageXML Files
     │
     ├─► EXTRACT ──► Individual CSVs (with paragraph column)
     │                    │
     │                    ├─► NORMALIZE ──► CSVs (+ normalised_paragraph)
     │                                            │
     │                                            ├─► MERGE ──► Single CSV
     │                                                              │
     │                                                              ▼
     └──────────────────────────────────────────────────► FINAL OUTPUT


Input:  100 XML files
Step 1: 100 extracted CSV files
Step 2: 100 normalized CSV files  
Step 3: 1 merged CSV file (all data combined)
```

## File Naming Convention

```
Input XML:  0001_QTN_1959_10_03_001_SB_Zsn128163MR.xml
            └┬─┘ └┬┘ └──┬──┘ └┬┘ └┬┘ └─┬┘
             │    │     │     │   │    │
         Transk News Year  Month Day Page
          ID     Code

Output CSV: 0001_QTN_1959_10_03_001_SB_Zsn128163MR.csv
            (same name, different extension)
```
