"""
Visual Project Structure for Python Project Template
"""

PROJECT_STRUCTURE = """
python-project-template/
│
├── 📦 PACKAGE (myproject/)
│   ├── __init__.py          # Package initialization, version, exports
│   ├── core.py              # HelloWorld example & math functions
│   ├── client.py            # HTTP client with error handling
│   ├── exceptions.py        # Custom exception hierarchy
│   └── utils.py             # Utility functions (email, dict, list)
│
├── 🧪 TESTS (tests/)
│   ├── __init__.py          # Test package init
│   ├── conftest.py          # Shared fixtures & configuration
│   ├── test_core.py         # Core functionality tests (15+ tests)
│   ├── test_client.py       # HTTP client tests (mocked)
│   ├── test_utils.py        # Utility function tests
│   ├── test_exceptions.py   # Exception tests
│   ├── test_integration.py  # Integration test examples
│   └── test_init.py         # Package initialization tests
│
├── 🔄 CI/CD (.github/workflows/)
│   ├── tests.yml            # Multi-version testing (Python 3.8-3.12)
│   ├── publish-to-pypi.yml  # Automated PyPI publishing
│   ├── security.yml         # Security scanning (4 tools)
│   └── dependency-updates.yml # Dependency monitoring
│
├── 📚 DOCUMENTATION
│   ├── README.md            # Main project overview
│   ├── INSTALL.md           # Installation guide
│   ├── USAGE.md             # API documentation & examples
│   ├── CONTRIBUTING.md      # Contribution guidelines
│   ├── DEVELOPMENT.md       # Development workflow
│   ├── TEMPLATE_SETUP.md    # How to use this template
│   ├── QUICKREF.md          # Quick reference card
│   └── TEMPLATE_SUMMARY.md  # This file
│
├── ⚙️ CONFIGURATION
│   ├── pyproject.toml       # Modern Python config (PEP 621)
│   ├── setup.py             # Traditional setup (compatibility)
│   ├── pytest.ini           # pytest configuration & markers
│   ├── requirements.txt     # Development dependencies
│   ├── MANIFEST.in          # Package manifest
│   ├── .gitignore           # Git ignore patterns
│   └── LICENSE              # MIT License
│
├── 🛠️ SCRIPTS
│   └── run_tests.sh         # Test runner (unit/integration/coverage)
│
└── 📁 REFERENCE (can be removed)
    ├── haveibeenpwned-py/   # Reference implementation
    └── lastpass-py/         # Reference implementation

"""

FEATURES = """
🎯 KEY FEATURES
================

✅ Testing
   • 90%+ code coverage requirement
   • Unit, integration, and slow test markers
   • Mocked HTTP requests with responses
   • Coverage reporting (HTML & terminal)
   • 50+ example tests

✅ Code Quality
   • Black (code formatting, 100 char lines)
   • Ruff (fast linting)
   • MyPy (static type checking)
   • Type hints throughout
   • Google-style docstrings

✅ CI/CD
   • Multi-version testing (Python 3.8-3.12)
   • Automated PyPI publishing
   • Security scanning (Bandit, Safety, CodeQL, TruffleHog)
   • Dependency monitoring
   • Codecov integration

✅ Documentation
   • 7 comprehensive documentation files
   • Code examples throughout
   • API reference
   • Setup guides

✅ Developer Experience
   • Simple test runner script
   • Clear project structure
   • Example code with real functionality
   • Context manager support
   • Comprehensive error handling

"""

USAGE_EXAMPLES = """
📝 USAGE EXAMPLES
==================

1. HelloWorld Example:
   from myproject import HelloWorld
   
   greeter = HelloWorld(name="Alice")
   print(greeter.greet())  # "Hello, Alice!"

2. HTTP Client:
   from myproject import Client
   
   with Client(base_url="https://api.example.com") as client:
       data = client.get("/endpoint")

3. Utilities:
   from myproject.utils import validate_email, chunk_list
   
   if validate_email("user@example.com"):
       print("Valid email!")
   
   chunks = chunk_list([1,2,3,4,5], chunk_size=2)

"""

TEST_COMMANDS = """
🧪 TEST COMMANDS
================

./run_tests.sh              # All tests
./run_tests.sh unit         # Unit tests only (fast)
./run_tests.sh integration  # Integration tests
./run_tests.sh coverage     # With HTML coverage report
./run_tests.sh tests/test_core.py  # Specific file

pytest                      # All tests (direct)
pytest -v                   # Verbose output
pytest -m unit             # Only unit tests
pytest -m "not slow"       # Exclude slow tests
pytest --cov=myproject     # With coverage

"""

WORKFLOW_TRIGGERS = """
⚡ GITHUB ACTIONS WORKFLOWS
============================

tests.yml:
  • Push to main
  • Pull requests
  • Daily at 2am UTC
  • Manual trigger
  → Runs on Python 3.8, 3.9, 3.10, 3.11, 3.12

security.yml:
  • Weekly (Mondays at 3am UTC)
  • Push to main
  • Pull requests
  • Manual trigger
  → Scans with 4 different tools

dependency-updates.yml:
  • Weekly (Mondays at 9am UTC)
  • Manual trigger
  → Creates issues for vulnerabilities

publish-to-pypi.yml:
  • GitHub releases only
  → Automatic versioning and publishing

"""

CUSTOMIZATION = """
🔧 CUSTOMIZATION CHECKLIST
===========================

Required Changes:
  ☐ Rename myproject/ to yourpackage/
  ☐ Update pyproject.toml metadata
  ☐ Update setup.py metadata
  ☐ Update README.md (title, URLs, examples)
  ☐ Update all documentation files
  ☐ Update pytest.ini (--cov=yourpackage)
  ☐ Update workflow files (package name)
  ☐ Update LICENSE (year, name)

Optional Changes:
  ☐ Remove HTTP client if not needed
  ☐ Replace HelloWorld example with your code
  ☐ Add/remove dependencies
  ☐ Customize test markers
  ☐ Adjust coverage threshold
  ☐ Modify workflow schedules

Cleanup:
  ☐ Remove haveibeenpwned-py/ directory
  ☐ Remove lastpass-py/ directory
  ☐ Remove TEMPLATE_*.md files (optional)

"""

DEPENDENCIES = """
📦 DEPENDENCIES
===============

Core (Runtime):
  • requests>=2.28.0        # HTTP library

Development:
  • pytest>=7.0.0           # Testing framework
  • pytest-cov>=4.0.0       # Coverage plugin
  • pytest-mock>=3.10.0     # Mocking plugin
  • responses>=0.22.0       # HTTP mocking
  • coverage>=7.0.0         # Coverage tool
  • black>=22.0.0           # Code formatter
  • ruff>=0.1.0             # Fast linter
  • mypy>=0.950             # Type checker

"""

METRICS = """
📊 PROJECT METRICS
==================

Code:
  • Python files: 12
  • Test files: 7
  • Test cases: 50+
  • Lines of code: ~2,000
  • Coverage target: 90%+

Documentation:
  • Documentation files: 10
  • Total doc lines: ~2,500
  • Code examples: 30+

CI/CD:
  • Workflows: 4
  • Python versions tested: 5
  • Security tools: 4
  • Automated checks: 15+

"""

if __name__ == "__main__":
    print(PROJECT_STRUCTURE)
    print(FEATURES)
    print(USAGE_EXAMPLES)
    print(TEST_COMMANDS)
    print(WORKFLOW_TRIGGERS)
    print(CUSTOMIZATION)
    print(DEPENDENCIES)
    print(METRICS)
