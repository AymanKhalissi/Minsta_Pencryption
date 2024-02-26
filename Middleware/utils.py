def get_key_from_file(filepath):
    with open(filepath, 'rb') as file:
        key = file.read()
    return key