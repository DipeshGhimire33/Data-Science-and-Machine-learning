nested_data = {
    "user": "Alice",
    "profile": {
        "info": {
            "age": 30,
            "city": "Denver",
        },
        "tags": ["admin", "developer"],
    },
    "settings": {
        "theme": "dark",
    },
}


def flatten_dict(data, parent_key=""):
    """Flatten a nested dictionary using dot notation."""
    flattened_data = {}

    for key, value in data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            flattened_data.update(flatten_dict(value, new_key))

        elif isinstance(value, list):
            for index, item in enumerate(value):
                list_key = f"{new_key}.{index}"

                if isinstance(item, dict):
                    flattened_data.update(flatten_dict(item, list_key))
                else:
                    flattened_data[list_key] = item

        else:
            flattened_data[new_key] = value

    return flattened_data


flattened_data = flatten_dict(nested_data)

print(flattened_data)