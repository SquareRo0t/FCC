#1 Declare an empty list
lst = []

#2 Declare a list with more than 5 items
five_item_list = ["apple", "banana", "pear", "strawberry", "pineapple"]

#3 Find the length of your list
print(len(five_item_list))

#4 Get the first item, the middle item and the last item of the list
print(five_item_list[0])
print(five_item_list[2])
print(five_item_list[4])

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["J", "P", 175, "unmarried", "sweden"]

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 Print the list using print()
print(it_companies)

#8 Print the number of companies in the list
print(len(it_companies))

#9 Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#10 Print the list after modifying one of the companies
# it_companies[0] = "Tesla"
print(it_companies)

#11 Add an IT company to it_companies
# it_companies.append("Facebook")
print(it_companies)

#12 Insert an IT company in the middle of the companies list
# it_companies.insert(2, "X")
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14 Join the it_companies with a string '#;  '
res = "#; ".join(it_companies)
print(res)

#15 Check if a certain company exists in the it_companies list.
does_exist = "twittwr" in it_companies
print(does_exist)

#16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17 Reverse the list in descending order using reverse() method
# it_companies.sort(reverse=True)
print(it_companies)

#18 Slice out the first 3 companies from the list
print(it_companies[:3])

#19 Slice out the last 3 companies from the list
print(it_companies[-3:])

#20 Slice out the middle IT company or companies from the list
print(it_companies[3:4])

#21 Remove the first IT company from the list
it_companies.remove("Amazon")
print(it_companies)

#22 Remove the middle IT company or companies from the list
it_companies.remove("GOOGLE")
print(it_companies)

#23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24 Remove all IT companies from the list
# del it_companies[0:5]
it_companies.clear()
print(it_companies)

#25 Destroy the IT companies list
# del it_companies

#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

tot_join = front_end + back_end # Skapar ny lista med andra listor
front_end.extend(back_end) # Lägger till i nuvarande lista
print(tot_join)
print(front_end)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = tot_join.copy()
print(full_stack)
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
print("-----------------------------------------------------")

# Exercises: Level 2
#1 The following is a list of 10 students ages:
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
median_tot = ages[4] + ages[5]
median = median_tot / 2
print(median)

# Find the average age (sum of all items divided by their number )
ages_sum = sum(ages)
ages_len = len(ages)
ages_tot = ages_sum / ages_len
print(ages_tot)

# Find the range of the ages (max minus min)
ages_max = max(ages)
ages_min = min(ages)
range_tot = ages_max - ages_min
print(range_tot)

# Compare the value of (min - average) and (max - average), use abs() method
value1 = ages_min - ages_tot
value2= ages_max - ages_tot
print(abs(value1))
print(abs(value2))

#2 Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
country_len = len(countries)
print(countries[97])

#3 Divide the countries list into two equal lists if it is even if not one more country for the first half.
c1 = countries[0:98]
c2= countries[98:]
print(c1)
print("This is c2 ",c2)

#4 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries1
print(scandic)