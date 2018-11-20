from customer import Customer

if __name__ == "__main__":
    hanako = Customer(first_name="Hanako", family_name="Yamada", age=80)

    print(hanako.entry_fee())
