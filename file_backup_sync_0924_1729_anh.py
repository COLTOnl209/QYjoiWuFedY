# 代码生成时间: 2025-09-24 17:29:00
import streamlit as st
import os
import shutil
from datetime import datetime

""" 文件备份和同步工具

该程序使用Streamlit框架创建一个简单的文件备份和同步工具。
用户可以指定源文件夹和目标文件夹，程序将自动备份并同步文件。
"""

# 函数：创建备份目录
def create_backup_dir(target_dir):
    """
    在目标目录中创建一个以当前日期和时间命名的备份目录。
    """
    backup_folder = os.path.join(target_dir, datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(backup_folder, exist_ok=True)
    return backup_folder

# 函数：同步文件
def sync_files(source_dir, backup_dir):
    """
    将源目录中的文件复制到备份目录中。
    """
    for filename in os.listdir(source_dir):
        src_file = os.path.join(source_dir, filename)
        dst_file = os.path.join(backup_dir, filename)
        try:
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)
        except Exception as e:
            st.error(f"无法复制文件 {src_file} 到 {dst_file}: {str(e)}")

# Streamlit界面
def main():
    st.title("文件备份和同步工具")
    
    # 输入源目录和目标目录
    source_dir = st.text_input("源目录")
    target_dir = st.text_input("目标目录")
    
    # 按钮：开始备份和同步
    if st.button("开始备份"):
        if not source_dir or not target_dir:
            st.error("请填写源目录和目标目录")
        else:
            try:
                # 创建备份目录
                backup_dir = create_backup_dir(target_dir)
                
                # 同步文件
                sync_files(source_dir, backup_dir)
                
                st.success("文件备份和同步成功！")
            except Exception as e:
                st.error(f"备份和同步失败: {str(e)}")

if __name__ == '__main__':
    main()