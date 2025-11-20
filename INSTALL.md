# Installation Guide

This guide covers how to install the Python Project Template.

## Table of Contents

- [Requirements](#requirements)
- [Installation Methods](#installation-methods)
  - [From PyPI (Recommended)](#from-pypi-recommended)
  - [From Source](#from-source)
  - [Development Installation](#development-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version recommended
- **Dependencies**: 
  - `requests >= 2.28.0`

## Installation Methods

### From PyPI (Recommended)

The easiest way to install the library is from PyPI using pip:

```bash
pip install python-project-template
```

To upgrade to the latest version:

```bash
pip install --upgrade python-project-template
```

To install a specific version:

```bash
pip install python-project-template==1.0.0
```

### From Source

To install directly from the GitHub repository:

```bash
# Clone the repository
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template

# Install
pip install .
```

Or install directly from GitHub without cloning:

```bash
pip install git+https://github.com/yourusername/python-project-template.git
```

### Development Installation

For development, install in editable mode with all dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt
```

This allows you to make changes to the code and see them reflected immediately without reinstalling.

### Optional Dependencies

If you need development tools:

```bash
pip install python-project-template[dev]
```

This includes:
- pytest and plugins for testing
- black for code formatting
- ruff for linting
- mypy for type checking
- coverage tools

## Verification

After installation, verify it's working correctly:

### Command Line Verification

```bash
python -c "import myproject; print(myproject.__version__)"
```

### Python Script Verification

Create a file `test_install.py`:

```python
from myproject import HelloWorld

# Test basic functionality
hw = HelloWorld(name="Test")
result = hw.greet()
print(result)

if result == "Hello, Test!":
    print("✓ Installation successful!")
else:
    print("✗ Installation failed!")
```

Run it:

```bash
python test_install.py
```

### Run Tests

If you installed from source:

```bash
# Run the test suite
./run_tests.sh unit

# Or use pytest directly
pytest tests/ -v
```

## Troubleshooting

### Common Issues

#### Import Error: No module named 'myproject'

**Solution**: Make sure you've installed the package:
```bash
pip install python-project-template
# or for development:
pip install -e .
```

#### Permission Denied Error

**Solution**: Use `--user` flag or a virtual environment:
```bash
pip install --user python-project-template
```

Or create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install python-project-template
```

#### Old Version Installed

**Solution**: Force reinstall:
```bash
pip install --upgrade --force-reinstall python-project-template
```

#### Dependency Conflicts

**Solution**: Use a fresh virtual environment:
```bash
python -m venv fresh_env
source fresh_env/bin/activate
pip install python-project-template
```

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/yourusername/python-project-template/issues) for similar problems
2. Search the [Discussions](https://github.com/yourusername/python-project-template/discussions)
3. Create a new issue with:
   - Your Python version (`python --version`)
   - Your pip version (`pip --version`)
   - Your operating system
   - The full error message
   - Steps to reproduce the issue

## Next Steps

- Read the [Usage Guide](USAGE.md) to learn how to use the library
- Check the [Development Guide](DEVELOPMENT.md) for contributing
- Review the [API documentation](USAGE.md#api-reference)
