# Lab 5 — Reflection

**1. What is static code analysis?**

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities and coding-style problems.

**2. What is the difference between Pylint, Bandit and Flake8?**

Pylint checks code quality and potential programming errors. Bandit identifies common security issues. Flake8 checks Python style and formatting.

**3. How did static analysis help improve the parking permit manager?**

The tools identified issues such as mutable default arguments, unsafe exception handling, weak random number generation and formatting violations. Fixing them improved code quality, security and maintainability.

**4. What are the limitations of static analysis?**

Static analysis cannot detect every logical error or runtime problem. The program must also be executed and tested with valid and invalid inputs.
