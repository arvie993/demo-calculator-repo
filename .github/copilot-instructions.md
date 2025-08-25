# Demo Calculator Repository - GitHub Copilot Instructions

**ALWAYS follow these instructions first and fallback to additional search and context gathering only if the information here is incomplete or found to be in error.**

## Project Overview

Demo Calculator Repository is a simple Python calculator library providing basic arithmetic operations and advanced scientific functions. It uses only Python standard library (no external dependencies) and consists of 4 main Python modules plus documentation.

## Working Effectively

### Prerequisites and Setup
- Ensure Python 3.x is installed: `python3 --version`
- No additional installation required - uses Python standard library only
- All operations complete in under 1 second

### Repository Structure
Navigate the codebase using this structure:
```
demo-calculator-repo/
├── README.md          # Project documentation and usage examples
├── add.py            # Addition function (CONTAINS BUG - see Known Issues)
├── divide.py         # Division function with zero-division handling
├── subtraction.py    # Subtraction function supporting multiple arguments
├── scientific.py     # Advanced mathematical functions
└── .gitignore        # Standard Python gitignore
```

### Key Module Locations
- **Basic arithmetic**: `add.py`, `divide.py`, `subtraction.py`
- **Scientific functions**: `scientific.py` (trigonometric, logarithmic, exponential, square root)
- **Documentation**: `README.md` contains complete API reference and examples
- **Configuration**: `.gitignore` for Python cache files and IDE settings

## Validation and Testing

### CRITICAL: Always run this comprehensive validation after making changes
Execute this complete functionality test (takes <1 second):

```bash
python3 -c "
import math
from add import addition
from divide import divide_numbers  
from subtraction import subtraction
from scientific import sin, cos, tan, log, exp, sqrt, power, log10, log2

print('=== VALIDATION TEST ===')
print('Basic arithmetic:')
print(f'addition(10, 5): {addition(10, 5)}  # BUG: returns 5 instead of 15')
print(f'divide_numbers(10, 2): {divide_numbers(10, 2)}  # Expected: 5.0')
print(f'divide_numbers(10, 0): {divide_numbers(10, 0)}  # Expected: Error message')
print(f'subtraction(10, 3, 2): {subtraction(10, 3, 2)}  # Expected: 5')

print('Scientific functions:')
print(f'sin(π/2): {sin(math.pi/2)}  # Expected: 1.0')
print(f'cos(0): {cos(0)}  # Expected: 1.0') 
print(f'sqrt(16): {sqrt(16)}  # Expected: 4.0')
print(f'log(math.e): {log(math.e)}  # Expected: 1.0')
print(f'exp(1): {exp(1)}  # Expected: ~2.718')
print('=== VALIDATION COMPLETE ===')
"
```

### File Compilation Check
Always verify Python syntax is correct:
```bash
python3 -m py_compile *.py && echo "All files compile successfully"
```

### Import Pattern Testing
Test the documented import patterns work correctly:
```bash
python3 -c "from add import addition; print('Import test passed')"
python3 -c "from scientific import sin, cos, sqrt; print('Scientific imports passed')"
```

## Known Issues and Workarounds

### CRITICAL BUG in add.py
- **Issue**: `addition(a, b)` function returns `a - b` instead of `a + b`
- **Location**: Line 2 in `add.py`
- **Current code**: `return a - b`  
- **Expected**: `return a + b`
- **Workaround**: Use `subtraction(a, -b)` for actual addition, or fix the implementation
- **Testing**: `addition(10, 5)` returns `5` but should return `15`

## Build and Test Process

### No Build System Required
- This is a pure Python library with no build process
- No `setup.py`, `requirements.txt`, or external dependencies
- All modules use only Python standard library

### Linting and Code Quality
- No formal linting setup in repository
- Use manual code review and Python compilation check
- All current files pass `python3 -m py_compile` validation

### Manual Testing Scenarios
Always test these scenarios after making changes:

1. **Basic arithmetic operations**:
   ```bash
   python3 -c "from divide import divide_numbers; print(divide_numbers(20, 4))"
   python3 -c "from subtraction import subtraction; print(subtraction(15, 3, 2))"
   ```

2. **Scientific function accuracy**:
   ```bash
   python3 -c "from scientific import sin, cos; import math; print(sin(math.pi/2), cos(0))"
   ```

3. **Error handling**:
   ```bash
   python3 -c "from divide import divide_numbers; print(divide_numbers(5, 0))"
   python3 -c "from subtraction import subtraction; print(subtraction(5))"
   ```

4. **Command-line usage patterns**:
   ```bash
   python3 -c "from add import addition; print('Result:', addition(10, 3))"
   ```

## Common Development Tasks

### Adding New Functions
- Place basic arithmetic in respective module files (`add.py`, `divide.py`, `subtraction.py`)
- Place advanced math functions in `scientific.py`
- Update `README.md` with documentation and examples
- Always test with the validation commands above

### Modifying Existing Functions
- **CRITICAL**: Always run full validation test after changes
- Check that import patterns in README still work
- Verify mathematical accuracy with known values
- Test edge cases (zero division, invalid inputs)

### Documentation Updates
- Main documentation in `README.md`
- Follow existing format: function signature, parameters, returns, example
- Include both import usage and command-line testing examples

## Timing Expectations

- **All operations**: Complete in <1 second
- **Full validation test**: ~0.02 seconds
- **File compilation check**: ~0.1 seconds  
- **NEVER CANCEL**: No long-running operations exist in this repository

## Repository Navigation Tips

### Frequently Accessed Files
1. **README.md** - Complete API documentation and examples
2. **scientific.py** - Most comprehensive module with mathematical functions  
3. **add.py** - First check for the known bug when debugging arithmetic issues

### Quick Reference Commands
```bash
# View all Python files
ls *.py

# Check file structure matches expected layout
ls -la

# Quick function test
python3 -c "from scientific import sqrt; print(sqrt(25))"

# View function signatures
grep -n "^def " *.py
```

## Integration and CI Considerations

### No Automated CI
- Repository has no `.github/workflows` or CI setup
- Manual validation required before commits
- Use the validation commands above as your testing suite

### Code Style
- Follow existing simple function style in modules
- Include docstrings for new functions (see `scientific.py` examples)
- Handle errors appropriately (see `divide.py` zero-division example)

---

**Remember: Always reference these instructions first. Run the comprehensive validation test after any changes. The repository is simple but the add.py bug is critical to be aware of when working with arithmetic operations.**