import csv

# Returns # of deaths per year
def deaths_by_year():
    with open('data/Accidental_Drug_Deaths_Cleansed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        # Dict containing deaths per year
        deaths_by_year = {year: 0 for year in range(2012, 2023)}
        # Iterates through csv file
        for row in reader:
            year = int(row['Date'])
            # Adds a death to respective year in the dict
            if year in deaths_by_year:
                deaths_by_year[year] += 1
    return deaths_by_year

# Returns # and % of drugs used in a given year
def drug_distribution_by_year(year):
  with open('data/Accidental_Drug_Deaths_Cleansed.csv') as csvfile:
    # Dict containing drugs and their totals and percentages
    drugs = {
        # Drug: [Deaths, Percentage]
        'Alcohol': [0, 0],
        'Heroin': [0, 0],
        'Cocaine': [0, 0],
        'Fentanyl': [0, 0],
        'Oxycodone': [0, 0],
        'Oxymorphone': [0, 0],
        'Ethanol': [0, 0],
        'Hydrocodone': [0, 0],
        'Benzodiazepine': [0, 0],
        'Methadone': [0, 0],
        'Amphet': [0, 0],
        'Tramad': [0, 0],
        'Morphine': [0, 0],
        'Xylazine': [0, 0],
        'Gabapentin': [0, 0],
        'Other': [0, 0],
        'Total': 0
    }
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Checks if year in file matches given year
        if int(row['Date']) == year:
            # Gets cause of death and drugs involved in it
            drug = row['Real Cause of Death'].lower()
            # Checks if any known drug is found
            found = False
            # Iterates through known drugs
            for key in drugs.keys():
                if key.lower() in drug:
                    # Updates totals and percentages
                    drugs[key][0] += 1
                    drugs['Total'] += 1
                    drugs[key][1] = round(((drugs[key][0] / drugs['Total']) * 100), 2)
                    found = True
            # If no known drug is found, add to 'Other'
            if not found:
                drugs['Other'][0] += 1
                drugs['Total'] += 1
                drugs['Other'][1] = round(((drugs['Other'][0] / drugs['Total']) * 100), 2)
  return drugs

# Returns total deaths of each age in a given range
def death_age_range(lowest, highest):
    with open('data/Accidental_Drug_Deaths_Cleansed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        ages = {str(i): 0 for i in range(lowest, highest+1)}
        for row in reader:
            # Checks if age is known and within the specified range
            if row['Age'].isdigit():
                age = int(row['Age'])
                if lowest <= age <= highest:
                    ages[str(age)] += 1
    return ages

# Returns death by race in a given year
def death_by_race(year):
  with open('data/Accidental_Drug_Deaths_Cleansed.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    races = {"White": 0, "Black": 0, "Asian - All": 0, "Black or African American": 0, "Unknown": 0, "Other": 0}
    for row in reader:
      if int(row['Date']) == year:
        # If the race in the row is found in the dict, adds 1
        try:
          races[row['Race']] += 1
        # If race not found adds to other
        except:
          races["Other"] += 1
  return races

# Returns drug usage between male and female of a given drug
def male_female_drug_usage(drug):
    with open('data/Accidental_Drug_Deaths_Cleansed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        # Dict with totals
        male_female = {
            "Drug": drug,
            "Male": 0,
            "Female": 0
        }
        for row in reader:
            # Checks if given drug is present in the cause of death
            if drug.lower() in row['Real Cause of Death'].lower():
                # Adds to male or female count based on gender
                if row['Sex'] == 'Male':
                    male_female["Male"] += 1
                elif row['Sex'] == 'Female':
                    male_female["Female"] += 1
    return male_female