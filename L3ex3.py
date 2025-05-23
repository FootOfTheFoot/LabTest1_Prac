import math
import statistics as st
def main():
    temp=[]
    templist=[]
    min_max=[]
    value=display_main_menu()
    templist=get_user_input(value)
    print(templist)
    avg=calc_average(templist)
    print(f"Average temperature: {avg}")
    min_max=find_min_max(templist)
    print("Minimum temperature:",min_max[0],"\nMaximum temperature:",min_max[1])
    temp=sort_temperature(templist)
    print(f"Sorted temperature list: {temp}")
    median=calc_median_temperature(temp)
    print(f"Median temperature: {median:.2f}")


def display_main_menu():
    value=input(f"Enter some numbers separated by commas (e.g. 5, 67, 32)")
    return value

def get_user_input(value):
    temp=[]
    temp=value.split(",")
    temp_list=[float(item) for item in temp]
    return temp_list

def calc_average(templist):
    sum=0
    for num in templist:
        sum+=num
    avg=sum/(len(templist))
    return avg
    
def find_min_max(templist):
    max=templist[0]
    min=templist[0]
    for num in templist:
        if num>max:
            max=num
        elif num<min:
            min=num
    return [min,max]

def sort_temperature(templist):
    sorted_templist = sorted(templist)
    return sorted_templist

def calc_median_temperature(sorted_templist):
    median=st.median(sorted_templist)
    return median




if __name__=='__main__':
    main()