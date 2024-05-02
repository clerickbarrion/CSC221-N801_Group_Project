import tkinter as tk
import tkinter.simpledialog as simpledialog
import modules.visualization as visualization
import modules.stats as stats

MIN_YEAR = 2012
MAX_YEAR = 2022


class DrugStatsGUI:

  def __init__(self):
    self.window = tk.Tk()
    self.window.grab_set()
    self.window.title("CT Accidental Drug Deaths Data Analysis")
    self.window.geometry("800x800")
    self.window.configure(bg="light blue")

    self.title_frame = tk.Frame(self.window)
    self.title_frame.pack()

    self.title_label = tk.Label(self.title_frame,
                                text="CT Accidental Drug Deaths Data Analysis",
                                bg="lightblue",
                                font="arial 20")
    self.title_label.pack()
    # -------------------------------------------------------------------------------------------------------
    self.menu_frame = tk.Frame(self.window, bg="lightblue")
    self.menu_frame.pack(pady=5)

    self.deaths_by_year_button = tk.Button(self.menu_frame,
                                           text="Deaths by Year",
                                           command=self.deaths_by_year,
                                           font="arial 12")
    self.deaths_by_year_button.pack(pady=5)

    self.drug_distribution_by_year_button = tk.Button(
        self.menu_frame,
        text="Drug Distribution by Year",
        command=self.drug_distribution_by_year,
        font="arial 12")
    self.drug_distribution_by_year_button.pack(pady=5)

    self.drug_distribution_by_year_button = tk.Button(
        self.menu_frame,
        text="Death By Age Range",
        command=self.death_by_age_range,
        font="arial 12")
    self.drug_distribution_by_year_button.pack(pady=5)

    self.death_by_race_button = tk.Button(self.menu_frame,
                                          text="Death By Race",
                                          command=self.death_by_race,
                                          font="arial 12")
    self.death_by_race_button.pack(pady=5)

    self.drug_gender_distribution_button = tk.Button(
        self.menu_frame,
        text="Drug Gender Distribution",
        command=self.drug_gender_distribution,
        font="arial 12")
    self.drug_gender_distribution_button.pack(pady=5)

    self.quit_button = tk.Button(self.menu_frame,
                                 text="Quit",
                                 command=self.window.quit,
                                 font="arial 12")
    self.quit_button.pack(pady=10)
    # -------------------------------------------------------------------------------------------------------
    self.data_frame = tk.Frame(self.window, bg="lightblue")
    self.data_frame.pack()

    self.data_label = tk.Label(self.data_frame,
                               text="Data will be displayed below:",
                               bg="lightblue",
                               font="arial 16")
    self.data_label.pack()

    self.data_text = tk.Label(self.data_frame,
                              wraplength=800,
                              justify="left",
                              anchor="w",
                              bg="lightblue")
    self.data_text.pack()

    tk.mainloop()

  def deaths_by_year(self):

    start_year = simpledialog.askinteger("Year",
                                         "Enter start year:",
                                         minvalue=MIN_YEAR,
                                         maxvalue=MAX_YEAR,
                                         parent=self.window)
    end_year = simpledialog.askinteger("Year",
                                       "Enter end year:",
                                       minvalue=MIN_YEAR,
                                       maxvalue=MAX_YEAR,
                                       parent=self.window)
    years = list(range(start_year, end_year + 1))

    chart_list = ["bar", "line"]
    chart_type = simpledialog.askinteger(
        "Chart Type",
        "Enter a chart type:\n0-Bar\n1-Line\n",
        minvalue=0,
        maxvalue=1,
        parent=self.window)

    data = visualization.yearly_comparisons(years, chart_list[chart_type],
                                            stats.deaths_by_year)
    data_formatted = "Year\tDeaths"
    for year, deaths in data.items():
      data_formatted += f"\n{year}\t{deaths}"

    self.data_text.config(text=data_formatted)

  def drug_distribution_by_year(self):

    year = simpledialog.askinteger("Year",
                                   "Enter a year:",
                                   minvalue=MIN_YEAR,
                                   maxvalue=MAX_YEAR,
                                   parent=self.window)

    chart_list = ["bar", "pie"]
    chart_type = simpledialog.askinteger("Chart Type",
                                         "Enter a chart type:\n0-Bar\n1-Pie\n",
                                         minvalue=0,
                                         maxvalue=1,
                                         parent=self.window)

    data = visualization.drug_distribution_by_year(
        year, chart_list[chart_type], stats.drug_distribution_by_year)

    data_formatted = "Drug\tTotal\tPercentage"
    for drug, totals in data.items():
      if drug == "Total":
        data_formatted += f"\n{drug}\t{totals}\t100%"
      else:
        data_formatted += f"\n{drug[:7]}\t{totals[0]}\t{totals[1]}%"

    self.data_text.config(text=data_formatted)

  def death_by_age_range(self):

    lowest = simpledialog.askinteger("Lowest Age",
                                     "Enter the lowest age:",
                                     minvalue=0,
                                     maxvalue=87,
                                     parent=self.window)

    highest = simpledialog.askinteger("Highest Age",
                                      "Enter the highest age:",
                                      minvalue=0,
                                      maxvalue=87,
                                      parent=self.window)

    chart_list = ["bar", "line"]
    chart_type = simpledialog.askinteger(
        "Chart Type",
        "Enter a chart type:\n0-Bar\n1-Line\n",
        minvalue=0,
        maxvalue=1,
        parent=self.window)

    data = visualization.death_age_range(lowest, highest,
                                         chart_list[chart_type],
                                         stats.death_age_range)

    data_formatted = "Age: Deaths\n\n"
    count = 1
    for age, deaths in data.items():
      if count % 5 == 0:
        data_formatted += "\n"
      data_formatted += f"{age}: {deaths} | "
      count +=1

    self.data_text.config(text=data_formatted)

  def death_by_race(self):

    start_year = simpledialog.askinteger("Year",
                                         "Enter start year:",
                                         minvalue=MIN_YEAR,
                                         maxvalue=MAX_YEAR,
                                         parent=self.window)
    end_year = simpledialog.askinteger("Year",
                                       "Enter end year:",
                                       minvalue=MIN_YEAR,
                                       maxvalue=MAX_YEAR,
                                       parent=self.window)

    years = list(range(start_year, end_year + 1))

    chart_list = ["bar", "line"]
    chart_type = simpledialog.askinteger(
        "Chart Type",
        "Enter a chart type:\n0-Bar\n1-Line\n",
        minvalue=0,
        maxvalue=1,
        parent=self.window)

    data = visualization.race_deaths_comparison(years, chart_list[chart_type],
                                                stats.death_by_race)
    
    data_formatted = "Race"

    for i in years:
      data_formatted += f"\t{i}"
    for race, deaths in data.items():
      data_formatted += f"\n{race[:8]}"
      for i in deaths:
        data_formatted += f"\t{i}"
    
    self.data_text.config(text=data_formatted)

  def drug_gender_distribution(self):

    drug_list = [
        "Alcohol", "Heroin", "Cocaine", "Fentanyl", "Oxycodone", "Ethanol",
        "Hydrocodone", "Benzodiazepine", "Methadone", "Amphet", "Tramad",
        "Morphine", "Xylazine", "Gabapentin"
    ]

    drug = simpledialog.askinteger("Drug",
                                   """Enter a drug:\n
        0-Alcohol\n
        1-Heroin\n
        2-Cocaine\n
        3-Fentanyl\n
        4-Oxycodone\n
        5-Oxymorphone\n
        6-Ethanol\n
        7-Hydrocodone\n
        8-Benzodiazepine\n
        9-Methadone\n
        10-Amphet\n
        11-Tramad\n
        12-Morphine\n
        13-Xylazine\n
        14-Gabapentin\n""",
                                   minvalue=0,
                                   maxvalue=14,
                                   parent=self.window)

    chart_list = ["bar", "pie"]
    chart_type = simpledialog.askinteger("Chart Type",
                                         "Enter a chart type:\n0-Bar\n1-Pie",
                                         minvalue=0,
                                         maxvalue=1,
                                         parent=self.window)

    data = visualization.drug_gender_distribution(drug_list[drug],
                                                  chart_list[chart_type],
                                                  stats.male_female_drug_usage)

    total = data["Male"] + data["Female"]
    data_formatted = ""
    for key, value in data.items():
      if key == "Male" or key == "Female":
        data_formatted += f"{key}: {value}, {round((value/total)*100, 2)}%\n"
      else:
        data_formatted += f"{key}: {value}\n"
    data_formatted += f"Total: {total}"

    self.data_text.config(text=data_formatted)


if __name__ == "__main__":
  DrugStatsGUI()
