import json

def load_from_jsonl(filename):
    """
    Load data from a .jsonl file.

    :param filename: The path to the .jsonl file.
    :return: A list of dictionaries.
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(json.loads(line.strip()))
    return data

def save_to_jsonl(data, filename):
    """
    Save data to a .jsonl file.

    :param data: A list of dictionaries.
    :param filename: The path to the .jsonl file where data will be saved.
    """
    with open(filename, 'a') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')
