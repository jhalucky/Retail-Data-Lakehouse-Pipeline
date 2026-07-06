from src.config.spark_session import get_spark_session
from src.extract.read_csv import read_csv
from src.extract.explore_df import print_schema, show_columns, describe_data, count_rows, show_rows
from src.experiments.lazy_evaluation import lazy_evaluation_demo
from src.validate.missing import validate_missing_values

spark = get_spark_session()
customer_df = read_csv(spark, "data/raw/customers.csv")
# print_schema(customer_df)
# print(f"spark version : {spark.version}")
# print(show_columns(customer_df))
# print(describe_data(customer_df))
# print(count_rows(customer_df))
# print(show_rows(customer_df, 10))
# print(validate_missing_values(customer_df))

customer_df.dropDuplicates()
# lazy_evaluation_demo(customer_df)
spark.stop()