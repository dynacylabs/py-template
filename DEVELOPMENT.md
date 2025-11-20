# Development Guide

This guide covers the development workflow, testing, and release process for the Python Project Template.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Code Coverage](#code-coverage)
- [Development Workflow](#development-workflow)
- [Release Process](#release-process)
- [Continuous Integration](#continuous-integration)
- [Debugging](#debugging)
- [Performance](#performance)

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- pip
- Virtual environment tool (venv, virtualenv, or conda)

### Initial Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template
```

2. **Create Virtual Environment**

```bash
# Using venv (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda
conda create -n myproject python=3.11
conda activate myproject
```

3. **Install Development Dependencies**

```bash
# Install package in editable mode
pip install -e .

# Install all development dependencies
pip install -r requirements.txt
```

4. **Verify Installation**

```bash
# Run tests
./run_tests.sh unit

# Check imports
python -c "from myproject import HelloWorld; print('Success!')"
```

### IDE Setup

#### VS Code

Recommended extensions:
- Python (Microsoft)
- Pylance
- Python Test Explorer
- Coverage Gutters
- GitLens

Recommended settings (`.vscode/settings.json`):

```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "black",
    "python.analysis.typeCheckingMode": "basic",
    "editor.formatOnSave": true,
    "editor.rulers": [100]
}
```

#### PyCharm

1. Mark `myproject/` as Sources Root
2. Enable pytest as test runner
3. Configure Python 3.8+ interpreter
4. Enable type checking
5. Set Black as code formatter

## Project Structure

```
python-project-template/
├── myproject/              # Main package
│   ├── __init__.py        # Package initialization & exports
│   ├── core.py            # Core functionality
│   ├── client.py          # HTTP client wrapper
│   ├── exceptions.py      # Custom exception classes
│   └── utils.py           # Utility functions
├── tests/                  # Test suite
│   ├── __init__.py        # Test package initialization
│   ├── conftest.py        # Shared fixtures and configuration
│   ├── test_core.py       # Tests for core module
│   ├── test_client.py     # Tests for client module
│   ├── test_utils.py      # Tests for utilities
│   ├── test_exceptions.py # Tests for exceptions
│   └── test_integration.py# Integration tests
├── .github/                # GitHub configuration
│   └── workflows/         # CI/CD workflows
│       ├── tests.yml      # Test automation
│       ├── publish-to-pypi.yml  # PyPI publishing
│       ├── security.yml   # Security scanning
│       └── dependency-updates.yml # Dependency checks
├── docs/                   # Documentation (optional)
├── .gitignore             # Git ignore patterns
├── LICENSE                # MIT License
├── MANIFEST.in            # Package manifest
├── README.md              # Main documentation
├── INSTALL.md             # Installation guide
├── USAGE.md               # Usage guide
├── CONTRIBUTING.md        # Contribution guidelines
├── DEVELOPMENT.md         # This file
├── pyproject.toml         # Project metadata and config
├── setup.py               # Setup script
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Development dependencies
└── run_tests.sh           # Test runner script
```

## Testing

### Running Tests

Use the provided test runner script:

```bash
# Run all tests
./run_tests.sh

# Run only unit tests (fast)
./run_tests.sh unit

# Run integration tests
./run_tests.sh integration

# Run with coverage report
./run_tests.sh coverage

# Run specific test file
./run_tests.sh tests/test_core.py

# Run specific test
./run_tests.sh tests/test_core.py::TestHelloWorld::test_greet_default
```

Or use pytest directly:

```bash
# All tests
pytest

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Run tests matching pattern
pytest -k "test_greet"

# Run tests with marker
pytest -m unit
pytest -m integration
pytest -m slow
```

### Writing Tests

Follow these guidelines:

1. **Location**: Place tests in `tests/` directory
2. **Naming**: Name test files `test_*.py`
3. **Structure**: Group related tests in classes
4. **Markers**: Use pytest markers (`@pytest.mark.unit`, etc.)
5. **Fixtures**: Use fixtures from `conftest.py`

Example test structure:

```python
import pytest
from myproject import HelloWorld

@pytest.mark.unit
class TestHelloWorld:
    """Tests for the HelloWorld class."""
    
    def test_greet_default(self, hello_world):
        """Test default greeting behavior."""
        result = hello_world.greet()
        assert result == "Hello, World!"
    
    def test_greet_custom_name(self):
        """Test greeting with custom name."""
        hw = HelloWorld(name="Alice")
        assert hw.greet() == "Hello, Alice!"
```

### Test Markers

Available markers (defined in `pytest.ini`):

- `@pytest.mark.unit`: Unit tests (fast, mocked)
- `@pytest.mark.integration`: Integration tests (may hit external services)
- `@pytest.mark.slow`: Slow-running tests

Usage:

```python
@pytest.mark.unit
def test_fast_operation():
    pass

@pytest.mark.integration
@pytest.mark.slow
def test_api_integration():
    pass
```

Run specific markers:

```bash
pytest -m unit           # Only unit tests
pytest -m "not slow"     # Exclude slow tests
pytest -m "unit and not slow"  # Unit tests, excluding slow
```

## Code Coverage

### Measuring Coverage

```bash
# Generate coverage report
./run_tests.sh coverage

# View in terminal
coverage report

# Generate HTML report
coverage html
# Open htmlcov/index.html in browser

# Generate XML report (for CI)
coverage xml
```

### Coverage Goals

- **Overall**: 90%+ coverage
- **New Code**: 100% coverage
- **Critical Paths**: 100% coverage

### Checking Coverage Locally

```bash
# Run tests with coverage
pytest --cov=myproject --cov-report=term-missing

# Fail if coverage below threshold
pytest --cov=myproject --cov-report=term --cov-fail-under=90
```

## Development Workflow

### Daily Development

1. **Pull Latest Changes**

```bash
git checkout main
git pull origin main
```

2. **Create Feature Branch**

```bash
git checkout -b feature/new-feature
```

3. **Make Changes**

- Edit code
- Add tests
- Update docs

4. **Run Tests**

```bash
./run_tests.sh
```

5. **Format and Lint**

```bash
# Format with Black
black myproject/ tests/

# Lint with Ruff
ruff check myproject/ tests/

# Type check with MyPy
mypy myproject/
```

6. **Commit Changes**

```bash
git add .
git commit -m "feat: Add new feature"
```

7. **Push and Create PR**

```bash
git push origin feature/new-feature
# Then create PR on GitHub
```

### Code Quality Tools

#### Black (Code Formatting)

```bash
# Format all code
black myproject/ tests/

# Check formatting without changing
black --check myproject/ tests/

# Format specific file
black myproject/core.py
```

Configuration in `pyproject.toml`:
```toml
[tool.black]
line-length = 100
target-version = ['py38', 'py39', 'py310', 'py311', 'py312']
```

#### Ruff (Linting)

```bash
# Lint all code
ruff check myproject/ tests/

# Auto-fix issues
ruff check --fix myproject/ tests/

# Lint specific file
ruff check myproject/core.py
```

#### MyPy (Type Checking)

```bash
# Type check package
mypy myproject/

# Strict mode
mypy --strict myproject/

# Check specific file
mypy myproject/core.py
```

## Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Creating a Release

1. **Update Version**

Version is managed by `setuptools_scm` based on git tags.

2. **Update CHANGELOG** (if exists)

Document changes in CHANGELOG.md.

3. **Create and Push Tag**

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0
```

4. **Create GitHub Release**

- Go to GitHub Releases
- Click "Draft a new release"
- Select the tag
- Fill in release notes
- Publish release

5. **Automated Publishing**

GitHub Actions will automatically:
- Run tests
- Build distribution packages
- Publish to PyPI (if configured)

### Manual Publishing to PyPI

If needed, publish manually:

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to TestPyPI (for testing)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## Continuous Integration

### GitHub Actions Workflows

#### Tests Workflow (`.github/workflows/tests.yml`)

Runs on:
- Push to main
- Pull requests
- Daily schedule (2am UTC)

Actions:
- Test on Python 3.8, 3.9, 3.10, 3.11, 3.12
- Run linting and type checking
- Generate coverage reports
- Upload to Codecov

#### Security Workflow (`.github/workflows/security.yml`)

Runs weekly and on pushes.

Scans:
- Dependency vulnerabilities (Safety)
- Code security issues (Bandit)
- Secret detection (TruffleHog)
- CodeQL analysis

#### Publish Workflow (`.github/workflows/publish-to-pypi.yml`)

Triggers on GitHub releases.

Actions:
- Build distribution packages
- Publish to PyPI using trusted publishing

### Local CI Simulation

Run the same checks locally:

```bash
# Run all tests like CI
pytest -v --cov=myproject --cov-report=term-missing

# Run linting
black --check myproject/ tests/
ruff check myproject/ tests/
mypy myproject/

# Security scan
pip install safety bandit
safety check
bandit -r myproject/
```

## Debugging

### Using pdb

```python
# Add breakpoint
import pdb; pdb.set_trace()

# Python 3.7+ breakpoint()
breakpoint()
```

### Using pytest debugger

```bash
# Drop into debugger on failure
pytest --pdb

# Drop into debugger on first failure
pytest -x --pdb
```

### Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
```

## Performance

### Profiling

```python
# Using cProfile
python -m cProfile -o profile.stats script.py

# Analyze profile
python -m pstats profile.stats
# Then: sort time, stats 10
```

### Memory Profiling

```bash
# Install memory_profiler
pip install memory_profiler

# Profile script
python -m memory_profiler script.py
```

### Benchmarking

```python
import timeit

# Time a function
time = timeit.timeit(
    'hw.greet()',
    setup='from myproject import HelloWorld; hw = HelloWorld()',
    number=10000
)
print(f"Time: {time}")
```

## Troubleshooting

### Common Issues

**Import errors after changes**:
```bash
pip install -e .
```

**Tests not found**:
```bash
# Ensure tests directory has __init__.py
# Check pytest.ini configuration
pytest --collect-only
```

**Coverage not working**:
```bash
# Reinstall in editable mode
pip uninstall python-project-template
pip install -e .
```

## Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Semantic Versioning](https://semver.org/)

## Getting Help

- Check GitHub Issues
- Read documentation
- Ask in GitHub Discussions
- Contact maintainers
