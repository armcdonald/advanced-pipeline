# GitHub Marketplace CI/CD Demo

This project demonstrates how to use **GitHub Marketplace Actions** in a CI/CD pipeline.

## What is GitHub Marketplace?

GitHub Marketplace is a central hub where developers can find and share **Actions** — reusable automation components for GitHub workflows. Instead of writing all your CI/CD logic from scratch, you can use pre-built, tested actions.

## Marketplace Actions Used in This Project

| Action | Marketplace Link | Purpose |
|--------|------------------|---------|
| `actions/checkout` | [Checkout](https://github.com/marketplace/actions/checkout) | Clone your repository into the runner |
| `actions/setup-python` | [Setup Python](https://github.com/marketplace/actions/setup-python) | Install Python and configure caching |
| `codecov/codecov-action` | [Codecov](https://github.com/marketplace/actions/codecov) | Upload test coverage reports |
| `actions/upload-artifact` | [Upload Artifact](https://github.com/marketplace/actions/upload-a-build-artifact) | Save build outputs between jobs |
| `actions/download-artifact` | [Download Artifact](https://github.com/marketplace/actions/download-artifact) | Retrieve artifacts from previous jobs |
| `softprops/action-gh-release` | [GH Release](https://github.com/marketplace/actions/gh-release) | Automatically create GitHub releases |

## Project Structure

```
github-ci-demo/
├── .github/
│   └── workflows/
│       └── ci.yml          # The CI/CD pipeline config
├── src/
│   └── text_analyzer.py    # Python module
├── tests/
│   └── test_text_analyzer.py # Unit tests
├── pyproject.toml
└── README.md
```

## 🚀 The CI/CD Pipeline

The workflow in `.github/workflows/ci.yml` runs these jobs:

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│  LINT   │────▶│  TEST   │────▶│ BUILD   │────▶│ RELEASE │
│         │     │(matrix) │     │         │     │(on tag) │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
                     │
                ┌────┴────┐
           ┌────┴───┐  ┌──┴────┐
           │Py 3.12 │  │Py 3.13│  ...
           └────────┘  └───────┘
```

### Job Breakdown

1. **Lint** - Checks code formatting (Black, isort, flake8)
2. **Test** - Runs pytest on Python 3.12, 3.13, 3.14 (matrix strategy)
3. **Security** - Scans for vulnerabilities with Bandit
4. **Build** - Creates distributable package
5. **Release** - Creates GitHub release when you push a tag

## Running Locally

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
python tests/test_text_analyzer.py

# Run linters
black src/ tests/
flake8 src/ tests/
```

## 📌 How to Use Marketplace Actions

In your workflow YAML, reference an action with `uses`:

```yaml
steps:
  # Format: owner/repo@version
  - uses: actions/checkout@v6
  
  # With configuration options
  - uses: actions/setup-python@v7
    with:
      python-version: "3.11"
      cache: "pip"
```

### Finding Actions

1. Go to [github.com/marketplace](https://github.com/marketplace?type=actions)
2. Filter by "Actions"
3. Search for what you need (e.g., "python", "docker", "deploy")
4. Check the action's README for usage instructions

## 🏷️ Creating a Release

To trigger the release job:

```bash
git tag -a v1.0.0
git push origin v1.0.0
```

This will:
1. Run the full pipeline
2. Build the package
3. Create a GitHub Release with the artifacts attached
