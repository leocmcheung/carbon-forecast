import pandas as pd
import numpy as np


def show_sector():
    """
    To help with initial data filtering on Historical Emission csv
    """
    sector = input("Which GICS Sector?")
    print("Reading data...")
    data = pd.read_csv("../raw_data/Historical_Emissions_simp.csv")
    print("Getting rid of 2021 incomplete data...")
    data = data[data["Financial Year"] < 2021]
    print("Adding scope1&2 -> For absolute please look 'C-absolute-1+2'\n For intensity please look 'C-intensity-1+2'")
    data["C-absolute-1+2"] = data["Carbon-Scope 1 (tonnes CO2e)"] + data["Carbon-Scope 2 (tonnes CO2e)"]
    data["C-intensity-1+2"] = data["Carbon Intensity-Scope 1 (tonnes CO2e/USD mn)"] + data["Carbon Intensity-Scope 2 (tonnes CO2e/USD mn)"]
    print("Filtering by GICS Industry Name")
    data_filtered = data[data["GICS Sector Name"] == f"{sector}"]
    print("Done!")
    return data_filtered


if __name__ == '__main__':
    show_sector()
