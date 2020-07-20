def max_index(numbers):
    return numbers.index(max(numbers))


def magician_and_chocolates(boxes, taken_time):
    chocolates = 0
    while taken_time != 0:
        large_box = max_index(boxes)
        chocolates = chocolates + boxes[large_box]
        if boxes[large_box] == 0:
            break
        boxes[large_box] = float(boxes[large_box]/2)
        taken_time = taken_time - 1
    return chocolates


if __name__ == "__main__":
    ans = magician_and_chocolates([6, 5], 3)
    print("Ans :", int(ans))

