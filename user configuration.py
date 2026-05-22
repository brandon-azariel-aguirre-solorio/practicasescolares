test_settings = {
        'theme':'dark',
        'notifications':'disable',
        'volume':'low',
        'xd':'a'
}
      
def add_setting(dictionary_set, tuple_set):
    key, value = tuple_set
    key = key.lower()
    value = value.lower()
    if key in dictionary_set:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary_set[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionary_sett, tuple_sett):
    key, value = tuple_sett
    key = key.lower()
    value = value.lower()
    if key in dictionary_sett:
        dictionary_sett[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary_setti, tuple_setti):
    key = tuple_setti
    key = key.lower()
    if key in dictionary_setti:
        dictionary_setti.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dictionary_setting):
    if not dictionary_setting:
        return 'No settings available.'
    else:
        result = "Current User Settings:\n"
        for key, value in dictionary_setting.items():
            result += f"{key.capitalize()}: {value}\n"

        return result

print (update_setting(test_settings,('theme','dark')))
