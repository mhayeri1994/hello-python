#!/usr/bin/env python3
def find_s(fp: str) -> tuple:
    """find-s or find specified hypothesis, developed by Tom Mitchel

    Args:
        fp (str): CSV file path of data.

    Returns:
        float: The tuple of hypothesis

    Raises:
        ValueError: if `arr` is empty.
    """
    import pandas as pd

    df = pd.read_csv(fp)
    h = [set() for _ in range(df.shape[1] - 1)]
    for i in df.values:
        if i[-1] == "yes":
            for i, v in enumerate(i[:-1]):
                if not v in h[i]:
                    h[i].add(v)
    for i in range(df.shape[1] - 1):
        if h[i] == set(df.iloc[:, i].unique()):
            h[i] = "?"
    return h


if __name__ == "__main__":
    print(find_s("faces.csv"))
