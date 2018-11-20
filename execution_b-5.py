from customer import Customer

if __name__ == "__main__":
    taro = Customer(first_name="Taro", family_name="Yamada", age=3)

    print(taro.entry_fee())
