import pandas as pd

TRAIN_PATH = "data/Gen_AI Dataset.xlsx"
TEST_PATH = "data/Gen_AI Dataset.xlsx"

def load_train_data():
    """
    Load labeled train-set (Query + Assessment_url).
    Returns a dictionary: {query: set(urls)}
    """
    df = pd.read_excel(TRAIN_PATH, sheet_name="Train-Set")

    gold = {}
    for _, row in df.iterrows():
        q = row["Query"].strip()
        url = row["Assessment_url"].strip()
        gold.setdefault(q, set()).add(url)

    return gold


def load_test_data():
    """
    Load test-set queries (unlabeled).
    Returns a list of queries.
    """
    df = pd.read_excel(TEST_PATH, sheet_name="Test-Set")
    return df["Query"].dropna().tolist()
