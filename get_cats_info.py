from pathlib import Path

def get_cats_info(path) -> list[dict]:
    with open(path, 'r', encoding='utf-8') as file:
        cats = file.readlines()
        cats_info = []
        for cat in cats:
            cat_dict = {}
            # cat_dict['id'], cat_dict['name'], cat_dict['age'] = cat.split(",")
            id, name, age = cat.split(',')
            cat_dict['id'], cat_dict['name'], cat_dict['age'] = id, name, age.strip()
            cats_info.append(cat_dict) # cat_dict перезаписується
            # print(cat_dict)
        return cats_info
# get_cats_info("cats_file.txt")
print(get_cats_info("cats_file.txt"))