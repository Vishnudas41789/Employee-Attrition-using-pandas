import pandas as pd


data = pd.read_csv('/content/WA_Fn-UseC_-HR-Employee-Attrition.csv')
data


print(" Sample Data:\n", data.head())

print("\nDepartments:", data['Department'].unique())

print(" Genders:", data['Gender'].unique())
attrition_count = data['Attrition'].value_counts()


print("\n Attrition Count:\n", attrition_count)

avg_salary = data.groupby('Department')['MonthlyIncome'].mean()
print("\n Avg Salary by Department:\n", avg_salary)

avg_salary_gender = data.groupby('Gender')['MonthlyIncome'].mean()
print("\n Avg Salary by Gender:\n", avg_salary_gender)

satisfaction_vs_attr = data.groupby('Attrition')['JobSatisfaction'].mean()
print("\n Avg Job Satisfaction vs Attrition:\n", satisfaction_vs_attr)

at_risk = data[(data['MonthlyIncome'] < 35000) & (data['JobSatisfaction'] <= 2)]
print("\n At-Risk Employees:\n", at_risk[['EmployeeNumber', 'MonthlyIncome', 'JobSatisfaction']])