# Contributing Guidelines

Thank you for considering contributing to the LLM project! This document provides guidelines and best practices for contributing to this repository.

---

## 📋 Table of Contents

1. [Code Style and Formatting](#code-style-and-formatting)
2. [Branch Naming and PR Workflow](#branch-naming-and-pr-workflow)
3. [Running Tests Locally](#running-tests-locally)
4. [Submitting a Pull Request](#submitting-a-pull-request)
5. [Review and Merge Process](#review-and-merge-process)
6. [Branch Protection](#branch-protection)

---

## 🎨 Code Style and Formatting

### Python Code

- **Formatter**: We use [Black](https://black.readthedocs.io/) for Python code formatting
- **Line Length**: 88 characters (Black default)
- **Linter**: Use `pylint` or `flake8` for code quality checks
- **Type Hints**: Encouraged for function signatures

#### Running Formatters and Linters

```bash
# Format Python code with Black
black .

# Run linter
flake8 .
# or
pylint *.py
```

### Jupyter Notebooks

- Clear all outputs before committing (`Cell > All Output > Clear`)
- Use descriptive markdown cells to explain code sections
- Keep cells focused and modular

### General Guidelines

- Use meaningful variable and function names
- Write clear comments for complex logic
- Follow existing code patterns in the repository
- Keep commits atomic and focused on a single concern

---

## 🌿 Branch Naming and PR Workflow

### Branch Naming Convention

Use descriptive branch names following these patterns:

- **Feature**: `feature/short-description` or `feat/short-description`
- **Bug Fix**: `bugfix/issue-description` or `fix/issue-description`
- **Enhancement**: `enhance/what-is-enhanced`
- **Documentation**: `docs/what-docs-updated`
- **Refactor**: `refactor/what-refactored`

**Examples:**
- `feature/add-embedding-layer`
- `bugfix/fix-tokenization-edge-case`
- `docs/update-readme-examples`

### Workflow

1. **Fork or Clone**: Fork the repository (external contributors) or clone directly (team members)
2. **Create Branch**: Create a new branch from `main`
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature-name
   ```
3. **Make Changes**: Implement your changes following the code style guidelines
4. **Commit**: Write clear, descriptive commit messages
   ```bash
   git add .
   git commit -m "Add tokenization unit tests"
   ```
5. **Push**: Push your branch to the remote repository
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open PR**: Create a Pull Request using the [PR template](.github/PULL_REQUEST_TEMPLATE.md)

---

## 🧪 Running Tests Locally

Before submitting a pull request, ensure all tests pass locally.

### Python Scripts

```bash
# If pytest is available
pytest

# If unittest is used
python -m unittest discover

# Run specific test file
python test_tokenization.py
```

### Jupyter Notebooks

- Run all cells from top to bottom (`Kernel > Restart & Run All`)
- Verify outputs are correct and no errors occur
- Clear outputs before committing

### Manual Testing

- Test your changes with various inputs
- Check edge cases (empty strings, special characters, etc.)
- Verify documentation examples work as described

---

## 📤 Submitting a Pull Request

### PR Checklist

When submitting a pull request, use our [PR template](.github/PULL_REQUEST_TEMPLATE.md) and ensure:

- [ ] Code follows the style guidelines
- [ ] Code has been formatted (Black for Python)
- [ ] Linters pass without errors
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated (README, docstrings, etc.)
- [ ] Jupyter notebook outputs cleared (if applicable)
- [ ] Commit messages are clear and descriptive
- [ ] PR is linked to related issue(s)
- [ ] [FEATURE_UPDATES.md](FEATURE_UPDATES.md) updated with changes (if user-facing)

### PR Title Format

Use clear, imperative titles:
- ✅ "Add embedding layer implementation"
- ✅ "Fix tokenization bug with special characters"
- ✅ "Update README with installation instructions"
- ❌ "updated stuff"
- ❌ "fixes"

### PR Description

- Explain **what** changed and **why**
- Reference related issues: `Fixes #123` or `Relates to #456`
- Include screenshots for UI/visual changes
- List breaking changes (if any)
- Mention if documentation needs updates

---

## 👀 Review and Merge Process

### How Maintainers Review

1. **Automated Checks**: CI/CD workflows run automatically
2. **Code Review**: At least one maintainer reviews the code
3. **Testing**: Maintainers may test changes locally
4. **Feedback**: Reviewers provide constructive feedback via PR comments
5. **Approval**: Once approved, the PR is merged by a maintainer

### Timeline

- **Initial Review**: Within 3-5 business days
- **Follow-up**: Typically 1-2 days for subsequent reviews
- **Merge**: After approval and all checks pass

### Addressing Feedback

- Respond to review comments
- Make requested changes in new commits (don't force-push)
- Re-request review after making changes
- Resolve conversations once addressed

---

## 🔒 Branch Protection

The `main` branch is protected to ensure code quality and stability.

### Protected Branch Rules

- **Required Reviews**: At least 1 approving review required
- **Status Checks**: CI/CD checks must pass before merging
- **Linear History**: Merge commits or squash merging preferred
- **No Direct Pushes**: All changes must go through pull requests

### Requesting Exceptions

In rare cases, you may need an exception to branch protection rules (e.g., urgent hotfix, administrative changes).

**How to Request:**
1. Open an issue explaining the need for an exception
2. Tag repository administrators
3. Provide justification and impact assessment

**Who Can Grant Exceptions:**
- Repository administrators (see [docs/BRANCH_PROTECTION.md](docs/BRANCH_PROTECTION.md))

For detailed information on branch protection settings and how to configure them, see [docs/BRANCH_PROTECTION.md](docs/BRANCH_PROTECTION.md).

---

## 🙏 Thank You

Thank you for contributing to the LLM project! Your efforts help make this resource better for everyone learning about Large Language Models.

If you have questions or need help, feel free to:
- Open an issue for discussion
- Reach out to maintainers
- Join our community discussions

Happy coding! 🚀
