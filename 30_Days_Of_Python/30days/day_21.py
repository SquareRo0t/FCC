# syntax
# class ClassName:
    #   def __init__ (self, name):
    #     # self allows to attach parameter to the class
    #       self.name =name

# Exercises: Day 21

# Exercises: Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self):
        pass

    def count(self):
        return len(ages)

    def sum(self):
        return sum(ages)

    def min(self):
        return min(ages)

    def max(self):
        return max(ages)

    def range(self):
        return max(ages) - min(ages)

    def mean(self):
       return round(sum(ages) / len(ages))

    def median(self):
        sorted_ages = sorted(ages)
        n = len(sorted_ages)
        if n % 2 == 1:
            return sorted_ages[n // 2]
        else:
            return(sorted_ages[n // 2] + sorted_ages[n // 2] / 2)

    def mode(self):
        counts = {}
        for age in ages:
            if age in counts:
                counts[age] +=1
            else:
                counts[age] = 1
        return max(counts, key=counts.get)

    def std(self):
        mean = sum(ages) / len(ages)
        squared_differences = []
        for age in ages:
            difference = age - mean
            squared_differences.append(difference**2)
        variance = sum(squared_differences) / len(ages)
        return variance ** 0.5

    def var(self):
        mean = sum(ages) / len(ages)
        squared_differences = []

        for age in ages:
            difference = age - mean
            squared_differences.append(difference**2)
        return sum(squared_differences) / len(ages)

    def freq_dist(self):
        freq = {}
        for age in ages:
            if age in freq:
                freq[age] +=1
            else:
                freq[age] = 1
        return freq

    def describe(self):
        print("Count:", data.count())
        print("Sum:", data.sum())
        print("Min:", data.min())
        print("Max:", data.max())
        print("Range:", data.range())
        print("Mean:", data.mean())
        print("Median:", data.median())
        print("Mode:", data.mode())
        print("Variance:", data.var())
        print("Standard Deviation:", data.std())
        print("Frequency Distribution:", data.freq_dist())

    
data = Statistics()
data.describe()
# print("Count:", data.count())
# print("Sum:", data.sum())
# print("Min:", data.min())
# print("Max:", data.max())
# print("Range:", data.range())
# print("Mean:", data.mean())
# print("Median:", data.median())
# print("Mode:", data.mode())
# print("Standard Deviation:", data.std())
# print("Variance:", data.var())
# print("Frequency Distribution:", data.freq_dist())
print('-------------------------------')

# Exercises: Level 2
# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
    def __init__(self, firstname, lastname):
        # properties
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set() # set() = set med tuples.
        self.expenses = set()

    def total_income(self):
        pass

    def total_expense(self):
        pass

    def account_info(self):
        pass

    def add_income(self):
        pass

    def add_expense(self):
        pass

    def account_balance(self):
        pass