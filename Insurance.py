# Medical Insurance Project

import csv

# creates a List by each individual with value for age, sex, bmi, ...
individuals = []

# creates a list for a specific kpi with entries from the individuals
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# starts a counter for the number of rows in the csv file, thus the number of individuals in the database
counter = 0

# opens the csv file and transform it to the variables
with open("insurance.csv", newline="") as data:
    data = csv.DictReader(data)
    for row in data:
        individuals.append(row)

        age.append(row["age"])
        sex.append(row["sex"])
        bmi.append(row["bmi"])
        children.append(row["children"])
        smoker.append(row["smoker"])
        region.append(row["region"])
        charges.append(row["charges"])

        counter += 1

class bmi:
    pass

print(individuals)
print(age)
print(counter)