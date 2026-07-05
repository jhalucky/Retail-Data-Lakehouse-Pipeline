from read_csv import read_csv
from spark_session import get_spark_session

spark = get_spark_session()

customer_df = read_csv(spark, "data/raw/customer.csv")

print(customer_df.inferSchema())
