from payslip_generator.payslip import Payslip
import json

def main():
    """
    Main function to generate and display a sample payslip.
    """
    # 1. Define sample data
    employee_data = {
        "name": "John Doe",
        "employee_id": "E12345"
    }

    payment_data = {
        "payment_method": "bank",
        "account_number": "1234567890",
        "bank_name": "Global Trust Bank",
        "payment_status": "confirmed"
    }

    # 2. Create an instance of the Payslip
    payslip_instance = Payslip(
        employee=employee_data,
        period="September 2025",
        gross_pay=5000.00,
        deductions=1200.00,
        net_pay=3800.00,
        payment=payment_data,
        is_demo=False,
        created_by="xpertforextradeinc"
    )

    # 3. Get the payslip data as a dictionary
    payslip_dict = payslip_instance.to_dict()

    # 4. Print the payslip details in a readable format
    print("--- Generated Payslip ---")
    print(json.dumps(payslip_dict, indent=4))
    print("-------------------------")
    print("\nSuccessfully generated a sample payslip.")

if __name__ == "__main__":
    main()