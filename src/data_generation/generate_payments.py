import csv
import random
from faker import Faker
from constants import random_payment_method, random_payment_status


fake = Faker()

def generate_payments(num_payments, output_file):

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)
        writer.writerow([
            "payment_id",
            "order_id",
            "payment_method",
            "payment_status",
            "payment_date"
        ])


        for payment_id in range(1,num_payments+1):

            writer.writerow([
                payment_id,
                payment_id, #order_id
                random_payment_method(),
                random_payment_status(),
                fake.date_between(start_date="-3y", end_date="today")
            ])


    print(f"{num_payments} generated and written successfully.")



if __name__ == "__main__":
    generate_payments(num_payments=1000, output_file="data/raw/payments.csv")