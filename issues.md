# Lab 5 — Static Code Analysis Issue Log

| Issue | Tool / Code | Original Line | Description | Fix Approach |
|---|---|---:|---|---|
| Weak random number generation | Bandit B311 | 11 | random.randint() generates permit numbers. | Review whether unpredictable permit numbers are required; use a secure generator if needed. |
| Silent exception handling | Bandit B110 | 22–23 | An exception is ignored using pass. | Catch and handle the expected exception explicitly. |
| Mutable default argument | Pylint W0102 | 9 | A default list may be shared between function calls. | Use None and initialize a new list inside the function. |
| Bare exception handling | Pylint W0702 / Flake8 E722 | 16, 22, 29, 43 | Exceptions are caught without specifying their types. | Catch appropriate exception types. |
| Global statement | Pylint W0603 | 40 | A function modifies a global variable. | Reduce global state where practical. |
| File handling | Pylint W1514 / R1732 | 42, 47 | File operations omit explicit encoding or context managers. | Use with open(..., encoding="utf-8"). |
| Missing documentation | Pylint C0114 / C0116 | Multiple | The module and functions lack docstrings. | Add appropriate docstrings. |
| Naming convention | Pylint C0103 | 51 | setExpiry uses camelCase. | Rename it to set_expiry and update its calls. |
| Formatting | Flake8 E302 / E305 / E501 | Multiple | Blank lines and line lengths violate style rules. | Correct spacing and split long lines. |