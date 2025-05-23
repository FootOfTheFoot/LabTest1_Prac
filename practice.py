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

def main():
    tempArr=[]
    tempArr=getTemp()
    avg=avgTemp(tempArr)
    print("The average temp is",avg)

if __name__=='__main__':
    main()
