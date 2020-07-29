def max_distance_easy(array):
    nums = []

    for i, num in enumerate(array):
        nums.append((num, i))
    nums.sort()

    max_gap = 0
    min_num = nums[0][1]

    for items in nums:
        num = items[1]
        if num <= min_num:
            min_num = num
        else:
            max_gap = max(max_gap, num - min_num)

    return max_gap


if __name__ == "__main__":
    numbers = [3, 5, 4, 2]
    ans = max_distance_easy(numbers)
    print("One : ", ans)

    numbers = [5, 4, 3, 2]
    ans = max_distance_easy(numbers)
    print("Two : ", ans)
