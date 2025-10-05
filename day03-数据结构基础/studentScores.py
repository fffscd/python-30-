# 初始化学生成绩表（dict: 学生名 -> 分数）
scores = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "张八": 90
}
# 1. 添加或更新学生成绩
def add_or_upd_students(name, score):
   scores[name] = score;
   print(f"已更新 {name} 的成绩为 {score} 分。")

 
# 2. 查询学生的成绩
def query_by_name(name):
    return scores[name];

# 3. 删除学生成绩
def delete_by_name(name):
    if name in scores:
        del scores[name];
        print(f"delete {name} 's score");
    else:
        print(f"cannot find {name} 's score");

# 4. 查看所有学生成绩
def show_all():
    for name, score in scores:
         print(f"{name}: {score}");

# 5. 计算平均成绩
def average_score():
    if scores:
        avg = sum(scores.values()) / len(scores)
        print(f"班级平均分：{avg:.2f}")
    else:
        print("当前无成绩记录。")

# 示例调用
add_or_upd_students("赵六", 88)
print(query_by_name("李四"))
delete_by_name("王五")
show_all()
average_score()
    