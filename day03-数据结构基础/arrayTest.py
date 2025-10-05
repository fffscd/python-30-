from array import array

nums = array('i', [10, 20, 30, 40, 50])

# 访问与修改与 list 类似
print(nums[0])        # 10
nums.append(60)
nums.remove(30)
nums[1] = 25

# 求和
print(sum(nums))
