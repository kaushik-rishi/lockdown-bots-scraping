
def load_frm_DB():
    loaded_data = {}
    with open(DB_NAME, 'r') as fp:
        loaded_data = json.load(fp)
    return loaded_data


def save_to_DB(data_):
    with open(DB_NAME, 'w') as fp:
        json.dump(data_, fp, indent=4)


def urlJoin(service, attach):
    if service[len(service)-1] == '/':
        service = service[:len(service)-1]
    if attach[0] == '/':
        attach = attach[1:]
    joined = service+'/'+attach
    return joined


def print_menu():
    print('-'*40, 'Covid 19 Reporter', '-'*40, end='\n\n')
    with open('main menu.txt', 'r') as fp:
        for line in fp:
            print(line.strip())
    print('-'*100)
