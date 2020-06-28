import math

def running_median_easy(items):
    size = len(items)
    items = sorted(items)
    if size % 2 == 1:
        mid = math.floor(size/2)
        median = items[mid]
    else:
        mid = math.floor(size/2)
        median = (items[mid-1]+items[mid])/2
    return median

if __name__ == "__main__":
    print("<--- Find Median --->")
    my_list = []
    while True:
        option = int(input("Enter an operation (1 to enter number, 2 to exit) : "))
        if option == 1:
            num = int(input("Enter a number : "))
            my_list.append(num)
            ans = running_median_easy(my_list)
            print("Median : ", ans)
        elif option == 2:
            print("Process ends ...!")
            break
        else:
            print("Try again...!")
