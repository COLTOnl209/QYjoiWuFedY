# 代码生成时间: 2025-10-07 01:41:24
import streamlit as st
import json
import os
import toml
import yaml

"""
配置文件管理器 - 使用STREAMLIT框架创建的简易配置文件编辑器。
支持JSON, TOML, YAML格式。
"""

# 定义一个函数来加载和解析配置文件
def load_config(file_path):
    try:
        if file_path.endswith(".json"):
            with open(file_path, 'r') as file:
                return json.load(file)
        elif file_path.endswith(".toml"):
            return toml.load(file_path)
        elif file_path.endswith(".yaml\) or file_path.endswith(".yml"):
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        st.error(f"Failed to load config file: {e}")
        return None

# 定义一个函数来保存配置文件
def save_config(config, file_path):
    try:
        if file_path.endswith(".json"):
            with open(file_path, 'w') as file:
                json.dump(config, file, indent=4)
        elif file_path.endswith(".toml"):
            with open(file_path, 'w') as file:
                toml.dump(config, file)
        elif file_path.endswith(".yaml\) or file_path.endswith(".yml"):
            with open(file_path, 'w') as file:
                yaml.dump(config, file, allow_unicode=True, default_flow_style=False)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        st.error(f"Failed to save config file: {e}")
        return False
    return True

# 使用STREAMLIT框架设置UI界面
def main():
    st.title("配置文件管理器")
    file_path = st.file_uploader("选择配置文件", type=["json", "toml", "yaml", "yml"])
    if file_path is not None:
        config = load_config(file_path)
        if config is not None:
            # 使用Streamlit的session state来保存配置数据
            session_state.config = config
            
            # 显示编辑后的配置文件内容
            st.json(config)
            
            # 提供保存按钮
            if st.button("保存配置"):
                save_config(session_state.config, file_path)
                st.success("配置文件已保存")
    else:
        st.info("请上传配置文件")
        
    # 提供清空状态的按钮
    if st.button("清空状态"):
        session_state.config = None
        st.experimental_rerun()

# 程序入口点
if __name__ == "__main__":
    main()