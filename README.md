# Credit Risk Modeling

A machine learning project for estimating borrower credit risk through **Probability of Default (PD)**, **Expected Loss (EL)**, and **FICO score quantization**.

This project is based on the **JPMorgan Chase & Co. Quantitative Research Virtual Experience (Job Simulation)** and has been refactored into a production-style repository with modular code organization, reusable components, and a clean project structure for portfolio purposes.

---

## Project Overview

Credit risk assessment is a fundamental process in banking and financial institutions. Before issuing a loan, lenders must estimate the likelihood that a borrower will default and quantify the potential financial loss.

This project demonstrates an end-to-end credit risk modeling workflow, including:

- Probability of Default (PD) estimation
- Expected Loss (EL) calculation
- FICO score quantization into credit rating buckets
- Modular Python implementation
- Reusable project architecture

In addition to solving the business problem, the repository emphasizes software engineering best practices such as modular code, reusable utilities, version control, and repository organization.

---

## Business Problem

Financial institutions need reliable methods to evaluate borrower risk before approving loans. Estimating the probability of default and expected financial loss enables lenders to make better lending decisions, manage portfolio risk, and satisfy regulatory requirements.

This project develops a simple credit risk framework using supervised machine learning and credit score segmentation techniques.

---

## Project Objectives

- Estimate Probability of Default (PD) using Logistic Regression
- Calculate Expected Loss (EL)
- Quantize FICO scores into credit rating categories
- Organize reusable project modules
- Demonstrate an end-to-end machine learning workflow

---

## Repository Structure

```text
credit-risk-modeling/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_probability_of_default.ipynb
│   └── 02_fico_quantization.ipynb
│
├── reports/
│   └── figures/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── risk.py
│   └── __init__.py
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Methodology

### Task 3 — Probability of Default

- Data preprocessing
- Feature selection
- Logistic Regression model
- Probability of Default prediction
- Expected Loss calculation

### Task 4 — Credit Rating Quantization

- FICO score preprocessing
- Dynamic Programming optimization
- Log-Likelihood maximization
- Credit rating generation
- Bucket performance evaluation

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

## Key Features

- Modular project structure
- Reusable data loader
- Configurable dataset location
- Expected Loss calculation module
- Clean repository organization
- Reproducible notebooks
- Portfolio-oriented implementation

---

## Dataset

The original dataset used for this project is intentionally **not included** in this repository.

Datasets are stored locally outside the repository to:

- protect data ownership
- keep the repository lightweight
- simplify version control
- follow common software engineering practices

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Aryaprwira-peps/credit-risk-modeling.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Configure the dataset location in:

```text
src/config.py
```

Then open the notebooks inside the `notebooks/` directory.

---

## Project Status

**Status:** ✅ Completed

Implemented features:

- Probability of Default estimation
- Expected Loss calculation
- FICO score quantization
- Modular project structure
- External dataset configuration
- Reusable Python modules

---

## Future Improvements

Potential future enhancements include:

- Gradient Boosting models
- XGBoost comparison
- Cross-validation
- Hyperparameter optimization
- Model explainability (SHAP)

---

## Acknowledgements

This project is based on the **JPMorgan Chase & Co. Quantitative Research Virtual Experience (Job Simulation)**.

The implementation has been independently refactored and extended with improved project organization, reusable modules, documentation, and repository structure for educational and portfolio purposes.