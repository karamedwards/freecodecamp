import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv(r"C:\Users\kme80\OneDrive - ACS\Documents\VS Code\Data Analysis with Python Course\Sea Level Predictor\epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regress = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    slope = regress[0]
    intercept = regress[1]
    x = np.arange(1880, 2051, 1)
    y = slope*x + intercept
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    plt.plot(x,y)
    
    # Create second line of best fit
    regress2 = linregress(x=df.loc[df['Year']>=2000]['Year'],y=df.loc[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    slope2 = regress2[0]
    slope2 = regress2[0]
    intercept2 = regress2[1]
    x2 = np.arange(2000, 2051, 1)
    y2 = slope2*x2 + intercept2
    
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    plt.plot(x,y)
    plt.plot(x2,y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()