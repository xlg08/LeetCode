def containsNearbyDuplicate(nums, k):
    last = {}
    for i, v in enumerate(nums):
        if v in last and i - last[v] <= k:
            return True
        last[v] = i
    return False

if __name__ == '__main__':

    nums = [1, 2, 3, 1, 2, 3]
    k = 2

    print(containsNearbyDuplicate(nums, k))

    nums = [1, 0, 1, 1]
    k = 1
    print(containsNearbyDuplicate(nums, k))
