basic_salary = 45000
hra_percentage = 20
da_percentage = 10
bonus = 50 
tax_percentage = 10 
provident_fund_percentage = 12
hra = basic_salary * hra_percentage / 100
da = basic_salary * da_percentage / 100
gross_salary = basic_salary + hra + da + bonus
tax = gross_salary * tax_percentage / 100
provident_fund = basic_salary * provident_fund_percentage / 100
total_deductions = tax + provident_fund
net_salary = gross_salary - total_deductions
print(net_salary)

