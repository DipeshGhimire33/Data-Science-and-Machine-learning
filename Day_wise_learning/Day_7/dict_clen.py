nested_data ={
    "user": "Alice",
    "profile": {
        "info": {
            "age": 30,
            "city": "Denver"
        },
        "tags": ["admin", "developer"]
    },
    "settings": {
        "theme": "dark"
    }
    }


expected_dict = {}

def flatten_list(data, parent_key=""):
    for k, v in data.items():
        new_key = f"{parent_key}.{k}" if parent_key else k

        if isinstance(v, dict):
            flatten_list(v, new_key)

        elif isinstance(v, list):
            for i, item in enumerate(v):
                list_key = f"{new_key}.{i}"
                
                if isinstance(item, dict):
                    flatten_list(item, list_key)
                else:
                    expected_dict[list_key] = item

        else:
            expected_dict[new_key] = v


flatten_list(nested_data)

print(expected_dict)


# Excepted Dict:
# {
#     "user": "Alice",
#     "profile.info.age": 30,
#     "profile.info.city": "Denver",
#     "profile.tags.0": "admin",
#     "profile.tags.1": "developer",
#     "settings.theme": "dark"
# }