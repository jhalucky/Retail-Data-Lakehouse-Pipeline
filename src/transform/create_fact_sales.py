from pyspark.sql.functions import col 


def create_fact_sales(df):

    df = df.withColumn(
        "sales_amount",
        col("quantity") * col("unit_price")
    )

    df = df.select(
        "order_id",
        "order_date",
        "customer_id",
        "first_name",
        "last_name",
        "city",
        "state",
        "product_id",
        "product_name",
        "category",
        "brand",
        "quantity",
        "unit_price",
        "sales_amount",
        "payment_method",
        "payment_status"
    )


    return df


