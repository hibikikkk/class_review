class Customer:

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        # ガード節使ってみた
        if self.age <= 3:
            return 0

        if self.age < 20:
            return 1000

        if self.age >= 20 and self.age < 65:
            return 1500

        if self.age >= 65 and self.age < 75:
            return 1200

        if self.age >= 75:
            return 500

    def info_csv(self):
        user_full_name = self.full_name()
        user_payment = self.entry_fee()

        return f"{user_full_name},{self.age},{user_payment}"

    def info_format_split_blank(self):
        user_full_name = self.full_name()
        user_payment = self.entry_fee()

        return f"{user_full_name}   {self.age}  {user_payment}"

    def info_format_split_pipe(self):
