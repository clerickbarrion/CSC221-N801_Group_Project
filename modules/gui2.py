
import tkinter as tk
import tkinter.simpledialog as simpledialog
import modules.visualization as visualization
import modules.stats as stats

MIN_YEAR = 2012
MAX_YEAR = 2022

class DrugStatsGUI:   
        
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CT Accidental Drug Deaths Data Analysis")
        self.window.geometry("800x600")
        self.window.configure(bg="light blue")

        self.title_frame = tk.Frame(self.window)
        self.title_frame.pack()

        self.title_label = tk.Label(self.title_frame, text="CT Accidental Drug Deaths Data Analysis", bg="lightblue", font="arial 20")
        self.title_label.pack()
# -------------------------------------------------------------------------------------------------------
        self.menu_frame = tk.Frame(self.window, bg="lightblue")
        self.menu_frame.pack(pady= 5)
        
        self.deaths_by_year_button = tk.Button(self.menu_frame, text="Deaths by Year", command=self.deaths_by_year, font="arial 12")
        self.deaths_by_year_button.pack(pady= 5)

        self.drug_distribution_by_year_button = tk.Button(self.menu_frame, text="Drug Distribution by Year", command=self.drug_distribution_by_year, font="arial 12")
        self.drug_distribution_by_year_button.pack(pady= 5)

        self.drug_distribution_by_year_button = tk.Button(self.menu_frame, text="Death By Age Range", command=self.death_by_age_range, font="arial 12")
        self.drug_distribution_by_year_button.pack(pady= 5)

        self.death_by_race_button = tk.Button(self.menu_frame , text="Death By Race", command=self.death_by_race, font="arial 12")
        self.death_by_race_button.pack(pady= 5)

        self.drug_gender_distribution_button = tk.Button(self.menu_frame, text="Drug Gender Distribution", command=self.drug_gender_distribution, font="arial 12")
        self.drug_gender_distribution_button.pack(pady= 5)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.window.quit, font="arial 12")
        self.quit_button.pack(pady= 10)
# -------------------------------------------------------------------------------------------------------
        self.data_frame = tk.Frame(self.window, bg="lightblue")
        self.data_frame.pack()

        self.data_label = tk.Label(self.data_frame, text="Data will be displayed below:", bg="lightblue", font="arial 16")
        self.data_label.pack()

        self.data_text = tk.Label(self.data_frame, wraplength=200, justify="left", anchor="w", bg="lightblue")
        self.data_text.pack()
    
        tk.mainloop()   
    
    def deaths_by_year(self):

        start_year = simpledialog.askinteger("Year", "Enter start year:")
        end_year = simpledialog.askinteger("Year", "Enter end year:")
        years = list(range(start_year, end_year+1))

        chart_type = simpledialog.askstring("Chart Type", "Enter a chart type (bar or pie):")

        data = visualization.yearly_comparisons(years, chart_type, stats.deaths_by_year)
        self.data_text.config(text=data)
    def drug_distribution_by_year(self):

        year = simpledialog.askinteger("Year", "Enter a year:")

        chart_type = simpledialog.askstring("Chart Type", "Enter a chart type (bar or pie):")

        data = visualization.drug_distribution_by_year(year, chart_type, stats.drug_distribution_by_year)
        self.data_text.config(text=data)
    def death_by_age_range(self):

        lowest = simpledialog.askinteger("Lowest Age", "Enter the lowest age:")

        highest = simpledialog.askinteger("Highest Age", "Enter the highest age:")

        chart_type = simpledialog.askstring("Chart Type", "Enter a chart type (bar or line):")

        data = visualization.death_age_range(lowest, highest, chart_type, stats.death_age_range)
        self.data_text.config(text=data)
    def death_by_race(self):

        start_year = simpledialog.askinteger("Year", "Enter start year:")
        end_year = simpledialog.askinteger("Year", "Enter end year:")
        years = list(range(start_year, end_year+1))

        chart_type = simpledialog.askstring("Chart Type", "Enter a chart type (bar or line):")

        data = visualization.race_deaths_comparison(years, chart_type, stats.death_by_race)
        self.data_text.config(text=data)
    def drug_gender_distribution(self):

        drug = simpledialog.askstring("Drug", "Enter a drug:")

        chart_type = simpledialog.askstring("Chart Type", "Enter a chart type (bar or pie):")

        data = visualization.drug_gender_distribution(drug, chart_type, stats.male_female_drug_usage)
        self.data_text.config(text=data)
    
DrugStatsGUI()
