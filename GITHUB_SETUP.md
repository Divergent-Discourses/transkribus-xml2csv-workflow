# GitHub Setup Guide

This guide will help you publish the Transkribus XML to CSV Workflow on GitHub.

## 📋 Pre-Publication Checklist

Before publishing, ensure you have:

- ✅ All core Python modules (workflow.py, extractor.py, normalizer.py, merger.py)
- ✅ Configuration file (workflow_config.ini)
- ✅ Requirements file (requirements.txt)
- ✅ Documentation files (README.md, QUICKSTART.md, etc.)
- ✅ License file (LICENSE)
- ✅ .gitignore file
- ✅ Directory structure with .gitkeep files
- ✅ Normalization tables in tables/ directory

All files are included and ready to publish!

## 🚀 Publishing to GitHub

### Option 1: Using GitHub Web Interface

1. **Create a new repository on GitHub**
   - Go to https://github.com/new
   - Repository name: `transkribus-xml2csv-workflow` (or your preferred name)
   - Description: "Unified pipeline for processing Transkribus PageXML with Tibetan text normalization"
   - Choose Public or Private
   - Do NOT initialize with README (we already have one)
   - Click "Create repository"

2. **Upload files**
   - On the new repository page, click "uploading an existing file"
   - Drag and drop all files and folders from this directory
   - Write commit message: "Initial commit: Complete workflow system"
   - Click "Commit changes"

### Option 2: Using Git Command Line

1. **Initialize Git repository locally**
   ```bash
   cd /path/to/this/directory
   git init
   git add .
   git commit -m "Initial commit: Complete workflow system"
   ```

