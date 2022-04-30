from faker import Faker
import random

company_choices = [
    "Boeing",
    "VMLY&R",
    "Express Scripts",
    "Edward Jones",
    "Centene",
    "World Wide Technology",
    "Microsoft",
    "Ad Astra",
    "Commerce Bank",
    "Mastercard",
    "Spectrum",
    "Hunter Engineering",
    "Emerson Electric",
    "Freedom Pay",
    "Washington University",
    "Apple",
    "Balto",
    "Netflix",
    "Square",
    "Amazon",
    "Google",
    "Facebook"
]

def get_password(good_password):
    possible_passwords = [good_password, "password", "admin", "123456", "12345", "batman", "matlock"]
    password_weights = [15, 1, 1, 1, 1, 1, 1]
    return random.choices(possible_passwords, password_weights)[0]

def get_company():
    return random.choices(company_choices)[0]

def user_data_dict():
    fake = Faker()
    user_dict = {}
    user_dict['first_name'] = fake.first_name()
    user_dict['last_name'] = fake.last_name()
    user_dict['email'] = fake.email()
    user_dict['employer'] = get_company()
    return user_dict

def sensitive_user_data_dict():
    fake = Faker()
    sensitive_user_data_dict = {}
    sensitive_user_data_dict['email'] = fake.email()
    sensitive_user_data_dict['username'] = fake.user_name()
    sensitive_user_data_dict['password'] = get_password(fake.password())
    return sensitive_user_data_dict

def transaction_data_dict():
    fake = Faker()
    transaction_data_dict = {}
    transaction_data_dict['name'] = fake.name()
    transaction_data_dict['email'] = fake.email()
    transaction_data_dict['type'] = random.choices(["deposit", "withdrawl"])[0]
    multiplication_amounts = [1000, 1500, 2000, 3000, 10000, 100000]
    multiplication_weights = [15, 12, 8, 6, 3, 2]
    amount = float("{:.2f}".format(random.random() * random.choices(multiplication_amounts, multiplication_weights)[0]))
    transaction_data_dict['amount'] = amount
    return transaction_data_dict

def log_data_dict():
    fake = Faker()
    log_data_dict = {}
    log_data_dict['ipv4_address'] = fake.ipv4()
    log_data_dict['user_agent'] = fake.user_agent().replace(",", ";")
    log_data_dict['iso_datetime'] = fake.past_datetime().isoformat()
    return log_data_dict

def get_users_list(amount=10):
    validated_amount = 500 if amount > 500 else amount
    return [user_data_dict() for i in range(validated_amount)]

def get_sensitive_users_list(amount=10):
    validated_amount = 500 if amount > 500 else amount
    return [sensitive_user_data_dict() for i in range(validated_amount)]

def get_transactions_list(amount=10):
    validated_amount = 500 if amount > 500 else amount
    return [transaction_data_dict() for i in range(validated_amount)]

def get_logs_list(amount=10):
    validated_amount = 500 if amount > 500 else amount
    return [log_data_dict() for i in range(validated_amount)]
