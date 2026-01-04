import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import the data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5, label='Original Data')

    # 3. Create first line of best fit (using all data)
    # Get slope and intercept
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 1880 to 2050 for prediction
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    # Calculate y values: y = mx + c
    line_all = res_all.slope * years_extended + res_all.intercept
    plt.plot(years_extended, line_all, 'r', label='Best Fit Line 1880-2050')

    # 4. Create second line of best fit (using data from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create array of years from 2000 to 2050
    years_recent_ext = pd.Series([i for i in range(2000, 2051)])
    
    # Calculate y values for the second line
    line_recent = res_recent.slope * years_recent_ext + res_recent.intercept
    plt.plot(years_recent_ext, line_recent, 'green', label='Best Fit Line 2000-2050')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()