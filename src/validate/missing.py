from pyspark.sql.functions import col, when, count

def validate_missing_values(df):

    missing_df = df.select([
        count(
            when(col(column).isNull(), column)
        ).alias(column)

        for column in df.columns
    ])

    missing_df.show()

    return df