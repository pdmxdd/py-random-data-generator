from generate_random import get_users_list, get_sensitive_users_list, get_transactions_list, get_logs_list

from random_writer import write_dict_list_to_csv

write_dict_list_to_csv('test-user.csv', get_users_list(11))
write_dict_list_to_csv('test-sensitive.csv', get_sensitive_users_list(11))
write_dict_list_to_csv('test-transactions.csv', get_transactions_list(11))
write_dict_list_to_csv('test-logs.csv', get_logs_list(11))

# print(user_data_dict())

# print(get_users_list(10))
# print(get_sensitive_users_list(10))
# print(get_transactions_list(10))
# print(get_logs_list(10))
# print(len(get_logs_list(25)))

# user_data("temp.csv", 5)


