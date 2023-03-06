import numpy as np
from matplotlib import pyplot as plt
dataset = [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
plt.hist(dataset)
plt.show()
#myarr=np.array([3,6,5,4,8,2,1])
#print(myarr)
outliers = []


def detect_outliers(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(i)

    return outliers
detect_outliers(dataset)
print(outliers)