# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.
import re
from collections import Counter
# Exercises: Day 18

# Exercises: Level 1
# 1 What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word = re.findall(r'\b\w+\b', paragraph.lower())
counts = Counter(word) # -> word, counts
print(counts)
print('-----------------')
sort = [(count, word) for word, count in counts.items()]
s_sorted = sorted(sort, key=lambda x: x[0], reverse=True)
print(s_sorted[:10])
print('-----------------')

# 2 The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]

pointss = [int(x) for x in points]
print(pointss)
tot = max(pointss) - min(pointss)
print(tot)
print('-----------------')

# Exercises: Level 2
# 1 Write a pattern which identifies if a string is a valid python variable
regex_pattern = r'[a-z][a-zA-Z_0-9]*'

# Exercises: Level 3
# 1 Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text = re.sub("[%@&#$.,;!?]", "", sentence)
print(clean_text)
print('-----------------')
text = re.findall(r'\b\w+\b', clean_text.lower())
county = Counter(text)
print(county)
print('-----------------')
sort2 = [(coty, wrdy) for wrdy, coty in county.items()]
s_sorted2 = sorted(sort2, key=lambda y: y[0], reverse=True)
print(s_sorted2[:3])