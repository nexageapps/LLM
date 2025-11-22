# Contributing to LLM

Thank you for your interest in contributing to the LLM project! This document provides guidelines and instructions for contributing to this repository.

## 🤝 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## 📋 Table of Contents

- [How to Contribute](#how-to-contribute)
- [Code Style and Formatting](#code-style-and-formatting)
- [Branch Naming and PR Workflow](#branch-naming-and-pr-workflow)
- [Running Tests Locally](#running-tests-locally)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Review and Merge Process](#review-and-merge-process)
- [Branch Protection](#branch-protection)

## How to Contribute

1. **Fork the repository** and clone it locally
2. **Create a new branch** for your contribution (see [Branch Naming](#branch-naming-and-pr-workflow))
3. **Make your changes** following our code style guidelines
4. **Test your changes** thoroughly
5. **Commit your changes** with clear, descriptive commit messages
6. **Push to your fork** and submit a pull request
7. **Respond to feedback** from maintainers during code review

## Code Style and Formatting

### Python Code

This project primarily uses Python. Please follow these guidelines:

- **PEP 8**: Follow [PEP 8](https://pep8.org/) style guidelines for Python code
- **Formatting**: Use [Black](https://black.readthedocs.io/) for code formatting with default settings
  ```bash
  # Install Black
  pip install black
  
  # Format your code
  black .
  ```
- **Linting**: Use [flake8](https://flake8.pycqa.org/) or [pylint](https://pylint.org/) to catch potential issues
  ```bash
  # Install flake8
  pip install flake8
  
  # Run linter
  flake8 .
  ```
- **Type hints**: Use type hints where appropriate for better code clarity
- **Docstrings**: Use clear docstrings for functions, classes, and modules

### Jupyter Notebooks

- Keep cells clean and well-organized
- Add markdown cells to explain what each section does
- Clear all output before committing (optional but recommended)

### General Guidelines

- Write clear, self-documenting code
- Add comments for complex logic
- Keep functions small and focused
- Use meaningful variable and function names

## Branch Naming and PR Workflow

### Branch Naming Convention

Use descriptive branch names that follow this pattern:

- `feature/description` - for new features
- `fix/description` - for bug fixes
- `docs/description` - for documentation updates
- `refactor/description` - for code refactoring
- `test/description` - for adding or updating tests
- `enhance/description` - for enhancements to existing features

Examples:
- `feature/add-tokenizer-support`
- `fix/encoding-unicode-error`
- `docs/update-setup-instructions`

### Pull Request Template

When creating a pull request, please use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) provided in this repository. The template includes:
- Description of changes
- Type of change
- Testing checklist
- Link to related issues
- Changelog entry requirement

## Running Tests Locally

Currently, this project uses Jupyter notebooks for demonstrations. To test your changes:

1. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt  # if requirements.txt exists
   ```

2. **Run Jupyter notebooks**:
   ```bash
   jupyter notebook
   ```

3. **Execute all cells** in modified notebooks to ensure they run without errors

4. **Verify outputs** match expected results

As the project grows, we'll add automated testing frameworks like `pytest`. Check back for updates.

## Submitting a Pull Request

Before submitting your pull request, ensure you have:

- [ ] Followed the code style guidelines
- [ ] Tested your changes locally
- [ ] Updated documentation if needed
- [ ] Added an entry to [FEATURE_UPDATES.md](FEATURE_UPDATES.md) if applicable
- [ ] Linked related issues in the PR description
- [ ] Used the PR template
- [ ] Written clear commit messages
- [ ] Ensured your branch is up to date with the main branch

### Commit Message Guidelines

Write clear, concise commit messages:
- Use present tense ("Add feature" not "Added feature")
- Start with a verb ("Add", "Fix", "Update", "Remove", etc.)
- Keep the first line under 72 characters
- Add detailed description in the body if needed

Examples:
```
Add tokenization support for special characters

This commit extends the tokenizer to handle special Unicode characters
and emoji, improving text processing capabilities.
```

## Review and Merge Process

### How Maintainers Review PRs

1. **Automated checks**: CI/CD workflows will run (if configured)
2. **Code review**: Maintainers will review your code for:
   - Correctness and functionality
   - Code quality and style
   - Documentation and tests
   - Potential security issues
3. **Feedback**: You may receive comments and change requests
4. **Approval**: Once approved, a maintainer will merge your PR

### Response Time

- Initial review: Within 1-7 days (we're a small team!)
- Follow-up reviews: Within 1-3 days

Please be patient and responsive to feedback.

## Branch Protection

The `main` branch is protected to ensure code quality and stability. Branch protection settings require:

- Pull request reviews before merging
- Passing status checks (if configured)
- Up-to-date branches before merging

For detailed information about branch protection settings and how to configure them, see [docs/BRANCH_PROTECTION.md](docs/BRANCH_PROTECTION.md).

**Note**: Only repository administrators can modify branch protection settings. If you need an exception or have questions, please open an issue.

## Questions or Need Help?

- **Questions**: Open a [GitHub Discussion](../../discussions) or an issue
- **Bug reports**: Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- **Feature requests**: Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)

Thank you for contributing to the LLM project! 🎉
