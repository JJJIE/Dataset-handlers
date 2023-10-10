import os
import pickle

# 指定文件夹路径
dir_path = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/id_list'

# 获取文件夹中的所有文件
all_files = os.listdir(dir_path)

# 从每个文件名中去除文件扩展名，并保存到列表中

file_names_without_ext = [os.path.splitext(file)[0] for file in all_files if file.endswith('.pkl')]

# 只取前300个文件名
file_names_without_ext = file_names_without_ext[:300]

# 将列表保存为.pkl文件
output_path = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/test_list.pkl'
with open(output_path, 'wb') as f:
    pickle.dump(file_names_without_ext, f)

# 测试：读取并打印保存的列表
with open(output_path, 'rb') as f:
    data = pickle.load(f)
    print(data)
