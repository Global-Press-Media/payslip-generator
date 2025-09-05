# GitHub Copilot Instructions

This repository is a **Payslip Generator** project.

## General Guidelines
- Always use **Python 3.9+**.
- Prefer clear, modular functions over long scripts.
- Add docstrings and inline comments for all functions.
- Ensure code follows **PEP8 style guidelines**.

## Features to Support
- Generate payslips from employee data (name, salary, deductions, allowances).
- Export payslips in **PDF and Excel formats**.
- Support bulk employee data input via CSV.
- Provide error handling for invalid or missing fields.

## Testing
- Write **unit tests** using `pytest`.
- Ensure functions are tested for edge cases (e.g., zero salary, negative deductions).
- Aim for at least **80% code coverage**.

## Security & Data
- Avoid hardcoding sensitive information.
- Use environment variables for configs (e.g., DB credentials, API keys).

## Documentation
- Update the README.md when new features are added.
- Provide usage examples with sample input/output.
