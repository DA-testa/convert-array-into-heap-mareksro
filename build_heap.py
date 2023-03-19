# python3

from heapq import heapify


def build_heap(data):
    n=len(data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n // 2,-1,-1):
        heapify(data,i, swaps)

    return swaps

def heapify(data,i, swaps):
    n=len(data)
    kreisais = 2*i +1
    labais = 2*i+2
    min = i
    if kreisais < n and data[kreisais]<data[min]:
        min = kreisais
    if labais < n and data[labais]<data[min]:
        min = labais
    if  i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i,min))
        heapify(data,min,swaps)



def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    text = input()

    #if text not in ["I", "F"]:
       # print("invalid input")
       # return
    if "I" in text:
    # input from keyboard
        try:
            n = int(input())
            data = list(map(int, input().split()))
            
        except:
            print()
            return
    elif "F" in text:
        fails = input()
    try:
        #if "a" in fails:
            #print("wrong file name")
            #return
        with open("./test/" + fails, "r") as f:
                n=int(f.readline())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
    except FileNotFoundError:
            print("not found")
            return
    except:
            print("invaild format")
            return
        

    
    # checks if lenght of data is the same as the said lenght
    if len(data) != n:
        print("invalid data")
        return
    # calls function to assess the data 

    # and give back all swaps
    swaps = build_heap(data)

    if len(swaps) > 4 * len(data):
        print ("out of bound")
        return
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
