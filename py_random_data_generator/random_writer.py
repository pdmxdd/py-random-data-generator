from csv import DictWriter

def write_dict_list_to_csv(csv_filename, data_as_dict_list):
    with open(csv_filename, 'w') as csv_file:
        writer = DictWriter(csv_file, fieldnames=data_as_dict_list[0].keys())
        writer.writeheader()
        for d in data_as_dict_list:
            writer.writerow(d)
