# Rough draft

import matplotlib.pyplot as plt


# Takes in list of years and chart type as input (bar or line)
# Displays the comparison of death amount for years given
def yearly_comparisons(years, chart_type, deaths_by_year):
    plt.close()
    deaths_data = {year: deaths_by_year()[year] for year in years if year in deaths_by_year()}

    x = list(deaths_data.keys())
    y = list(deaths_data.values())

    if chart_type == 'bar':
        plt.bar(x, y, color='skyblue')
        plt.xlabel('Year')
        plt.ylabel('Number of Deaths')
        plt.title('Yearly Comparisons (Bar Chart)')
    elif chart_type == 'line':
        plt.plot(x, y, marker='o', color='skyblue')
        plt.xlabel('Year')
        plt.ylabel('Number of Deaths')
        plt.title('Yearly Comparisons (Line Chart)')
    else:
        return("Invalid chart type. Please choose 'bar' or 'line'.")

    plt.tight_layout()  
    plt.show(block=False)
    return deaths_data

# Example
#years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
#chart_type = 'line' 

#yearly_comparisons(years, chart_type)

# -------------------------------------------------------------------------------------------------------

# Takes in list of years and chart type as input (bar or line)
# Displays the amount of deaths per race for the years given
def race_deaths_comparison(years, chart_type, death_by_race):
    plt.close()
    race_labels = ['White', 'Black', 'Asian', 'Black or African American', 'Asian/Indian', 'Other']
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'gray']
    race_deaths = {year: death_by_race(year) for year in years}
    data = {race: [race_deaths[year][race] for year in years] for race in race_labels}

    if chart_type == 'bar':
        for i, race in enumerate(race_labels):
            plt.bar(years, data[race], color=colors[i], label=race)
        plt.title('Comparison of Deaths by Race')
        plt.xlabel('Year')
        plt.ylabel('Number of Deaths')
        plt.legend()
    elif chart_type == 'line':
        for i, race in enumerate(race_labels):
            plt.plot(years, data[race], marker='o', color=colors[i], label=race)
        plt.title('Comparison of Deaths by Race')
        plt.xlabel('Year')
        plt.ylabel('Number of Deaths')
        plt.legend()
    else:
        return("Invalid chart type. Please choose 'bar' or 'line'.")

    plt.tight_layout()
    plt.show(block=False)
    return data
# Example
#years = [2012, 2013, 2016, 2020, 2021]
#chart_type = 'line' 

#race_deaths_comparison(years, chart_type)


# -------------------------------------------------------------------------------------------------------

# Takes in lowest age, highest age and chart type as input (bar or line)
# Displays the death amount for each age given in the range
def death_age_range(lowest, highest, chart_type, death_age_range):
    plt.close()
    age_data = death_age_range(lowest, highest)
    ages = list(age_data.keys())
    deaths = list(age_data.values())

    if chart_type == 'bar':
        plt.bar(ages, deaths, color='skyblue')
        plt.xlabel('Age')
        plt.ylabel('Number of Deaths')
        plt.title(f'Deaths by Age Range ({lowest}-{highest}) (Bar Chart)')
        plt.xticks(rotation=45, ha='right')
    elif chart_type == 'line':
        plt.plot(ages, deaths, marker='o', color='skyblue')
        plt.xlabel('Age')
        plt.ylabel('Number of Deaths')
        plt.title(f'Deaths by Age Range ({lowest}-{highest}) (Line Chart)')
        plt.xticks(rotation=45, ha='right')
    else:
        return("Invalid chart type. Please choose 'bar' or 'line'.")

    if highest - lowest + 1 > 25:
        for i, age in enumerate(ages):
            if i % 2 == 0:
                ages[i] = ''
    plt.xticks(range(len(ages)), ages)

    plt.tight_layout()
    plt.show(block=False)
    return age_data

# Example 
#lowest_age = 22 
#highest_age = 35
#chart_type = 'bar' 

#death_age_range(lowest_age, highest_age, chart_type)

# -------------------------------------------------------------------------------------------------------

# Takes in drug and chart type as input (bar or pie)
# Displays the distribution of deaths by gender for the specified drug type
def drug_gender_distribution(drug, chart_type, male_female_drug_usage):
    plt.close()
    data = male_female_drug_usage(drug)
    genders = list(data.keys())[1:]
    deaths = []
    for gender in genders:
        if data[gender] == 0:
            return(f"No data available for {drug}. Please try again.")
        else:
            deaths.append(data[gender])
        

    if chart_type == 'bar':
        plt.bar(genders, deaths, color=['skyblue', 'pink']) 
        plt.title(f'Deaths by Gender for {drug}')
        plt.xlabel('Gender')
        plt.ylabel('Number of Deaths')
    elif chart_type == 'pie':
        plt.pie(deaths, labels=genders, autopct='%1.1f%%', colors=['skyblue', 'pink'])
        plt.title(f'Deaths by Gender for {drug}')
    else:
        return("Invalid chart type. Please choose 'bar' or 'pie'.")

    plt.tight_layout()
    plt.show(block=False)
    return data
# Example 
#drug = 'Tramad'  
#chart_type = 'pie' 

#drug_gender_distribution(drug, chart_type)

# -------------------------------------------------------------------------------------------------------

# Takes in year and chart type as input (bar or pie)
# Displays the distribution of drug amount for the year given
def drug_distribution_by_year(year, chart_type, drug_distribution_by_year):
    plt.close()
    drug_data = drug_distribution_by_year(year)
    
    drugs = list(drug_data.keys())[:-1]  
    percentages = [drug_data[drug][1] for drug in drugs]
    
    threshold = 2.0  
    other_percentage = sum(p for p in percentages if p < threshold)
    other_drugs = [drug for drug, p in zip(drugs, percentages) if p < threshold]

    drugs = [drug for drug in drugs if drug not in other_drugs]
    percentages = [p for p in percentages if p >= threshold]
    drugs.append('Other')
    percentages.append(other_percentage)
    
    if chart_type == 'bar':
        plt.figure(figsize=(10, 6))
        plt.bar(drugs, percentages, color='skyblue')
        plt.title(f'Drug Distribution for Year {year} (Bar Chart)')
        plt.xlabel('Drug')
        plt.ylabel('Percentage of Deaths (%)')
        plt.xticks(rotation=45, ha='right')
    elif chart_type == 'pie':
        labels = [drug if p >= threshold else 'Other' for drug, p in zip(drugs, percentages)]
        other_percentage = sum(p for p, drug in zip(percentages, labels) if drug == 'Other')
        percentages = [p for p, drug in zip(percentages, labels) if drug != 'Other']
        labels = [drug for drug in labels if drug != 'Other']
        labels.append('Other')
        percentages.append(other_percentage)
        
        plt.figure(figsize=(8, 8))
        plt.pie(percentages, labels=labels, autopct='%1.1f%%', colors=plt.cm.tab20.colors)
        plt.title(f'Drug Distribution for Year {year} (Pie Chart)')
    else:
        return("Invalid chart type. Please choose 'bar' or 'pie'.")
    
    plt.tight_layout()
    plt.show(block=False)
    return drug_data
# Example 
#year = 2019 
#chart_type = 'bar'  
#drug_distribution_by_year(year, chart_type)





