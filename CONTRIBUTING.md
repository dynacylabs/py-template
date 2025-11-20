# Contributing to Python Project Template

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Code Quality Standards](#code-quality-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background or experience level.

### Expected Behavior

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Be patient with questions and discussions
- Respect differing viewpoints and experiences

### Unacceptable Behavior

- Harassment or discrimination of any kind
- Trolling, insulting, or derogatory comments
- Publishing others' private information
- Any conduct inappropriate for a professional setting

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.8 or higher installed
- Git installed and configured
- A GitHub account
- Familiarity with pytest for testing

### First-Time Contributors

If this is your first contribution:

1. **Find an Issue**: Look for issues labeled `good first issue` or `help wanted`
2. **Ask Questions**: Don't hesitate to ask for clarification in the issue comments
3. **Small Changes**: Start with small, manageable changes
4. **Read the Docs**: Familiarize yourself with the [Usage Guide](USAGE.md) and [Development Guide](DEVELOPMENT.md)

## Development Setup

See the [Development Guide](DEVELOPMENT.md) for detailed setup instructions.

Quick setup:

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

# Run tests to verify setup
./run_tests.sh unit
```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Fixes**: Fix issues reported in the issue tracker
- **New Features**: Add new functionality
- **Documentation**: Improve docs, add examples, fix typos
- **Tests**: Add test coverage, improve test quality
- **Performance**: Optimize code for better performance
- **Refactoring**: Improve code structure and readability

### Reporting Bugs

When reporting bugs, include:

- **Clear Title**: Descriptive summary of the issue
- **Description**: Detailed explanation of the problem
- **Steps to Reproduce**: Exact steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: Python version, OS, package version
- **Code Sample**: Minimal code to reproduce the issue

Example bug report:

```markdown
**Title**: Client.get() fails with timeout error

**Description**: When making a GET request with a custom timeout, the client raises an unexpected error.

**Steps to Reproduce**:
1. Create a client: `client = Client(timeout=5)`
2. Make a request: `client.get("https://httpbin.org/delay/10")`
3. Error occurs

**Expected**: Should timeout gracefully after 5 seconds
**Actual**: Raises AttributeError

**Environment**: Python 3.11, macOS, package version 1.0.0

**Code Sample**:
\```python
from myproject import Client
client = Client(timeout=5)
client.get("https://httpbin.org/delay/10")
\```
```

### Suggesting Features

When suggesting new features:

1. **Check Existing Issues**: Search for similar feature requests
2. **Describe the Feature**: Clearly explain what you want
3. **Use Cases**: Provide real-world use cases
4. **Alternatives**: Mention alternatives you've considered
5. **Implementation Ideas**: Optional but helpful

### Making Changes

1. **Fork the Repository**

```bash
# Fork via GitHub UI, then clone
git clone https://github.com/YOUR-USERNAME/python-project-template.git
cd python-project-template
```

2. **Create a Branch**

```bash
# Create a descriptive branch name
git checkout -b feature/add-async-client
# or
git checkout -b fix/timeout-error
```

3. **Make Your Changes**

- Write clean, readable code
- Follow the style guide
- Add or update tests
- Update documentation

4. **Test Your Changes**

```bash
# Run all tests
./run_tests.sh

# Run specific tests
pytest tests/test_client.py -v

# Check coverage
./run_tests.sh coverage
```

5. **Commit Your Changes**

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add async support to Client class"
```

Follow commit message conventions:
- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Fix bug" not "Fixes bug"
- Keep first line under 50 characters
- Reference issues: "Fix timeout error (#123)"

6. **Push to Your Fork**

```bash
git push origin feature/add-async-client
```

7. **Open a Pull Request**

- Go to your fork on GitHub
- Click "Pull Request"
- Fill in the PR template
- Link related issues

## Code Quality Standards

### Code Style

We use several tools to maintain code quality:

```bash
# Format code with Black
black myproject/ tests/

# Lint with Ruff
ruff check myproject/ tests/

# Type check with MyPy
mypy myproject/
```

### Code Review Checklist

Before submitting, ensure:

- [ ] Code follows Python conventions (PEP 8)
- [ ] All tests pass
- [ ] New code has tests
- [ ] Documentation is updated
- [ ] No linting errors
- [ ] Type hints are used where appropriate
- [ ] Docstrings are added for public APIs
- [ ] Changes are backward compatible (or migration guide provided)

## Testing Requirements

### Writing Tests

- All new features must include tests
- Bug fixes should include regression tests
- Tests should be clear and well-documented
- Use descriptive test names

Example test:

```python
import pytest
from myproject import HelloWorld

@pytest.mark.unit
class TestHelloWorld:
    """Test the HelloWorld class."""
    
    def test_greet_with_custom_name(self):
        """Test that greeting uses the provided name."""
        hw = HelloWorld(name="Alice")
        result = hw.greet()
        assert result == "Hello, Alice!"
```

### Running Tests

```bash
# All tests
./run_tests.sh

# Unit tests only
./run_tests.sh unit

# With coverage
./run_tests.sh coverage

# Specific file
pytest tests/test_client.py -v
```

### Test Coverage

- Aim for 90%+ code coverage
- 100% coverage for new features
- Tests should be meaningful, not just for coverage

Check coverage:

```bash
./run_tests.sh coverage
# Then open htmlcov/index.html
```

## Pull Request Process

1. **Update Documentation**: Ensure all docs are updated
2. **Add Tests**: Include comprehensive tests
3. **Update Changelog**: Add entry to CHANGELOG.md (if exists)
4. **Follow Template**: Fill out the PR template completely
5. **Request Review**: Tag maintainers for review
6. **Address Feedback**: Respond to review comments promptly
7. **Keep Updated**: Rebase on main if needed

### PR Title Format

- `feat: Add async client support`
- `fix: Resolve timeout error in Client.get()`
- `docs: Update installation instructions`
- `test: Add tests for edge cases`
- `refactor: Simplify error handling`

### PR Description Template

```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes
- List of changes made
- Breaking changes (if any)

## Testing
How was this tested?

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests pass
- [ ] No linting errors
```

## Style Guide

### Python Style

- Follow PEP 8
- Use Black for formatting (line length: 100)
- Use type hints for function signatures
- Write docstrings for public APIs (Google style)

### Example

```python
def greet_user(name: str, greeting: str = "Hello") -> str:
    """
    Generate a greeting message for a user.
    
    Args:
        name: The name of the user to greet.
        greeting: The greeting to use. Defaults to "Hello".
    
    Returns:
        A formatted greeting string.
    
    Example:
        >>> greet_user("Alice")
        'Hello, Alice!'
        >>> greet_user("Bob", greeting="Hi")
        'Hi, Bob!'
    """
    return f"{greeting}, {name}!"
```

## Documentation

### Updating Documentation

When making changes:

1. Update relevant `.md` files
2. Update docstrings
3. Add examples if needed
4. Update README if API changes

### Documentation Standards

- Use clear, simple language
- Include code examples
- Keep examples up to date
- Use proper Markdown formatting

## Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and discussions
- **Pull Requests**: For code contributions

### Recognition

Contributors are recognized in:
- GitHub contributors list
- Release notes
- Project documentation

## Questions?

If you have questions about contributing:

1. Check existing issues and discussions
2. Read the documentation
3. Ask in GitHub Discussions
4. Contact maintainers

Thank you for contributing! 🎉
