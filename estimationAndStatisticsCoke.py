import numpy as np
from sklearn.linear_model import LinearRegression
# This code contains functions that calculates the mean and variance of a list of data
# It also contains a function that uses least squares estimation to estimate a future value for a list of data with a list of corresponding years


def mean(values):
    # Calculate the mean value in the given timespan
    valuesNpArray = np.array(values)
    meanAnswer = sum(valuesNpArray) / len(valuesNpArray)
    return meanAnswer


def variance(values):
    # Calculate the variance
    valuesNpArray = np.array(values)
    meanValue = sum(valuesNpArray) / len(valuesNpArray)
    sumDeviationSquared = 0
    for price in valuesNpArray:
        sumDeviationSquared += (price - meanValue) ** 2
    varianceAnswer = sumDeviationSquared / (len(valuesNpArray) - 1)
    return varianceAnswer


def leastSquaresEstimate(years, prices, futureYear):
    # Using the least squares method to estimate a price for a future year (year chosen by the user)
    yearsNpArray = np.array(years)
    pricesNpArray = np.array(prices)
    model = LinearRegression().fit(yearsNpArray.reshape(-1, 1), pricesNpArray)
    # Error handling if the input of the future year is not a number
    if not type(futureYear) is int:
        raise ValueError("Enter a future year using digits only")
    # Error handling if the input of the future year is not a year in the future
    if futureYear < 2025:
        raise ValueError("Please enter the future year as 2025 or a later year")
    futurePrice = model.predict([[futureYear]])[0]
    return futurePrice
