#  Employee Attrition 

This project performs insightful data analysis on an HR dataset using **Python Pandas**. It helps HR teams identify trends related to employee attrition, satisfaction, salary distribution, and potential at-risk employees.



## Dataset

- Source: Kaggle  
- File: `WA_Fn-UseC_-HR-Employee-Attrition.csv`  
- [ Kaggle Dataset Link](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)


## Key Insights

###  1. Department & Gender Stats
- Extracts unique values of **departments** and **genders**.

###  2. Attrition Count
- Shows how many employees have **left** or **stayed**.

###  3. Average Salary Analysis
- **By Department**
- **By Gender**

###  4. Job Satisfaction vs Attrition
- Compares average job satisfaction of employees who stayed vs. those who left.

###  5. At-Risk Employees
- Identifies employees with:
  - **Low salary** (< ₹35,000)
  - **Low job satisfaction** (≤ 2)


##  Tools Used

- Python 
- Pandas 
- Google Colab



##  How to Run

1. Upload the dataset to your Colab or Jupyter environment.
2. Run the analysis script (code in `main.py` or in a notebook).
3. Review the printed outputs for insights.

---

##  Sample Code Output

```python
# Sample:
Attrition Count:
No     1233
Yes     237
Name: Attrition, dtype: int64

Avg Salary by Department:
Department
Human Resources             6739.529412
Research & Development    7675.951286
Sales                     7422.415385
