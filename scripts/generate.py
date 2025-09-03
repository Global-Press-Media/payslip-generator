payment_method = request.form['payment_method']
pdf.cell(200, 10, txt=f"Payment Method: {payment_method}", ln=True)
