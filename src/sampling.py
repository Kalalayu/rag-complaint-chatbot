import pandas as pd

def stratified_sample(
    df: pd.DataFrame,
    group_col: str,
    n_samples: int,
    random_state: int = 42
) -> pd.DataFrame:
    """
    Perform proportional stratified sampling.
    """
    if group_col not in df.columns:
        raise ValueError(f"Column '{group_col}' not found in dataframe")

    sampled_df = (
        df.groupby(group_col, group_keys=False)
        .apply(
            lambda x: x.sample(
                max(1, int(len(x) / len(df) * n_samples)),
                random_state=random_state
            )
        )
    )

    return sampled_df.sample(frac=1, random_state=random_state).reset_index(drop=True)
