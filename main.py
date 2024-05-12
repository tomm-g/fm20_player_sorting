import pandas as pd
import numpy as np
import sys
from lib import data_cleaning

dataFile = 'datafm20.csv'

df = pd.read_csv(dataFile)

df = df.drop(columns='Unnamed: 0')

if __name__ == "__main__":

    print(len(sys.argv))

    if sys.argv == 4:

        position = sys.argv[1]
        high_wage = float(sys.argv[2])
        low_wage = float(sys.argv[3])

    else:

        position = " "
        high_wage = float(sys.argv[1])
        low_wage = float(sys.argv[2])

    print(f"Position: {position}")
    print(f"high_wage: {high_wage}")
    print(f"low_wage: {low_wage}")

    selected_players = data_cleaning.find_player(position, high_wage, low_wage, df)

    selected_players = selected_players.iloc[:50]
    print(selected_players) 

    output_file = "selected_players.csv"
    selected_players.to_csv(output_file)
    print(f"Player info written to file: {output_file}")


