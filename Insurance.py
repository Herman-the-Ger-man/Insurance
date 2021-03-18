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

        age.append(int(row["age"]))
        sex.append(row["sex"])
        bmi.append(float(row["bmi"]))
        children.append(int(row["children"]))
        smoker.append(row["smoker"])
        region.append(row["region"])
        charges.append(float(row["charges"]))

        counter += 1

# classifier for bmi
class bmi_classification:
    # aggregates the bmi values into different segments
    bmi_segments = {"thin": [], "normal": [], "fat": [], "very fat": []}

    # shows the distribution of the different within the total dataset
    bmi_segments_distribution = {"thin": 0, "normal": 0, "fat": 0, "very fat": 0}
    
    for i in bmi:
        if i < 18.5:
            bmi_segments["thin"].append(i)
        elif (i >= 18.5) and (i < 24.9):
            bmi_segments["normal"].append(i)
        elif (i >= 24.9) and (i < 29.9):
            bmi_segments["fat"].append(i)
        else:
            bmi_segments["very fat"].append(i)
    
    bmi_segments_distribution["thin"] = round(len(bmi_segments["thin"])/counter*100, 2)
    bmi_segments_distribution["normal"] = round(len(bmi_segments["normal"])/counter*100, 2)
    bmi_segments_distribution["fat"] = round(len(bmi_segments["fat"])/counter*100, 2)
    bmi_segments_distribution["very fat"] = round(len(bmi_segments["very fat"])/counter*100, 2)

    print(bmi_segments_distribution["thin"])
    print(bmi_segments_distribution["normal"])
    print(bmi_segments_distribution["fat"])
    print(bmi_segments_distribution["very fat"])

bmi_classification = bmi_classification()