import pandas as pd


def calculate_expected_loss(
    model,
    features,
    customer_id,
    credit_lines_outstanding,
    loan_amt_outstanding,
    total_debt_outstanding,
    income,
    years_employed,
    fico_score,
    recovery_rate=0.10,
):
    """
    Calculate Probability of Default (PD) and Expected Loss (EL)
    for a single borrower.
    """

    input_dict = {
        "customer_id": [customer_id],
        "credit_lines_outstanding": [credit_lines_outstanding],
        "loan_amt_outstanding": [loan_amt_outstanding],
        "total_debt_outstanding": [total_debt_outstanding],
        "income": [income],
        "years_employed": [years_employed],
        "fico_score": [fico_score],
    }

    input_data = pd.DataFrame(input_dict)

    input_data = input_data[features]

    pd_value = model.predict_proba(input_data)[0, 1]

    lgd = 1 - recovery_rate
    ead = loan_amt_outstanding

    expected_loss = pd_value * lgd * ead

    return {
        "probability_of_default": round(pd_value, 4),
        "expected_loss": round(expected_loss, 2),
    }