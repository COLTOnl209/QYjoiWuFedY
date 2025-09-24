# 代码生成时间: 2025-09-24 10:22:36
import streamlit as st
import json
import os

"""
配置文件管理器，用于加载、保存和管理配置文件。
这个程序使用STREAMLIT框架创建一个简单的Web界面，
允许用户加载和保存配置文件。
"""

# 配置文件的默认路径
DEFAULT_CONFIG_PATH = 'config.json'

# 检查配置文件是否存在
def check_config_file(path):
    """检查配置文件是否存在"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"配置文件 {path} 不存在")

# 加载配置文件
def load_config(path):
    """从指定路径加载配置文件。
    参数：
    path (str): 配置文件的路径
    返回：
    dict: 配置文件的内容
    """
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"配置文件 {path} 解析失败：{e}")

# 保存配置文件
def save_config(path, config):
    """保存配置文件到指定路径。
    参数：
    path (str): 配置文件的路径
    config (dict): 要保存的配置内容
    """
    try:
        with open(path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        raise IOError(f"保存配置文件 {path} 失败：{e}")

# STREAMLIT应用的主函数
def main():
    # 设置页面标题
    st.title('配置文件管理器')

    # 显示配置文件路径输入框
    config_path = st.text_input('配置文件路径', value=DEFAULT_CONFIG_PATH)

    # 显示加载按钮
    load_button = st.button('加载配置文件')

    # 如果加载按钮被点击，则加载配置文件
    if load_button:
        try:
            # 检查配置文件是否存在
            check_config_file(config_path)
            # 加载配置文件
            config = load_config(config_path)
            # 显示配置文件内容
            st.json(config)
        except Exception as e:
            st.error(f'加载配置文件失败：{e}')

    # 显示保存按钮
    save_button = st.button('保存配置文件')

    # 如果保存按钮被点击，且配置文件路径输入框不为空，则保存配置文件
    if save_button and config_path:
        try:
            # 显示配置文件内容输入框
            config_content = st.text_area('配置文件内容', height=200)
            # 尝试解析配置文件内容
            config = json.loads(config_content)
            # 保存配置文件
            save_config(config_path, config)
            st.success(f'配置文件 {config_path} 已成功保存')
        except json.JSONDecodeError as e:
            st.error(f'配置文件内容解析失败：{e}')
        except Exception as e:
            st.error(f'保存配置文件失败：{e}')

# 运行STREAMLIT应用
if __name__ == '__main__':
    main()