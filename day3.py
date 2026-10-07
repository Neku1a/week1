nums = [3, 5, 2]   # список
nums.append(10)    # додати в кінець -> [3,5,2,10]
print(len(nums))   # 4 - довжина
print(nums[0])     # 3 - перший елемент, рахунок з 0
for x in nums:     # пройти по всіх
    print(x)


def list_sum(nums):
    s = 0
    for x in nums:
        s = s + x
    return s
print(list_sum([1,2,3]))
def list_avg(nums):
    return list_sum(nums) / len(nums)
print(list_avg([1,2,3]))


def list_max(nums):
    m = nums[0]
    for x in nums:
        if x > m:
            m = x
    return m
print(list_max([1,2,3]))
def list_min(nums):
    m = nums[0]
    for x in nums:
        if x < m:
            m = x
    return m
print(list_min([1,2,3]))


def list_rev(nums):
    r = []
    for x in nums:
        r = [x] + r
    return r
print(list_rev([1,2,3]))


def uniq(nums):
    res = []
    for x in nums:
        if x not in res:
            res.append(x)
    return res

print(uniq([1,2,2,3,1]))