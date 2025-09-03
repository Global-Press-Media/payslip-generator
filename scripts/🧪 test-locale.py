import locale
import datetime
import json

# Define test locales and expected formats
locales = {
    "en_US": {"currency": "$", "date_format": "%m-%d-%Y"},
    "en_GB": {"currency": "£", "date_format": "%d/%m/%Y"},
    "fr_FR": {"currency": "€", "date_format": "%d/%m/%Y"},
    "ng_NG": {"currency": "₦", "date_format": "%d-%m-%Y"}
}

def validate_locale(locale_code, expected):
    try:
        locale.setlocale(locale.LC_ALL, locale_code)
        currency_symbol = locale.localeconv()["currency_symbol"]
        formatted_date = datetime.datetime.now().strftime(expected["date_format"])
        
        result = {
            "locale": locale_code,
            "currency_match": currency_symbol == expected["currency"],
            "date_format": formatted_date,
            "status": "✅ Passed" if currency_symbol == expected["currency"] else "❌ Failed"
        }
    except Exception as e:
        result = {
            "locale": locale_code,
            "error": str(e),
            "status": "❌ Error"
        }
    return result

# Run validations
results = [validate_locale(code, config) for code, config in locales.items()]

# Log results
with open("diagnostics/locale-errors.log", "w") as log_file:
    for entry in results:
        log_file.write(json.dumps(entry) + "\n")

# Print summary
for entry in results:
    print(f"{entry['locale']}: {entry['status']}")
