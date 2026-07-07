from pyspark.sql.functions import col, trim, lower, regexp_replace 


def clean_email(df):
    for c in df.columns:

        if c == "email":
            df = df.withColumn(c, regexp_replace(col(c), " ",""))
            df = df.withColumn(c, trim(col(c)))
            df = df.withColumn(c, lower(col(c)))


    return df

    



