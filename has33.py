# Wrong
from MyString import MyString


def has_331(nums):
    for i in range(len(nums) - 1):
        return nums[i] == 3 and nums[i + 1] == 3


# Right
def has_332(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    else:
        return False


print(has_332([1,3,3]))