2. **Create repository on GitHub**
   - Go to https://github.com/new
   - Follow steps from Option 1 to create empty repository
   - Copy the repository URL (e.g., https://github.com/username/repo-name.git)

3. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/USERNAME/REPO-NAME.git
   git branch -M main
   git push -u origin main
   ```

### Option 3: Using GitHub Desktop

1. **Open GitHub Desktop**
2. **File → Add Local Repository**
3. **Choose this directory**
4. **Publish repository** button in top right
5. **Fill in details and click "Publish Repository"**

## 📝 Recommended Repository Settings

### After Publishing

1. **Add Topics** (in About section):
   - `transkribus`
   - `pagexml`
   - `text-normalization`
   - `tibetan-language`
   - `digital-humanities`
   - `ocr`
   - `workflow`
   - `csv-processing`

2. **Enable Discussions**
   - Go to Settings → General
   - Check "Discussions" under Features
   - This allows users to ask questions

3. **Set up Issues Templates** (Optional)
   - Go to Settings → Features → Issues → Set up templates
   - Create templates for:
     - Bug Report
     - Feature Request
     - Question

4. **Add Repository Description**
   - Click ⚙️ next to About
   - Add: "Unified pipeline for extracting, normalizing, and merging Transkribus PageXML outputs. Built for the Divergent Discourses project."
   - Add website: https://www.soas.ac.uk/ (or project website)

5. **Branch Protection** (if working with collaborators)
   - Settings → Branches
   - Add branch protection rule for `main`
   - Require pull request reviews

## 🏷️ Creating First Release

1. **Go to Releases** (right sidebar)
2. **"Create a new release"**
3. **Choose a tag**: v1.0.0
4. **Release title**: v1.0.0 - Initial Release
5. **Description**:
   ```
   ## First Release of Transkribus XML to CSV Workflow
   
   ### Features
   - Complete extraction, normalization, and merge pipeline
   - Configurable workflow via INI file
   - Comprehensive documentation
   - Tested with Tibetan text normalization
   
   ### Installation
   ```bash
   pip install -r requirements.txt
   ```
   
   ### Usage
   ```bash
   python workflow.py
   ```
   
   See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.
   ```
6. **Click "Publish release"**

## 📊 GitHub Actions

The repository includes a GitHub Actions workflow that will:
- Automatically test the code on push/pull request
- Test on Python 3.8, 3.9, 3.10, 3.11, and 3.12
- Verify all workflow steps execute successfully
- Check code style with flake8

View test results in the "Actions" tab after pushing.

## 🔗 Recommended README Badge Updates

After publishing, update badges in README.md with your actual repository info:

```markdown
[![GitHub release](https://img.shields.io/github/release/USERNAME/REPO-NAME.svg)](https://github.com/USERNAME/REPO-NAME/releases)
[![GitHub issues](https://img.shields.io/github/issues/USERNAME/REPO-NAME.svg)](https://github.com/USERNAME/REPO-NAME/issues)
[![GitHub stars](https://img.shields.io/github/stars/USERNAME/REPO-NAME.svg)](https://github.com/USERNAME/REPO-NAME/stargazers)
```

## 📢 Promoting Your Repository

### After Publishing:

1. **Add to related awesome lists**
   - awesome-digital-humanities
   - awesome-nlp
   - awesome-python

2. **Share with:**
   - Transkribus community forums
   - Digital humanities mailing lists
   - Tibetan studies communities
   - Academic Twitter/social media

3. **Submit to:**
   - Papers with Code (if publishing paper)
   - Research software directories
   - University research repositories

## 🔐 Security Considerations

1. **Never commit:**
   - Actual research data (XML files)
   - Personal information
   - API keys or passwords
   - Large binary files

2. **Use .gitignore** (already included)
   - Protects against accidental commits

3. **Regular updates:**
   - Keep dependencies updated
   - Monitor for security vulnerabilities

## 📦 What Gets Published

The .gitignore is configured to publish:

✅ **Included:**
- All Python source code
- Documentation files
- Configuration template
- Requirements file
- License
- Directory structure (.gitkeep files)
- Normalization tables (in tables/)
- Sample test file (optional)

❌ **Excluded (by .gitignore):**
- Python cache files (__pycache__)
- Virtual environments (venv/)
- Log files (logs/*.log)
- Processed data (data/*/files)
- IDE settings (.vscode/, .idea/)

## 🎯 Post-Publication Maintenance

### Regular Tasks:

1. **Monitor Issues**
   - Respond to bug reports
   - Consider feature requests
   - Help users with questions

2. **Update Documentation**
   - Keep README current
   - Add FAQ based on common questions
   - Update version numbers

3. **Release Management**
   - Tag new versions when making changes
   - Write clear release notes
   - Maintain CHANGELOG.md (optional)

4. **Dependency Updates**
   - Regularly update requirements.txt
   - Test with new Python versions
   - Update GitHub Actions workflow

## 📋 Suggested Repository Structure

```
your-repo/
├── .github/
│   └── workflows/
│       └── test.yml           # CI/CD configuration
├── data/
│   ├── to_process_xml/
│   │   └── .gitkeep          # Preserves directory
│   ├── step1_extracted_csv/
│   │   └── .gitkeep
│   ├── step2_normalized_csv/
│   │   └── .gitkeep
│   └── step3_merged_csv/
│       └── .gitkeep
├── logs/
│   └── .gitkeep
├── tables/
│   ├── abbreviations.tsv      # Include these
│   ├── table1.tsv
│   ├── table2.tsv
│   └── table3.tsv
├── .gitignore                 # Important!
├── CONTRIBUTING.md
├── INDEX.md
├── LICENSE
├── PROJECT_SUMMARY.md
├── QUICKSTART.md
├── QUICK_REFERENCE.md
├── README.md                  # Main page
├── WORKFLOW_DIAGRAM.md
├── extractor.py
├── merger.py
├── normalizer.py
├── requirements.txt
├── workflow.py
└── workflow_config.ini
```

## ✅ Verification Checklist

Before going live, verify:

- [ ] README.md displays correctly on GitHub
- [ ] All internal links work (test by clicking)
- [ ] Code syntax highlighting works
- [ ] License is appropriate
- [ ] .gitignore works (no sensitive files committed)
- [ ] Sample data is removed (if any)
- [ ] GitHub Actions passes (if enabled)
- [ ] All documentation files are linked from INDEX.md

## 🎉 You're Ready!

Your repository is now ready to be published on GitHub. Choose your preferred method above and follow the steps.

### Quick Command Summary

```bash
# Navigate to directory
cd /path/to/workflow

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: Complete workflow system"

# Add remote (replace with your URL)
git remote add origin https://github.com/USERNAME/REPO-NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 📞 Need Help?

- GitHub Documentation: https://docs.github.com
- GitHub Community: https://github.community
- Git Documentation: https://git-scm.com/doc

---

**Good luck with your publication!** 🚀
