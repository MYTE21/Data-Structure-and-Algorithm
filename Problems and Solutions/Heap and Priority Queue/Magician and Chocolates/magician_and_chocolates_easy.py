def max_index(numbers):
    return numbers.index(max(numbers))


def magician_and_chocolates_easy(box, taken_time):
    chocolates = 0
    while taken_time != 0:
        large_box = max_index(box)
        chocolates = chocolates + box[large_box]
        if boxes[large_box] == 0:
            break
        box[large_box] = float(box[large_box]/2)
        taken_time = taken_time - 1
    return chocolates


if __name__ == "__main__":
    box_number = int(input("Enter the total box number : "))  # 2
    print("Enter the chocolates number of ", box_number, " boxes : ")
    boxes = list(int(num) for num in input().strip().split())[:box_number]  # [6, 5]
    total_taken = int(input("Enter the taken number : "))  # 3
    ans = magician_and_chocolates_easy(boxes, total_taken)  # 14
    print("Ans : ", int(ans))

