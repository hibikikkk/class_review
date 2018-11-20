from customer import Customer

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

    print(ken.info_format_split_pipe())
    print(tom.info_format_split_pipe())
    print(ieyasu.info_format_split_pipe())
