def containduplicate(nums:list[int]):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

nums = [1,2,3,4]
print(containduplicate(nums))