
# 🏥 Health Insurance Purchase Prediction

This project predicts whether a customer is likely to buy health insurance based on several demographic and behavioral factors. It uses a machine learning model trained on relevant customer data to assist in decision-making for insurance sales.

---

## 📌 Project Overview

The goal is to develop a prediction system that takes user input (via command line or Jupyter Notebook), displays the input in tabular form, and predicts the likelihood of the customer purchasing health insurance.

---

## 🔍 Features

- User-friendly input collection
- Displays entered data as a formatted DataFrame
- Loads a trained `.pkl` (pickle) machine learning model
- Outputs a clear prediction: ✅ Likely to buy / ❌ Not likely to buy

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn (for model training)
- Pickle (for model serialization)
- Jupyter Notebook (for interactive UI)

---

## 📥 Input Parameters

| Feature               | Type   | Description                                      |
|-----------------------|--------|--------------------------------------------------|
| Gender                | int    | 1 = Male, 0 = Female                             |
| Age                   | int    | Age of the customer                              |
| Driving_License       | int    | 1 = Has license, 0 = No license                  |
| Region_Code           | float  | Region code of the customer                     |
| Previously_Insured    | int    | 1 = Previously insured, 0 = Not insured          |
| Vehicle_Age           | int    | 0 = < 1 year, 1 = 1–2 years, 2 = > 2 years       |
| Vehicle_Damage        | int    | 1 = Damaged before, 0 = No damage                |
| Annual_Premium        | float  | Premium in rupees                                |
| Policy_Sales_Channel  | float  | Channel code for sales                           |
| Vintage               | float  | Days customer has been associated with company   |

---

## 🚀 How to Run

1. Open the Jupyter Notebook or Python file:
   - `health_insurance_predict.ipynb` for interactive mode.
   - `main.py` if you're running from terminal.

2. Ensure the model file `model.pkl` is in the same directory.

3. Run the notebook or script:
   - Enter user inputs as prompted.
   - View your data and prediction output.

---

## 📊 Sample Output

```
Enter Gender ['Male':1, 'Female':0]: 1
Enter Age: 23
...
Gender  Age  Driving_License  ...  Vintage
1       23   1                ...  231.0

Response: The customer is NOT likely to buy health insurance. ❌
```

---

## 📁 File Structure

```
📦health-insurance-predictor/
├── model.pkl
├── health_insurance_predict.ipynb
├── main.py
└── README.md
```
---
## 👤 Author

**Akash Nikam**
Mail: akashnikam803@gmail.com
