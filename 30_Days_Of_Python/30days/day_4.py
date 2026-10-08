text = "Thirty", "Days", "Of", "Python"
result = " ".join(text)
# print(result)

text2 = "Coding", "For", "All"
res = " ".join(text2)
# print(res)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company [7:])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))
print(company.split())

company2 = "Python for Everyone"
print(company2)
print(company2.replace("Everyone", "All"))

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_company.split(", "))

#15 What is the character at index 0 in the string Coding For All. "C"
print(company[10])

#16 What is the last index of the string Coding For All. "13"

#17 What character is at index 10 in "Coding For All" string. "blankspace"

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
PFE = "Python For Everyone"

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
CFA = "Coding For All"

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(CFA.find("C"))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(CFA.find("F"))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(CFA.rfind("l"))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_sentence = "You cannot end a sentence with because because because is a conjunction"
print(new_sentence.find("because"))
print(new_sentence.index("because"))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.rindex("because"))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence[31:54])

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.find("because"))

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence[31:54])

#28 Does 'Coding For All' start with a substring Coding?
print(CFA.startswith("Coding"))

#29 Does 'Coding For All' end with a substring coding?
print(CFA.endswith("coding"))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
CFA2 = "   Coding For All      "
print(CFA2.strip())

#31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython -> FALSE
# thirty_days_of_python -> TRUE
true_or_false = "thirty_days_of_python"
print(true_or_false.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
res_lib = "# ".join(python_lib)
print(res_lib)

#33 Use the new line escape sequence to separate the following sentences.
text3 = "I am enjoying this challenge. \nI just wonder what is next."
print(text3)

#34 Use a tab escape sequence to write the following lines.
print("Name\tage\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square")

#36 Make the following using string formatting methods:
tal1 = 8
tal2 = 6
print(f"{tal1} + {tal2} = {tal1 + tal2} ")
print(f"{tal1} - {tal2} = {tal1 - tal2} ")
print(f"{tal1} * {tal2} = {tal1 * tal2} ")
print(f"{tal1} / {tal2} = {tal1 / tal2} ")
print(f"{tal1} % {tal2} = {tal1 % tal2} ")
print(f"{tal1} // {tal2} = {tal1 // tal2} ")
print(f"{tal1} ** {tal2} = {tal1 ** tal2} ")