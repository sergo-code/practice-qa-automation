import json
import os


def get_path(data_file):
    cfg_file_directory = 'config'
    return os.path.join(os.getcwd(), cfg_file_directory, data_file)


def get_data(file_name):
    DATA_FILE = get_path(file_name)
    data = list()
    with open(DATA_FILE, 'r', encoding='utf8') as file:
        reader = json.load(file)
        for item in reader.items():
            data.append(tuple(item))
    return data


if __name__ == '__main__':
    print(get_data('practice_form.json'))
