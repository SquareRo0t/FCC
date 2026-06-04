def add_setting(dictionary_setting, key_value_tuple):

    # Unpack and convert to lowercase strings
    key = str(key_value_tuple[0].lower())
    value = str(key_value_tuple[1].lower())

    # Check if the key already exists
    if key in dictionary_setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    # Lägg till i ordboken ENDAST om den inte fanns, och returnera rätt meddelande
    dictionary_setting[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary_setting, key_value_tuple):
    key = str(key_value_tuple[0].lower())
    value = str(key_value_tuple[1].lower())

    if key in dictionary_setting:
        dictionary_setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary_setting, key_value_tuple):
    key = str(key_value_tuple).lower()
        
    if key in dictionary_setting:
        del dictionary_setting[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

def view_settings(dictionary_setting):
    if not dictionary_setting:
        return "No settings available."

    # Starta strängen för inställningarna
    result = "Current User Settings:\n"

     # Loopa igenom alla nycklar och värden
    for key, value in dictionary_setting.items():
        # Gör första bokstaven i nyckeln stor (.capitalize())
        result += f"{str(key).capitalize()}: {value}\n"

    # Returnerar strängen som den är, vilket betyder att den slutar på \n
    return result

# Skapa ordboken med några startinställningar
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}
