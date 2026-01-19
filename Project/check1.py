import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load Excel file into DataFrame
    """
    df = pd.read_excel(file_path)
    return df


def filter_by_product_group(
    df: pd.DataFrame,
    product_group: str
) -> pd.DataFrame:
    """
    Filter data by product group.
    Includes 'Both' automatically.
    """

    product_group = product_group.capitalize()

    if product_group not in ['Loans', 'Deposits', 'Both']:
        raise ValueError("PRODUCT_GROUP must be Loans, Deposits, or Both")

    if product_group == 'Both':
        return df[df['PRODUCT_GROUP'] == 'Both']

    return df[df['PRODUCT_GROUP'].isin([product_group, 'Both'])]


def generate_dq_summary(
    df: pd.DataFrame,
    product_group: str,
    sla_threshold: float = 98.0
) -> pd.DataFrame:
    """
    Generate DQ summary per execution_date
    """

    # Filter data
    filtered_df = filter_by_product_group(df, product_group)

    # Group by execution_date and calculate metrics
    summary_df = (
        filtered_df
        .groupby('execution_date', as_index=False)
        .agg(
            avg_pass_percentage=('Pass_Percentage', 'mean'),
            best_pass_percentage=('Pass_Percentage', 'max'),
            worst_pass_percentage=('Pass_Percentage', 'min')
        )
    )

    # Add product group column
    summary_df['PRODUCT_GROUP'] = product_group

    # Add DQ Status based on SLA
    summary_df['DQ_STATUS'] = summary_df['avg_pass_percentage'].apply(
        lambda x: 'PASS' if x >= sla_threshold else 'FAIL'
    )

    return summary_df


def save_to_excel(
    df: pd.DataFrame,
    output_file: str
):
    """
    Save DataFrame to Excel
    """
    df.to_excel(output_file, index=False)


def main():
    # ========================
    # INPUTS (CHANGE HERE)
    # ========================
    input_file = "dq_input.xlsx"
    product_group = "Loans"   # Loans | Deposits | Both
    output_file = "dq_summary_loans.xlsx"

    # ========================
    # PROCESS
    # ========================
    df = load_data(input_file)

    dq_summary = generate_dq_summary(
        df=df,
        product_group=product_group,
        sla_threshold=98.0
    )

    # ========================
    # OUTPUT
    # ========================
    print("\nDQ SUMMARY\n")
    print(dq_summary)

    save_to_excel(dq_summary, output_file)


if __name__ == "__main__":
    main()
