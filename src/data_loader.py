from pathlib import Path
import pandas as pd


def load_loan_data():
    """
    Load the loan dataset from the project's data directory.
    """

    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "raw" / "loan_data.csv"

    return pd.read_csv(data_path)
