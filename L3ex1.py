import math
import statistics as st
def main():
    temp=[]
    templist=[]
    min_max=[]
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    bmi=calculate_bmi(weight=57, height=1.73)
    bmi_range(bmi)
    



def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/math.pow(height,2)
    print(f"BMI: {bmi:.2f}")
    if bmi>25:
        return 1
    elif 18.5<=bmi<=25:
        return 0
    else:
        return -1

def bmi_range(bmi):
    if bmi==1:
        print("Over Weight")
    elif bmi==0:
        print("Normal Weight")
    else:
        print("Under Weight")


if __name__=='__main__':
    main()