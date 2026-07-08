from pathlib import Path
import pandas as pd

from src.config import DATASETS_ROOT


def load_loan_data():
    data_path = DATASETS_ROOT / "credit-risk" / "loan_data.csv"

    print("DEBUG data_path :", data_path)
    print("DEBUG exists    :", data_path.exists())

    return pd.read_csv(data_path)