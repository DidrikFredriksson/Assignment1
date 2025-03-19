import numpy as np
from sklearn.linear_model import LinearRegression

def mean(values):
    #Calculate the mean value in the given timespan
    return sum(values) / len(values)

def variance(values):
    #calculate the variance
    meanValue = sum(values) / len(values)
    sumDeviationSquared = 0
    for price in values:
        sumDeviationSquared += (price - meanValue) ** 2
    return sumDeviationSquared / (len(values) - 1)

def leastSquaresEstimate(years, prices):
    #Using the least squares method to estimate a price for a future year (year chosen by the user)
    model = LinearRegression().fit(years.reshape(-1, 1), prices)
    #Error handling if the input of a year is not a number
    while True:
        try:
            future_year = int(input("Enter a future year to estimate the price of a can of Coke then: "))
            break
        except ValueError:
            print("That is not a valid year, try again with numbers")
    return model.predict([[future_year]])[0], future_year

def main():
    #Data for prices of a can of Coke (in Kronor) and corresponding years as numpy arrays
    prices = np.array([8.4, 9.0, 9.4, 9.8, 10.2])
    years = np.array([2016, 2018, 2020, 2022, 2024])
    
    #Using the least squares method to estimate a future price for a can of Coke
    leastSquareAns = leastSquaresEstimate(years, prices)
    
    #Printing the data for the price of a can of Coke
    print("\nMean price: " + str(round(mean(prices), 2)) + " Kr")
    print("Variance of price: " + str(round(variance(prices), 4)))
    print("Estimated price in " + str(leastSquareAns[1]) + " (using Least squares method): " + str(round(leastSquareAns[0], 2)) + " Kr")
main()