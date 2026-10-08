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

with open("30_Days_Of_Python/melina_trump_speech.txt", "r", encoding="utf-8") as file:
    text = file.read()
lines, words = count_lines_words(text)
print(lines)
print(words)
print('-------------------')

# 2 Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
with open("30_Days_Of_Python/countries_data.json", "r", encoding="utf-8" ) as f:
    countries = json.load(f)

def top_10_lanugages(countries):
    languages_count = {}

    for country in countries:
        for languages in country["languages"]:
            if languages in languages_count:
                languages_count[languages] += 1
            else:
                languages_count[languages] = 1
    sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:3]
print(top_10_lanugages(countries))
print('-------------------')

# 3 Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# Sort out the ten most populated countries.
def top_10_populated_countries(population):
    population_dic = {}

    for country in population:
    #   key = landets namn
    #   value = landets population
        population_dic[country["name"]] = country["population"]
    sorted_pops = sorted(population_dic.items(), key=lambda item: item[1], reverse=True)

    top_10 = sorted_pops[:10]

    return [{"country": country, "population": population} for country, population in top_10]
print(top_10_populated_countries(countries))
print('-------------------')

# Exercises: Level 2
import re
from collections import Counter

# 1 Extract all incoming email addresses as a list from the email_exchange_big.txt file.
with open("30_Days_Of_Python/email_exchanges.txt", "r", encoding="utf-8") as g:
    mail = g.read()

    # re.findall(REGEX, TEXT, FLAGGA)
    mejler = re.findall('^From ([^ ]+)', mail, re.MULTILINE)
    print(mejler)
print('-------------------')

# 3 Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(text, number: int):
    if number <= 0:
        raise ValueError("number must be a positive integer")

    if not isinstance(text, str):
        text = text.read()
    
    word = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(word) # -> word, counts
    
    sort = [(count, word) for word, count in counts.items()]
    return sorted(sort, key=lambda x: x[0], reverse=True)[:number]
print(find_most_common_words("hello hello world world world python", 3))
print('-------------------')

# 3 Use the function, find_most_frequent_words to find:
# The ten most frequent words used in Obama's speech
# The ten most frequent words used in Michelle's speech
# The ten most frequent words used in Trump's speech
# The ten most frequent words used in Melina's speech
with open("30_Days_Of_Python/obama_speech.txt", "r", encoding="utf-8") as file:
    text = file.read()

def find_most_frequent_words (text, number: int):
    if number <= 0:
        raise ValueError("number must be a positive integer")

    if not isinstance(text, str):
        text = text.read()
    
    word = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(word) # -> word, counts
    
    sort = [(count, word) for word, count in counts.items()]
    return sorted(sort, key=lambda x: x[0], reverse=True)[:number]
print(find_most_frequent_words (text, 10))
print('-------------------')

# 4 Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

# 5 Find the 10 most repeated words in the romeo_and_juliet.txt
with open("30_Days_Of_Python/romeo_and_juliet.txt", "r", encoding="utf-8") as file1:
    most_words_text = file1.read()

    word = re.findall(r'\b\w+\b', most_words_text.lower())
    counts = Counter(word) # -> word, counts
    
    sort = [(count, word) for word, count in counts.items()]
    most_words = sorted(sort, key=lambda x: x[0], reverse=True)
    print(most_words[:10])
print('-------------------')

# 6 Read the hacker news csv file and find out:
import csv
with open("30_Days_Of_Python/hacker_news.csv", "r", encoding="utf-8") as fcsv:
    csv_reader = csv.reader(fcsv)
    rows = list(csv_reader)

# Count the number of lines containing python or Python
# Count the number lines containing JavaScript, javascript or Javascript
# Count the number lines containing Java and not JavaScript
count = 0
for row in rows:
    if "java" in " ".join(row).lower():
        count += 1
print(count)
