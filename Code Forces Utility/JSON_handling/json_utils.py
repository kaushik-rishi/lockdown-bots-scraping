import json


def load_frm_DB(DB_NAME):
    """
        Loads data from database.json into a 
    """

    loaded_data = {}
    with open(DB_NAME, 'r') as fp:
        loaded_data = json.load(fp)
    return loaded_data


def save_to_DB(data_, DB_NAME):
    with open(DB_NAME, 'w') as fp:
        json.dump(data_, fp, indent=4)
