#** start of main.py **

full_dot = '●'
empty_dot = '○'

def create_character(ch_name, strength, intelligence, charisma):
    #3
    if not isinstance (ch_name, str):
        return 'The character name should be a string'
    elif ch_name == '':
        return 'The character should have a name'
    elif len(ch_name) > 10:
        return 'The character name is too long'
    elif ' ' in ch_name:
        return 'The character name should not contain spaces'
    #4
    elif not isinstance (strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else:
    #5
        line1 = ch_name
        line2 = 'STR ' + (full_dot * strength) + (empty_dot * (10 - strength ))
        line3 = 'INT ' + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
        line4 = 'CHA ' + (full_dot * charisma) + (empty_dot * (10 - charisma))
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

print(create_character('ren', 4, 2, 1))

#** end of main.py **

