# Contributing to Demo Calculator Repository

Thank you for your interest in contributing to the Demo Calculator Repository! We welcome contributions from the community and are grateful for your support.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Questions?](#questions)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How Can I Contribute?

### Reporting Bugs

If you find a bug in the calculator functions, please create an issue with the following information:

- **Clear title**: Use a descriptive title for the issue
- **Description**: Describe the bug and what you expected to happen
- **Steps to reproduce**: Provide step-by-step instructions to reproduce the issue
- **Code samples**: Include any relevant code snippets
- **Python version**: Specify which version of Python you're using

Example:
```
Title: Division by zero returns string instead of raising exception
Description: When calling divide_numbers(5, 0), it returns an error message string instead of raising a ZeroDivisionError
Steps to reproduce:
1. Import divide_numbers from divide.py
2. Call divide_numbers(5, 0)
3. Observe the result
Python version: 3.9.7
```

### Suggesting Enhancements

We welcome suggestions for new features or improvements! When suggesting enhancements:

- **Check existing issues**: Make sure the enhancement hasn't already been suggested
- **Provide clear use cases**: Explain why this enhancement would be useful
- **Be specific**: Include examples of how the feature would work

Potential areas for enhancement:
- Additional mathematical operations (modulo, factorial, etc.)
- Support for complex numbers
- Calculator history/memory functions
- Input validation improvements
- Performance optimizations

### Pull Requests

We actively welcome your pull requests! Follow these steps:

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** for any new functionality
4. **Ensure all tests pass** before submitting
5. **Update documentation** if you're adding new features
6. **Submit your pull request** with a clear description

## Development Setup

### Prerequisites

- Python 3.x installed on your system
- Git for version control

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/arvie993/demo-calculator-repo.git
   cd demo-calculator-repo
   ```

2. No additional dependencies are required! This project uses only standard Python libraries.

3. Verify your setup by running the tests:
   ```bash
   python3 -m unittest discover -s tests -v
   ```

## Coding Standards

Please follow these guidelines when contributing code:

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Keep functions focused on a single responsibility
- Add docstrings for all functions

### Function Structure

Example of a well-structured function:

```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Parameters:
    - param1 (type): Description of param1
    - param2 (type): Description of param2
    
    Returns:
    - type: Description of return value
    """
    # Implementation
    result = param1 + param2
    return result
```

### File Organization

- Each mathematical operation should be in its own file
- Related functions can be grouped together (e.g., all trigonometric functions in `scientific.py`)
- Keep files focused and manageable in size

## Testing Guidelines

All contributions must include appropriate tests.

### Writing Tests

- Use Python's `unittest` framework
- Place test files in the `tests/` directory
- Name test files as `test_<module_name>.py`
- Each test class should inherit from `unittest.TestCase`
- Use descriptive test method names starting with `test_`

### Test Structure Example

```python
import unittest
from your_module import your_function


class TestYourFunction(unittest.TestCase):
    def test_basic_functionality(self):
        """Test basic use case"""
        result = your_function(2, 3)
        self.assertEqual(result, 5)
    
    def test_edge_case(self):
        """Test edge case like zero or negative numbers"""
        result = your_function(0, 5)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
```

### Running Tests

Run all tests:
```bash
python3 -m unittest discover -s tests -v
```

Run a specific test file:
```bash
python3 -m unittest tests.test_add
```

### Test Coverage

- Test typical use cases
- Test edge cases (zero, negative numbers, very large numbers)
- Test error conditions (invalid input types, domain errors)
- Aim for comprehensive coverage of your code

## Commit Message Guidelines

Write clear and meaningful commit messages:

### Format

```
Short summary (50 characters or less)

Detailed explanation if necessary (wrap at 72 characters).
Explain what and why, not how.

- Bullet points are okay
- Use present tense ("Add feature" not "Added feature")
```

### Examples of Good Commit Messages

- `Add factorial function to scientific module`
- `Fix division by zero error handling`
- `Update README with new scientific functions`
- `Add tests for logarithm edge cases`

### Examples of Poor Commit Messages

- `fix bug` (too vague)
- `updated stuff` (not descriptive)
- `WIP` (work in progress should not be committed to main)

## Documentation

When adding new functions, please update:

1. **README.md**: Add documentation for the new function including:
   - Function signature
   - Parameter descriptions
   - Return value description
   - Usage examples

2. **Code comments**: Add docstrings to your functions

3. **Examples**: Provide practical examples of how to use the function

## Review Process

Once you submit a pull request:

1. Maintainers will review your code
2. You may be asked to make changes
3. Once approved, your PR will be merged
4. Your contribution will be credited

Please be patient during the review process. We aim to review all PRs within a few days.

## Questions?

If you have questions about contributing:

- Open an issue with the label "question"
- Check existing issues and pull requests for similar questions
- Review the README.md for project documentation

## Recognition

All contributors will be recognized for their contributions. Thank you for helping make this project better!

---

*Happy Contributing! 🧮*
