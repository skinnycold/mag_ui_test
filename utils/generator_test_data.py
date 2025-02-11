from faker import Faker

faker = Faker()

class DataGenerator:
    f_name = None
    l_name = None
    passw = None
    e_mail = None
    def first_name(self):
        self.f_name = faker.first_name()
        return self.f_name

    def last_name(self):
        self.l_name = faker.last_name()
        return self.l_name

    def password(self):
        self.passw = faker.password()
        return self.passw
    def email(self):
        self.e_mail = faker.email()
        return self.e_mail


print(faker.last_name())
print(faker.first_name())
print(faker.email())
print(faker.password())