input_name = input("Enter Employee Name: ")
input_id = input("Enter Employee ID: ")
input_salary = float(input("Enter Employee Salary: "))  
input_allowance = float(input("Enter Employee Allowance: "))
input_bonus_percent = float(input("Enter Employee Bonus Percentage: ")) 

gross_monthly_sal = input_salary + input_allowance
annual_gross_sal = gross_monthly_sal * 12 + (input_bonus_percent/100 * (gross_monthly_sal * 12))

print(f"\n%-40s : {input_name}" % "Employee Name")
print(f"%-40s : {input_id}" % "Employee ID")
print(f"%-40s : {input_salary}" % "Employee Salary")
print(f"%-40s : {input_allowance}" % "Employee Allowance")
print(f"%-40s : {input_bonus_percent}" % "Employee Bonus Percentage")
print(f"%-40s : {gross_monthly_sal}" % "Gross Monthly Salary")
print(f"%-40s : {annual_gross_sal}" % "Annual Gross Salary")


