from faker import Faker

fake = Faker()

def user_email_generator():
    generated_email = fake.email()
    return generated_email

def user_name_generator():
    generated_name = fake.first_name()
    return generated_name
