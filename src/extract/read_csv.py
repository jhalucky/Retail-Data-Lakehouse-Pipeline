def read_csv(spark, file_path):

    """ Read a csv file and returns a spark DataFrame.
        
        Parameters: File path, returns: 

        spark.read.csv, spark dataframe

        spark is an object already executed in main.py using get_spark_session
    
    """



    # i had first used spark.read.csv

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
    )

    return df

