import random
import csv
from faker import Faker
from constants import random_order_status


fake = Faker()

def generate_orders(num_orders, output_file):

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)
        writer.writerow([
            "order_id",
            "customer_id",
            "order_date",
            "order_status",
            "total_amount"
        ])


        for order_id in range(1, num_orders+1):

            writer.writerow([
                order_id,
                random.randint(1,1000),
                fake.date_between(start_date="-3y",end_date="today"),
                random_order_status(),
                random.randint(100,100000)

            ])



    print(f"{num_orders} generated successfully.")



if __name__ == "__main__":
    generate_orders(num_orders=1000, output_file="data/raw/orders.csv")



    






