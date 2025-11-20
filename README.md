# Python Project Template

[![PyPI version](https://badge.fury.io/py/python-project-template.svg)](https://badge.fury.io/py/python-project-template)
[![Python Support](https://img.shields.io/pypi/pyversions/python-project-template.svg)](https://pypi.org/project/python-project-template/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/yourusername/python-project-template/workflows/Tests/badge.svg)](https://github.com/yourusername/python-project-template/actions)

A well-structured Python project template with best practices, comprehensive testing, CI/CD, and documentation. Use this as a starting point for your Python projects.

## ✨ Features

- 🏗️ **Clean Architecture**: Well-organized package structure
- 🧪 **Comprehensive Testing**: Full test suite with pytest, mocking, and coverage
- 🚀 **CI/CD Ready**: GitHub Actions workflows for testing, linting, and publishing
- 📦 **Easy Distribution**: Ready for PyPI publishing with setuptools_scm
- 🔒 **Security Scanning**: Automated vulnerability scanning and secret detection
- 📝 **Full Documentation**: Installation, usage, contributing, and development guides
- 🎯 **Type Hints**: Full type annotations for better IDE support
- ⚡ **Modern Python**: Supports Python 3.8+

## 📚 Documentation

- **[Installation Guide](INSTALL.md)** - How to install and configure the project
- **[Usage Guide](USAGE.md)** - Comprehensive usage examples and API reference
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project
- **[Development Guide](DEVELOPMENT.md)** - Development setup and testing

## 🚀 Quick Start

### Installation

```bash
pip install python-project-template
```

For development:

```bash
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template
pip install -e .
pip install -r requirements.txt
```

[Full installation instructions →](INSTALL.md)

### Simple Example

```python
from myproject import HelloWorld

# Create a greeter
greeter = HelloWorld(name="Alice")
print(greeter.greet())  # Output: Hello, Alice!

# Greet multiple people
names = ["Bob", "Charlie", "Diana"]
for greeting in greeter.greet_multiple(names):
    print(greeting)
```

### Using the HTTP Client

```python
from myproject import Client

# Create a client
with Client(base_url="https://api.example.com") as client:
    # Make a GET request
    data = client.get("/endpoint")
    print(data)
    
    # Make a POST request
    response = client.post("/create", json={"key": "value"})
    print(response)
```

[More examples and detailed usage →](USAGE.md)

## 🏗️ Project Structure

```
python-project-template/
├── myproject/              # Main package
│   ├── __init__.py        # Package initialization
│   ├── core.py            # Core functionality
│   ├── client.py          # HTTP client
│   ├── exceptions.py      # Custom exceptions
│   └── utils.py           # Utility functions
├── tests/                  # Test suite
│   ├── conftest.py        # Test configuration
│   ├── test_core.py       # Core tests
│   ├── test_client.py     # Client tests
│   └── test_*.py          # Other test modules
├── .github/workflows/      # CI/CD workflows
│   ├── tests.yml          # Testing workflow
│   ├── publish-to-pypi.yml # PyPI publishing
│   └── security.yml       # Security scanning
├── docs/                   # Documentation (optional)
├── pyproject.toml         # Project configuration
├── setup.py               # Setup script
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## 🧪 Running Tests

```bash
# Run all tests
./run_tests.sh

# Run only unit tests (fast)
./run_tests.sh unit

# Run with coverage report
./run_tests.sh coverage

# Run specific test file
./run_tests.sh tests/test_core.py
```

Or use pytest directly:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=myproject --cov-report=html

# Run specific markers
pytest -m unit        # Only unit tests
pytest -m integration # Only integration tests
```

## 🔧 Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements.txt
```

### Code Quality

```bash
# Format code
black myproject/ tests/

# Lint code
ruff check myproject/ tests/

# Type checking
mypy myproject/
```

[Full development guide →](DEVELOPMENT.md)

## 📦 Publishing

This template is set up for easy publishing to PyPI:

1. Tag a release: `git tag v1.0.0 && git push --tags`
2. Create a GitHub release
3. GitHub Actions will automatically build and publish to PyPI

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed publishing instructions.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass: `./run_tests.sh`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to your fork: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This template is based on best practices from:
- [Python Packaging Guide](https://packaging.python.org/)
- [pytest documentation](https://docs.pytest.org/)
- Real-world Python projects

## 📞 Support

- 📫 Issues: [GitHub Issues](https://github.com/yourusername/python-project-template/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/python-project-template/discussions)
- 📖 Documentation: [Full Documentation](https://github.com/yourusername/python-project-template/blob/main/README.md)

## 🗺️ Roadmap

- [ ] Add more comprehensive examples
- [ ] Add CLI support
- [ ] Add async client support
- [ ] Add more utility functions
- [ ] Improve documentation

---

**Note**: Remember to replace `yourusername` with your actual GitHub username and update the project name throughout all files when using this template.