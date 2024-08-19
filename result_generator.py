import webbrowser
import shutil
from datetime import datetime
import os

def replace_content_in_html(placeholder, new_content):
    # 读取HTML文件内容
    with open(new_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # 替换占位符内容mnb
    updated_html_content = html_content.replace(placeholder, new_content)
    
    # 将更新后的内容写回HTML文件
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_html_content)


print("欢迎使用问卷星答题结果生成器!    --BY:icer233\n\n")

# 初始化生成结果文件夹
folder_name = "results"
path = "./" + folder_name
os.makedirs(path, exist_ok=True)

# 复制新文件用于修改

source_file_path = './source_file/wjx_exam_result_page.html' 
# 获取当前日期及时间
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
# 生成新文件路径
new_file_name = f"{source_file_path.split('.')[0]}_{current_time}.html"
new_file_path = "./results/" + new_file_name
# 复制原HTML文件
shutil.copy(source_file_path, new_file_path)


placeholder_text = ['PLACEHOLDER_TITLE', 'PLACEHOLDER_NAME', 'PLACEHOLDER_SUM_PROBLEMS', 'PLACEHOLDER_CORRECT_PROBLEMS', 'PLACEHOLDER_SUM_SCORE', 'PLACEHOLDER_YOUR_SCORE']  # 替换为HTML文件中的占位符
request_text = ['试卷标题', '答题人', '总题数', '正确的题数', '总分', '得分'] # 提示语内容


for i in range(0,6):
    new_text = input("请输入%s: " % request_text[i])  # 获取用户输入的新内容
    replace_content_in_html(placeholder_text[i], new_text) # 替换

# 打开更新后的HTML文件
os.chdir("./results")
webbrowser.open(new_file_name)
