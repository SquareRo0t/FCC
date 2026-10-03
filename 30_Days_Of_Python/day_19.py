# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Exercises: Day 19

# Exercises: Level 1
# 1 Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def count_lines_words(text):
    lines = text.splitlines()
    words = text.splitlines()
    return len(lines), len(words)

with open("30 Days Of Python/obama_speech.txt file", "r", encoding="utf-8") as file:
    text = file.read()

lines, words = count_lines_words(text)

print(lines)
print(words)