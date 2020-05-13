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


x1 = "vafouskos"
x1.format()
x2 = str("vafousk").capitalize()
x4 = "karolos"

xx5 = MyString(x4).capitalize()
print(xx5)
