import json
import matplotlib.pyplot as plt

def openReadJson():
    with open('internetdata.json', 'r') as file:
        data = json.load(file)
    return data

def splitByIncome(data):
    below = []
    atOrAbove = []

    for country in data:
        income = country["incomeperperson"]

        if income is None:
            continue

        if income < 10000:
            below.append(country)

        else:
            atOrAbove.append(country)

    return below, atOrAbove

def internetUsage(countries):
    usage = []
    for country in countries:
        rate = country["internetuserate"]
        if rate is not None:
            usage.append(rate)
    return usage

def createHistogram():
    data = openReadJson()
    low, high = splitByIncome(data)

    lowUsage = internetUsage(low)
    highUsage = internetUsage(high)

    plt.figure()
    plt.hist(low, bins=20)
    plt.title("Internet Usage (Income < 10,000)")
    plt.xlabel("Internet Usage Rate (%)")
    plt.ylabel("Number of Countries")
    plt.savefig("hist1.png")
    plt.show()


    plt.figure()
    plt.hist(high, bins=20)
    plt.title("Internet Usage (Income >= 10,000)")
    plt.xlabel("Internet Usage Rate (%)")
    plt.ylabel("Number of Countries")
    plt.savefig("hist2.png")
    plt.show()

def main():
    createHistogram()
    
    






