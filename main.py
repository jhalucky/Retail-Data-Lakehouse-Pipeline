from src.config.spark_session import get_spark_session

spark = get_spark_session()

print(f"spark version : {spark.version}")

spark.stop()