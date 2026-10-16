principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate: "))
time = int(input("Enter loan period in years: "))

monthly_rate = rate / (12 * 100)
months = time * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("Monthly EMI:", emi)