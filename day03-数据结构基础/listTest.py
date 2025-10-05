# 创建列表
nums = [10, 20, 30, 40, 50]

print(nums[2]);

nums.append(34);

# 删除元素
nums.remove(30)

# 修改元素
nums[1] = 25


# 切片操作
print(nums[1:4])     # [25, 40, 50]

# 求和与平均值
total = sum(nums)
avg = total / len(nums)
print(f"总和={total}, 平均值={avg:.2f}")