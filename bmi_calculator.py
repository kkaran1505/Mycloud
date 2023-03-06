def bmi_cal(weight,height):
    bmi=weight/(height**2)
    return bmi

w=float(input("Enter weight in Kg \n"))
h=float(input("Enter height in meter \n"))

print(round(bmi_cal(w,h),2))
