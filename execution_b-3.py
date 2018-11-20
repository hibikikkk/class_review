from customer import Customer

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    print(ken.entry_fee())  # 1000 という値を返す

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    print(tom.entry_fee())  # 1500 という値を返す

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    print(ieyasu.entry_fee())  # 1200 という値を返す
