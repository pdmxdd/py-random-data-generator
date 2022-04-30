from py_random_data_generator import __version__

from py_random_data_generator.generate_random import user_data_dict, sensitive_user_data_dict, transaction_data_dict, log_data_dict, get_users_list, get_sensitive_users_list, get_transactions_list, get_logs_list

def test_user_data_dict():
    actual = user_data_dict()
    assert len(actual.keys()) == 4
    assert 'first_name' in actual.keys()
    assert 'last_name' in actual.keys()
    assert 'email' in actual.keys()
    assert 'employer' in actual.keys()
    assert type(actual['first_name']) == type("string")
    assert type(actual['last_name']) == type("string")
    assert type(actual['email']) == type("string")
    assert type(actual['employer']) == type("string")

def test_sensitive_user_data_dict():
    actual = sensitive_user_data_dict()
    assert len(actual.keys()) == 3
    assert 'email' in actual.keys()
    assert 'username' in actual.keys()
    assert 'password' in actual.keys()
    assert type(actual['email']) == type("string")
    assert type(actual['username']) == type("string")
    assert type(actual['password']) == type("string")

def test_transaction_data_dict():
    actual = transaction_data_dict()
    actual_keys = actual.keys()
    assert len(actual_keys) == 4
    assert 'name' in actual_keys
    assert 'email' in actual_keys
    assert 'type' in actual_keys
    assert 'amount' in actual_keys
    assert type(actual['name']) == type("string")
    assert type(actual['email']) == type("string")
    assert type(actual['type']) == type("string")
    assert type(actual['amount']) == type(100.15) 

def test_log_data_dict():
    actual = log_data_dict()
    actual_keys = actual.keys()
    assert len(actual_keys) == 3
    assert 'ipv4_address' in actual_keys
    assert 'user_agent' in actual_keys
    assert 'iso_datetime' in actual_keys
    assert type(actual['ipv4_address']) == type("string")
    assert type(actual['user_agent']) == type("string")
    assert type(actual['iso_datetime']) == type("string")

def test_get_users_list_default():
    actual = get_users_list()
    assert len(actual) == 10

def test_get_users_list_within():
    actual = get_users_list(15)
    assert len(actual) == 15

def test_get_users_list_above():
    actual = get_users_list(501)
    assert len(actual) == 500


def test_version():
    assert __version__ == '0.1.0'
