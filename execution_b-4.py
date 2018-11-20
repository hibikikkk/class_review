from customer import Customer

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    print(ken.info_csv())  # "Tom Ford,57,1500" という値を返す

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を返す
