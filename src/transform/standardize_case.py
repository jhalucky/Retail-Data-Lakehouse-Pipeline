from pyspark.sql.functions import col, upper, lower, initcap
from pyspark.sql.types import StringType

def standardize_case(df):

    for column in df.schema:

        if isinstance(column.dataType, StringType):

            if column.name == "email":
                df = df.withColumn(
                    column.name,
                    lower(col(column.name))
                )

            else:
                df = df.withColumn(
                    column.name,
                    initcap(col(column.name))
                )


    return df