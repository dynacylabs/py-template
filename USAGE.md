# Usage Guide

This guide provides comprehensive examples for using the Python Project Template.

## Table of Contents

- [Quick Start](#quick-start)
- [Core Functionality](#core-functionality)
- [HTTP Client](#http-client)
- [Utilities](#utilities)
- [Error Handling](#error-handling)
- [Advanced Usage](#advanced-usage)
- [API Reference](#api-reference)

## Quick Start

### Basic Hello World Example

The simplest way to use the library:

```python
from myproject import HelloWorld

# Create a greeter
greeter = HelloWorld(name="Alice")
print(greeter.greet())  # Output: Hello, Alice!
```

### Custom Greeting

```python
from myproject import HelloWorld

# Custom greeting
greeter = HelloWorld(name="Bob", greeting="Hi")
print(greeter.greet())  # Output: Hi, Bob!

# Change the greeting dynamically
greeter.set_greeting("Howdy")
print(greeter.greet())  # Output: Howdy, Bob!
```

## Core Functionality

### HelloWorld Class

The `HelloWorld` class provides simple greeting functionality.

#### Creating an Instance

```python
from myproject import HelloWorld

# Default greeting
hw = HelloWorld()
print(hw.greet())  # Hello, World!

# Custom name
hw = HelloWorld(name="Alice")
print(hw.greet())  # Hello, Alice!

# Custom greeting and name
hw = HelloWorld(name="Bob", greeting="Hey")
print(hw.greet())  # Hey, Bob!
```

#### Greeting Multiple Names

```python
from myproject import HelloWorld

hw = HelloWorld(greeting="Welcome")
names = ["Alice", "Bob", "Charlie"]

greetings = hw.greet_multiple(names)
for greeting in greetings:
    print(greeting)

# Output:
# Welcome, Alice!
# Welcome, Bob!
# Welcome, Charlie!
```

#### Updating Greetings

```python
from myproject import HelloWorld

hw = HelloWorld(name="Alice")

# Change the name
hw.set_name("Bob")
print(hw.greet())  # Hello, Bob!

# Change the greeting
hw.set_greeting("Hi")
print(hw.greet())  # Hi, Bob!
```

### Mathematical Functions

Simple utility functions for basic operations:

```python
from myproject.core import add_numbers, multiply_numbers

# Addition
result = add_numbers(5, 3)
print(result)  # 8.0

# Multiplication
result = multiply_numbers(4, 2.5)
print(result)  # 10.0

# Works with negative numbers
result = add_numbers(-5, 3)
print(result)  # -2.0
```

## HTTP Client

### Basic GET Requests

```python
from myproject import Client

# Create a client
client = Client(base_url="https://api.example.com")

# Make a GET request
try:
    data = client.get("/users")
    print(data)
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
```

### Using Context Manager

The recommended way to use the client:

```python
from myproject import Client

with Client(base_url="https://api.example.com") as client:
    # Make requests
    users = client.get("/users")
    print(users)
    
    # Client automatically closes when exiting the context
```

### GET Requests with Parameters

```python
from myproject import Client

with Client(base_url="https://api.example.com") as client:
    # Add query parameters
    params = {
        "page": 1,
        "limit": 10,
        "sort": "name"
    }
    
    data = client.get("/users", params=params)
    print(data)
```

### POST Requests

```python
from myproject import Client

with Client(base_url="https://api.example.com") as client:
    # Send JSON data
    new_user = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 30
    }
    
    response = client.post("/users", json=new_user)
    print(f"Created user with ID: {response['id']}")
```

### Custom Headers and Timeout

```python
from myproject import Client

# Custom headers
headers = {
    "Authorization": "Bearer your-token-here",
    "X-Custom-Header": "custom-value"
}

# Create client with custom configuration
client = Client(
    base_url="https://api.example.com",
    timeout=60,
    headers=headers
)

# Use the client
try:
    data = client.get("/protected-resource")
    print(data)
finally:
    client.close()
```

## Utilities

### Email Validation

```python
from myproject.utils import validate_email

# Validate email addresses
emails = [
    "user@example.com",
    "invalid-email",
    "test@domain.co.uk"
]

for email in emails:
    if validate_email(email):
        print(f"✓ {email} is valid")
    else:
        print(f"✗ {email} is invalid")
```

### Dictionary Formatting

```python
from myproject.utils import format_dict

# Format a dictionary for display
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

formatted = format_dict(data)
print(formatted)
# Output:
# name: Alice
# age: 30
# city: New York
```

### List Chunking

```python
from myproject.utils import chunk_list

# Split a large list into chunks
items = list(range(1, 11))  # [1, 2, 3, ..., 10]
chunks = chunk_list(items, chunk_size=3)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}")

# Output:
# Chunk 1: [1, 2, 3]
# Chunk 2: [4, 5, 6]
# Chunk 3: [7, 8, 9]
# Chunk 4: [10]
```

## Error Handling

### Handling Client Errors

```python
from myproject import Client
from myproject.exceptions import NetworkError, NotFoundError

with Client(base_url="https://api.example.com") as client:
    try:
        data = client.get("/users/999")
    except NotFoundError:
        print("User not found!")
    except NetworkError as e:
        print(f"Network error: {e}")
```

### Custom Exception Hierarchy

```python
from myproject.exceptions import (
    ProjectError,
    ConfigurationError,
    ValidationError
)

def process_config(config):
    if not config:
        raise ConfigurationError("Configuration is empty")
    
    if "api_key" not in config:
        raise ValidationError("Missing required field: api_key")
    
    # Process configuration...
    pass

# Usage
try:
    process_config({})
except ConfigurationError as e:
    print(f"Configuration error: {e}")
except ValidationError as e:
    print(f"Validation error: {e}")
except ProjectError as e:
    # Catches all project-related errors
    print(f"Project error: {e}")
```

## Advanced Usage

### Combining Multiple Features

```python
from myproject import HelloWorld, Client
from myproject.utils import chunk_list

# Fetch users from API and greet them
with Client(base_url="https://api.example.com") as client:
    # Fetch users
    users = client.get("/users")
    
    # Extract names
    names = [user["name"] for user in users]
    
    # Process in chunks to avoid overwhelming the system
    chunks = chunk_list(names, chunk_size=10)
    
    # Greet each chunk
    greeter = HelloWorld(greeting="Welcome")
    for chunk in chunks:
        greetings = greeter.greet_multiple(chunk)
        for greeting in greetings:
            print(greeting)
```

### Building a Simple Application

```python
from myproject import HelloWorld, Client
from myproject.exceptions import NetworkError, NotFoundError

class UserGreeter:
    """Fetch users from API and greet them."""
    
    def __init__(self, api_base_url: str):
        self.client = Client(base_url=api_base_url)
        self.greeter = HelloWorld(greeting="Hello")
    
    def greet_user(self, user_id: int) -> str:
        """Fetch a user and generate a greeting."""
        try:
            user = self.client.get(f"/users/{user_id}")
            self.greeter.set_name(user["name"])
            return self.greeter.greet()
        except NotFoundError:
            return f"User {user_id} not found"
        except NetworkError as e:
            return f"Failed to fetch user: {e}"
    
    def close(self):
        """Close the client."""
        self.client.close()

# Usage
app = UserGreeter("https://api.example.com")
try:
    print(app.greet_user(1))
    print(app.greet_user(2))
finally:
    app.close()
```

## API Reference

### HelloWorld Class

**Constructor**: `HelloWorld(name: str = "World", greeting: str = "Hello")`

**Methods**:
- `greet() -> str`: Returns a greeting message
- `greet_multiple(names: list[str]) -> list[str]`: Greet multiple names
- `set_greeting(greeting: str) -> None`: Update the greeting
- `set_name(name: str) -> None`: Update the name

### Client Class

**Constructor**: `Client(base_url: str = "", timeout: int = 30, headers: Optional[Dict[str, str]] = None)`

**Methods**:
- `get(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`: Make a GET request
- `post(endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`: Make a POST request
- `close() -> None`: Close the session

**Context Manager**: Supports `with` statement for automatic cleanup

### Utility Functions

- `add_numbers(a: float, b: float) -> float`: Add two numbers
- `multiply_numbers(a: float, b: float) -> float`: Multiply two numbers
- `format_dict(data: Dict[str, Any], indent: int = 2) -> str`: Format a dictionary
- `validate_email(email: str) -> bool`: Validate an email address
- `chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]`: Split a list into chunks

### Exceptions

- `ProjectError`: Base exception for all project errors
- `ConfigurationError`: Configuration-related errors
- `ValidationError`: Validation failures
- `NetworkError`: Network operation failures
- `NotFoundError`: Resource not found (404)

## Best Practices

1. **Use Context Managers**: Always use `with` statement for the Client
2. **Handle Exceptions**: Catch and handle specific exceptions appropriately
3. **Type Hints**: The library uses type hints - leverage them in your IDE
4. **Close Resources**: Always close clients when done (or use context managers)
5. **Validate Input**: Use utility functions to validate data before processing

## Examples Repository

For more examples, check the `examples/` directory in the repository or visit the [examples documentation](https://github.com/yourusername/python-project-template/tree/main/examples).
