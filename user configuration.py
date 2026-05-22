test_settings =[
    {
        'theme':'dark',
        'languages':'english'
    }
    
]

def add_setting(dictionary_set, tuple_set):
    key, value = dictionary_set
    key = key.lower()
    value = value.lower()
    
    if key in dictionary_set:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    dictionary_set[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!."

def update_setting(dictionary_set, tuple_set):
    key, value = dictionary_set
    key = key.lower()
    value = value.lower()
    if key in dictionary_set:
        return f"Setting '{key}' update to {value} successfully."
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delate_setting(dictionary_set, tuple_set):
    key, value = dictionary_set
    key = key.lower()
    if key in dictionary_set:
        
        return f"Setting '{key}' deleted successfully."
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
