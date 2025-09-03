# Payslip Generator Kit

This kit empowers contributors to generate branded payslips with audit-friendly formatting and export options. Includes diagnostics, alerting templates, and CI workflows for seamless integration.

## 🔧 Folder Structure
- `/onboarding`: Setup guides and audit checklists
- `/diagnostics`: Validation scripts and fallback loggers
- `/scripts`: Core payslip generation and formatting
- `/alerts`: Slack alert templates
- `/.github/workflows`: CI pipeline for export testing

## 🚀 Quick Start
1. Clone repo and navigate to `payslip-generator-kit`
2. Run `setup-guide.md` for environment prep
3. Test currency format with `validate-currency-format.ps1`
4. Generate sample payslip via `generate-payslip.py`
5. Export to PDF and validate output
