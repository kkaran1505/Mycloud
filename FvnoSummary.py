import numpy as np
if __name__== "__main__":
    dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 12, 14, 17, 19, 10, 13, 12, 14, 12, 12, 11, 14, 13, 15, 10, 15, 12,
               10,14, 13, 15, 10]
    dataset = sorted(dataset)
    print("Sorted data :", dataset)
    print("5 Number Summary ")

def Five_No_Summary(data):
    min_value= min(data)
    print("Minimum Value = ", min_value)
    q1,q2,q3= np.percentile(data,[25,50,75])
    print("Lower Quartile= ",q1)
    print("Median= ",q2)
    print("Upper Quartile= ",q3)
    max_value= max(data)
    print("Maximum Value= ", max_value)
    return
if __name__== "__main__":
    Five_No_Summary(dataset)