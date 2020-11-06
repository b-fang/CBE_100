
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

def problem2():
    reading = np.array([10, 28, 48, 65, 81, 90])
    C = np.array([0.30, 0.85, 2.67, 7.31, 18.2, 30.0])

    m, b = np.polyfit(np.log(C), reading, 1)
    x = np.linspace(0, 30, 1000)
    plt.figure(1)
    plt.scatter(C, reading)
    plt.plot(x, m * np.log(x) + b)
    plt.xlabel("C (g SO2/m^3 gas)")
    plt.ylabel("Reading (0-100 scale)")
    plt.xlim(0, 30)
    plt.ylim(0,100)
    plt.title("Calibration Curve of S02 Analyzer Data")
    plt.legend(["Reading = {:.5g}*ln(C) + {:.5g}".format(m, np.abs(b))])
    plt.savefig("HW3/CBE100_HW3_Outputs/Problem 2")
