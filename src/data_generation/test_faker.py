from faker import Faker

fake = Faker()

# print(fake.aadhaar_id)
addresses = []
for i in range(1,101):
    address = fake.address()
    addresses.append(address)

for address in addresses:
    print(address)


# print(addresses)