import pandas as pd

# 设置pandas的显示选项
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# 读取excel文档
df = pd.read_excel('录取.xlsx')

# 计算每个学生录取名次的波动
# df['名次波动'] = df.groupby(['学校名称', '专业名称'])['位次'].diff()
df['名次波动'] = df.groupby(['学校代号', '专业名称', df['高考年'].diff().ne(0).cumsum()])['位次'].diff()

# 找出名次波动超过5000的项
result = df[df['名次波动'].abs() > 5000]

# 输出结果
print(result)
result.to_excel('名次波动.xlsx', index=False)