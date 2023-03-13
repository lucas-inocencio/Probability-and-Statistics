def log_transform_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Performs a log10 transformation on two dataframes after adding 1 to each value.

    Args:
        df1: A pandas DataFrame representing the first dataset.
        df2: A pandas DataFrame representing the second dataset.

    Returns:
        A tuple of two pandas DataFrames representing the transformed datasets.
    """
    try:
        # Create new dataframes to store the transformed data
        transformed_df1 = np.log10(df1 + 1)
        transformed_df2 = np.log10(df2 + 1)
    except ValueError:
        # Handle any errors that occur when taking the log of negative or zero values
        print("Error: DataFrame contains negative or zero values.")
        return None
    
    # Rename the dataframes to more descriptive names
    transformed_df1.name = "smart_tv_data_transformed"
    transformed_df2.name = "chromecast_data_transformed"
    
    # Return the transformed dataframes
    return transformed_df1, transformed_df2