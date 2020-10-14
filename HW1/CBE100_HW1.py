
import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def problem3():
    temperature = 50.0
    temperatureUncertainty = 0.05

    rho = np.array([0.98803, 0.98984, 0.99148, 0.99297, 0.99439, 0.99580])
    massRatio = np.array([0.0000, 0.8821, 1.7683, 2.6412, 3.4093, 4.2064])

    m, b = np.polyfit(rho, massRatio, 1)
    plt.figure(1)
    plt.scatter(rho, massRatio)
    plt.plot(rho, m*rho+b)
    plt.xlabel("density (g solution/cm^3)")
    plt.ylabel("mass ratio (g Ile/100 g H20)")
    plt.title("Calibration Curve of Aqueous Solutions of Amino acid L-isoleucine")
    plt.legend(["mass ratio = {:.5g}*rho - {:.5g}".format(m, np.abs(b))])
    print(0.9940*m+b)
    plt.savefig("HW1/CBE100_HW1_Outputs/Problem 3")


def problem4():
    time = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    biomass = np.array([0.01, 0.013, 0.04, 0.05, 0.38, 0.7, 0.85, 1.6])
    biomassLn = np.log(biomass)

    m, b = np.polyfit(time, biomassLn, 1)
    plt.figure(2)
    plt.scatter(time, biomassLn)
    plt.plot(time, m * time + b)
    plt.legend(["log(biomass) = {:.5}*time - {:.5g}".format(m, np.abs(b))])
    plt.title("Semi-log Biomass (g/L) vs Time (hrs)")
    plt.ylabel("Biomass (g/L)")
    plt.xlabel("Time (hrs)")
    plt.savefig("HW1/CBE100_HW1_Outputs/Problem 4")


def problem5():
    week = np.array([1, 2, 3, 4, 5, 6])
    demand = np.array([2385, 1890, 1506, 1196, 950, 755])
    demandLn = np.log(demand)

    m, b = np.polyfit(week, demandLn, 1)
    plt.figure(3)
    plt.scatter(week, demandLn)
    plt.plot(week, m * week + b)
    plt.legend(["log(demand rate) = {:.5g}*week + {:.5g}".format(m, np.abs(b))])
    plt.title("Semi-log Projected Demand Figures over Time")
    plt.ylabel("Demand Rate (kg/wk)")
    plt.xlabel("Time (weeks)")
    plt.savefig("HW1/CBE100_HW1_Outputs/Problem 5")
