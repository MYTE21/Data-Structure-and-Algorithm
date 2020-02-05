def needed_horse_shoes(shoes):
    unique_shoes = set(shoes)
    return len(shoes) - len(unique_shoes)

if __name__ == '__main__':
    shoes = list(int(num) for num in input().strip().split())[:4]
    needed_shoes_to_buy = needed_horse_shoes(shoes)
    print(needed_shoes_to_buy)
    