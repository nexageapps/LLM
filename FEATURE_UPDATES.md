# Feature Updates & Changelog

This document tracks notable changes, new features, and updates to the LLM project. All user-facing changes should be documented here.

---

## Format

Each entry should include:
- **Version/Date**: When the change was made
- **Type**: Feature, Fix, Enhancement, Documentation, etc.
- **Description**: What changed and why
- **Author**: Who made the change (optional)

---

## [Unreleased]

### Added
- Contributing guidelines (CONTRIBUTING.md)
- Pull request template
- Issue templates for bug reports and feature requests
- Code of Conduct (Contributor Covenant v2.1)
- Branch protection documentation
- GitHub Sponsors support

### Changed
- Updated README with sponsor badges and contribution flow

---

## [2024-11-22] - Initial Release

### Added
- **Lesson 1**: Tokenization, Vocabulary, Encoding & Decoding
  - Download and process text files
  - Regex-based tokenization
  - Vocabulary building with token-to-ID mapping
  - Encode text to token IDs
  - Decode token IDs back to text
- Initial README with project overview
- Jupyter notebooks: `LLM_|_Basic_|_L1.ipynb` and `LLM_|_Basic_|_L2.ipynb`

### Reference
- Based on concepts from *Build a Large Language Model* by Sebastian Raschka
- Uses only Python standard library (no external dependencies for core functionality)

---

## How to Update This File

When submitting a pull request with user-facing changes:

1. Add your changes under the `[Unreleased]` section
2. Use the appropriate category: Added, Changed, Fixed, Removed, Deprecated, Security
3. Write clear, user-friendly descriptions
4. Link to issues or PRs if relevant

Example:
```markdown
### Added
- New embedding layer with configurable dimensions (#123)

### Fixed
- Tokenization now correctly handles Unicode characters (#145)
```

---

## Categories

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes or improvements
