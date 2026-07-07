from pyspark.sql.functions import trim, col

def trim_whitespace(df):

    for c in df.columns:
        df =  df.withColumn(c, trim(col(c)))


    print("\nWhitespaces trimmed.")
    return df

