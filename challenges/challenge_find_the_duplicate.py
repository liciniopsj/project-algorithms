def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    visitedNums = set()
    for num in nums:
        if not isinstance(num, int) or num < 1 or num > len(nums) - 1:
            return False
        if num in visitedNums:
            return num
        visitedNums.add(num)

    return False




print(find_duplicate([-1, 0, 0, 1, 4, 5, 8]))
