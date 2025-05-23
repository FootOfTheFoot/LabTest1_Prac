def avgTemp(arr):
    total=0
    for element in arr: 
        total+=element
    return total/len(arr)

def getTemp():
    arr=[]
    arrSize=int(input("Enter array size: "))
    for i in range (arrSize):
        temp=int(input("Enter element: "))
        arr.append(temp)
    return arr

def getTempArr():
    tempArr=[]
    arrString=input("Enter temp values. E.g. 3,6,8,9,22: ")
    tempArrString=arrString.split(",")
    for x in tempArrString:
        tempArr.append(int(x))
    return tempArr

def main():
    tempArr=[]
    choice=input("1 for indiv input, 2 for one shot input: ")
    if choice=="1":
        tempArr=getTemp()
        avg=avgTemp(tempArr)
        print("The average temp is",avg)
    elif choice=="2":
        tempArr=getTempArr()
        avg=avgTemp(tempArr)
        print("The average temp is",avg)
    else:
        print("Invalid input")
    

if __name__=='__main__':
    main()
