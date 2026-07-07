from src.config.spark_session import get_spark_session
from src.extract.read_csv import read_csv
from src.extract.explore_df import print_schema, show_columns, describe_data, count_rows, show_rows
from src.experiments.lazy_evaluation import lazy_evaluation_demo
from src.validate.missing import validate_missing_values
from src.validate.duplicates import validate_duplicate_rows
from src.validate.primary_key import validate_duplicate_primary_keys
from src.validate.email import validate_emails
from src.validate.schema import validate_schema
from src.transform.trim_whitespace import trim_whitespace
from src.transform.standardize_case import standardize_case
from src.transform.clean_email import clean_email

CUSTOMER_SCHEMA = [
    "customer_id",
    "first_name",
    "last_name",
    "gender",
    "email",
    "phone",
    "address",
    "city",
    "state",
    "signup_date"
]
spark = get_spark_session()
customer_df = read_csv(spark, "data/raw/customers.csv")
product_df = read_csv(spark, "data/raw/products.csv")
order_df = read_csv(spark, "data/raw/orders.csv")
order_item_df = read_csv(spark, "data/raw/order_items.csv")
payment_df = read_csv(spark, "data/raw/payments.csv")


# customer_df run
# print_schema(customer_df)
# print(f"spark version : {spark.version}")
# print(show_columns(customer_df))
# print(describe_data(customer_df))
# print(count_rows(customer_df))
# print(show_rows(customer_df, 10))
# print(validate_missing_values(customer_df))

# print(validate_duplicate_rows(customer_df))
# print(validate_duplicate_primary_keys(customer_df, "customer_id"))
# print(count_rows(customer_df))
# validate_emails(customer_df, "email")
# lazy_evaluation_demo(customer_df)
# validate_schema(customer_df, CUSTOMER_SCHEMA)
# trim_whitespace(customer_df)
# standardize_case(customer_df)
customer_df=clean_email(customer_df)
print(show_rows(customer_df, 10))



# order_df run

# print_schema(order_df)
# print(show_columns(order_df))
# print(describe_data(order_df))
# print(count_rows(order_df))
# print(show_rows(order_df, 20))
# print(validate_missing_values(order_df))
# print(validate_duplicate_rows(order_df))
# print(validate_duplicate_primary_keys(order_df, "order_id"))
spark.stop()