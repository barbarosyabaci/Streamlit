def combine_values(row, columns_to_combine):
    import pandas as pd
    import numpy as np
    combined_values = ''.join(str(row[column]) for column in columns_to_combine if pd.notna(row[column]))
    return combined_values if combined_values else np.nan,

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')