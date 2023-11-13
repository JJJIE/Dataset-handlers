import pickle

# 加载 pkl 文件
with open('test_list.pkl', 'rb') as f:
    data = pickle.load(f)

# 检查数据类型是否为列表
if isinstance(data, list):
    for item in data:
        print(item)
else:
    print("Loaded data is not a list. It's a:", type(data))
