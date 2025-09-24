import uuid
from datetime import datetime
from typing import Optional


class Payslip:
    def __init__(self,
        employee: dict,
        period: str,
        gross_pay: float,
        deductions: float,
        net_pay: float,
        payment: Optional[dict] = None,
        is_demo: bool = True,
        created_by: str = "system"
    ):
        self.employee = employee  # {"name": "John Doe", "employee_id": "E123"}
        self.period = period
        self.gross_pay = gross_pay
        self.deductions = deductions
        self.net_pay = net_pay

        # --- Payment Section (demo-safe) ---
        if payment is None:
            payment = {}

        self.payment = {
            "payment_method": payment.get("payment_method", "bank"),  # bank, wallet, paypal, etc.
            "masked_account": self._mask_account(payment.get("account_number")),
            "bank_name": payment.get("bank_name", "Demo Bank"),
            "payment_status": payment.get("payment_status", "demo"),  # demo | pending | confirmed
        }

        # --- Demo flag + audit trail ---
        self.is_demo = is_demo
        self.verification_token = str(uuid.uuid4())
        self.created_by = created_by
        self.created_at_utc = datetime.utcnow().isoformat()

    def _mask_account(self, account_number: Optional[str]) -> str:
        if not account_number:
            return "****0000"
        return "****" + account_number[-4:]

    def to_dict(self) -> dict:
        return {
            "employee": self.employee,
            "period": self.period,
            "gross_pay": self.gross_pay,
            "deductions": self.deductions,
            "net_pay": self.net_pay,
            "payment": self.payment,
            "is_demo": self.is_demo,
            "verification_token": self.verification_token,
            "created_by": self.created_by,
            "created_at_utc": self.created_at_utc,
        }