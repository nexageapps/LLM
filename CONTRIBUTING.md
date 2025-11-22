# Contributing to LLM

Thank you for your interest in contributing to this project! We welcome contributions from the community and appreciate your help in making this repository better.

## Table of Contents

- [Code Style & Formatting](#code-style--formatting)
- [Branch Naming & PR Workflow](#branch-naming--pr-workflow)
- [Running Tests Locally](#running-tests-locally)
- [Submitting a Pull Request Checklist](#submitting-a-pull-request-checklist)
- [Review & Merge Process](#review--merge-process)
- [Branch Protection & Exceptions](#branch-protection--exceptions)
- [Security Disclosure](#security-disclosure)

---

## Code Style & Formatting

### Python Code
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Format code with `black` and lint with `flake8` or `pylint`

### Jupyter Notebooks
- Clear output before committing notebooks (to reduce diff noise)
- Use markdown cells to explain concepts
- Keep cells focused and modular
- Test notebooks end-to-end before committing

### General Guidelines
- Write clear, concise commit messages
- Keep commits atomic and focused on a single change
- Comment code where necessary to explain complex logic

---

## Branch Naming & PR Workflow

### Branch Naming Convention

Use descriptive branch names with the following prefixes:

- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `chore/` - Maintenance tasks (dependencies, configs, etc.)
- `refactor/` - Code refactoring without behavior changes
- `test/` - Test additions or updates

**Examples:**
- `feature/add-embeddings-lesson`
- `fix/tokenization-edge-case`
- `docs/update-readme-instructions`

### PR Workflow

1. **Fork and Clone**: Fork the repository and clone it locally
2. **Create a Branch**: Create a new branch from `main` using the naming convention above
3. **Make Changes**: Implement your changes, following code style guidelines
4. **Test Locally**: Run tests and verify your changes work as expected
5. **Commit**: Write clear commit messages describing your changes
6. **Push**: Push your branch to your fork
7. **Open a PR**: Open a pull request against the `main` branch
8. **Address Feedback**: Respond to review comments and make requested changes
9. **Merge**: Once approved, a maintainer will merge your PR

---

## Running Tests Locally

### Prerequisites
- Python 3.8 or higher
- Required dependencies (if any)

### Running Python Scripts
```bash
# Run lesson scripts
python lesson1_tokenization.py

# Run any test scripts (if present)
python -m pytest tests/
```

### Testing Jupyter Notebooks
```bash
# Install jupyter if not already installed
pip install jupyter

# Run notebooks manually or use nbconvert to execute
jupyter nbconvert --to notebook --execute LLM_|_Basic_|_L1.ipynb
```

### Validation Checklist
- [ ] All scripts run without errors
- [ ] Notebooks execute completely from top to bottom
- [ ] Code follows style guidelines
- [ ] Documentation is clear and accurate

---

## Submitting a Pull Request Checklist

Before submitting your PR, ensure you've completed the following:

- [ ] Code follows the style guidelines in [Code Style & Formatting](#code-style--formatting)
- [ ] Branch name follows the [Branch Naming Convention](#branch-naming-convention)
- [ ] Changes have been tested locally
- [ ] Commit messages are clear and descriptive
- [ ] Documentation has been updated (if applicable)
- [ ] Changelog entry added to `FEATURE_UPDATES.md` under "Unreleased" section
- [ ] No merge conflicts with the `main` branch
- [ ] All checks and tests pass (once CI is configured)
- [ ] PR description clearly explains the changes and motivation
- [ ] Related issues are linked in the PR description

**For Feature PRs:**
- [ ] Examples or usage instructions have been added
- [ ] New dependencies are justified and documented

**For Bug Fix PRs:**
- [ ] Root cause is explained
- [ ] Test case added to prevent regression (if applicable)

---

## Review & Merge Process

### Review Timeline
- Initial review: typically within 2-3 business days
- Follow-up reviews: 1-2 business days after updates

### Review Criteria
Reviewers will evaluate:
- **Correctness**: Does the code work as intended?
- **Style**: Does it follow the project's coding standards?
- **Testing**: Are changes adequately tested?
- **Documentation**: Is it clear and complete?
- **Impact**: Does it introduce breaking changes or risks?

### Approval & Merge
- At least one maintainer approval is required
- All checks must pass before merging
- Maintainers will merge using "Squash and Merge" for clean history (unless otherwise specified)
- After merge, the feature branch will be deleted

---

## Branch Protection & Exceptions

The `main` branch is protected to maintain code quality and stability. See [docs/BRANCH_PROTECTION.md](docs/BRANCH_PROTECTION.md) for detailed protection settings and rationale.

### Protected Branch Rules
- Direct pushes to `main` are not allowed
- All changes must go through pull requests
- At least one approving review is required
- Status checks must pass before merging
- Force pushes and deletions are prohibited

### Requesting an Exception
In rare cases (e.g., critical hotfixes, security patches), exceptions may be granted:

1. Open an issue explaining the urgency
2. Tag a maintainer for expedited review
3. For security issues, follow the [Security Disclosure](#security-disclosure) process
4. Maintainers may bypass protection rules if justified

---

## Security Disclosure

If you discover a security vulnerability, please do **not** open a public issue. Instead:

1. **Email the maintainer** directly at the contact information provided in the repository
2. Provide a detailed description of the vulnerability
3. Include steps to reproduce (if applicable)
4. Suggest a fix or mitigation (if you have one)

We take security seriously and will respond promptly to verified reports. Once the issue is resolved, we'll publicly acknowledge your contribution (unless you prefer to remain anonymous).

---

## Questions?

If you have questions about contributing, feel free to:
- Open a [Discussion](https://github.com/nexageapps/LLM/discussions) (if enabled)
- Open an issue with the `question` label
- Reach out to the repository maintainer

Thank you for contributing to the LLM project! 🎉
