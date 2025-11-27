# Contributing to Transkribus XML to CSV Workflow

Thank you for your interest in contributing to this project! This workflow is part of the **Divergent Discourses** project, a joint study involving SOAS University of London and Leipzig University.

## How to Contribute

### Reporting Issues

If you encounter bugs or have feature requests:

1. Check if the issue already exists in the [Issues](../../issues) section
2. If not, create a new issue with:
   - A clear, descriptive title
   - Detailed description of the problem or feature
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Your environment (OS, Python version, etc.)
   - Relevant log files from `logs/workflow.log`

### Suggesting Enhancements

We welcome suggestions for improvements:

- New features for extraction, normalization, or merging
- Performance optimizations
- Better error handling
- Documentation improvements
- Additional normalization rules

### Contributing Code

1. **Fork the repository** and create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

3. **Test your changes**
   - Run the workflow with sample data
   - Ensure all three steps work correctly
   - Check that logs are generated properly

4. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```

5. **Push to your fork and submit a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Include type hints where appropriate

### Testing

Before submitting a pull request:

- Test with sample PageXML files
- Verify all three workflow steps execute successfully
- Check that configuration options work as expected
- Ensure backward compatibility with existing config files

### Documentation

If your contribution affects user-facing functionality:

- Update relevant documentation files (README.md, QUICKSTART.md, etc.)
- Add examples if introducing new features
- Update the WORKFLOW_DIAGRAM.md if changing the process flow

## Development Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/transkribus-workflow.git
cd transkribus-workflow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python workflow.py
```

## Questions?

If you have questions about contributing:

- Open a discussion in the [Discussions](../../discussions) section
- Review existing pull requests for examples
- Check the documentation files for guidance

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the project and community
- Show empathy towards other contributors

## Attribution

Contributors will be acknowledged in the project documentation. Please ensure your commits include your name and email.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

---

**Project**: Divergent Discourses  
**Institutions**: SOAS University of London & Leipzig University  
**Funding**: AHRC (UK) & DFG (Germany)
