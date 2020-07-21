import heapq


def magician_and_chocolates(box, taken_time):
    max_container = []
    chocolates = 0
    for chocolate in box:
        heapq.heappush(max_container, chocolate*-1)

    for _ in range(taken_time):
        box_chocolates = heapq.heappop(max_container)*-1
        chocolates += box_chocolates
        modified_box = box_chocolates // 2
        heapq.heappush(max_container, modified_box*-1)

    return chocolates


if __name__ == "__main__":
    box_number = int(input("Enter the total box number : "))    # 2
    print("Enter the chocolates number of ", box_number, " boxes : ")
    boxes = list(int(num) for num in input().strip().split())[:box_number]  # [6, 5]
    total_taken = int(input("Enter the taken number : "))   # 3
    ans = magician_and_chocolates(boxes, total_taken)   # 14
    print("Ans : ", ans)
