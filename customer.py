class Customer:

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(self.first_name + " " + self.family_name)

    def entry_fee(self):
        # ガード節使ってみた
        if self.age < 20:
            return 1000

        if self.age >= 20 and self.age < 65:
            return 1500

        if self.age >= 65:
            return 1200
