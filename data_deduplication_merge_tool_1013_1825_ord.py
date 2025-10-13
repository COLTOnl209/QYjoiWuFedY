# 代码生成时间: 2025-10-13 18:25:09
import streamlit as st
import pandas as pd
from typing import List, Union

"""
数据去重和合并工具
用于合并两个数据集并去除重复项
"""


class DataDeduplicationMergeTool:
    def __init__(self):
        pass  # 初始化方法

    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        加载数据文件
        :param file_path: 文件路径
        :return: Pandas DataFrame
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            st.error(f"加载数据失败：{e}")
            return None

    def deduplicate_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        去除数据中的重复项
        :param data: Pandas DataFrame
        :return: 去重后的Pandas DataFrame
        """
        try:
            return data.drop_duplicates()
        except Exception as e:
            st.error(f"去重失败：{e}")
            return None

    def merge_data(self, data1: pd.DataFrame, data2: pd.DataFrame) -> pd.DataFrame:
        """
        合并两个数据集
        :param data1: 第一个Pandas DataFrame
        :param data2: 第二个Pandas DataFrame
        :return: 合并后的Pandas DataFrame
        """
        try:
            merged_data = pd.concat([data1, data2], ignore_index=True)
            return merged_data
        except Exception as e:
            st.error(f"合并数据失败：{e}")
            return None

    def run_tool(self):
        """
        运行数据去重和合并工具
        """
        st.title('数据去重和合并工具')

        # 加载数据文件
        file_path1 = st.file_uploader('上传第一个数据文件', type=['csv', 'txt'])
        file_path2 = st.file_uploader('上传第二个数据文件', type=['csv', 'txt'])

        if file_path1 and file_path2:
            data1 = self.load_data(file_path1)
            data2 = self.load_data(file_path2)

            if data1 is not None and data2 is not None:
                # 去重
                deduplicated_data1 = self.deduplicate_data(data1)
                deduplicated_data2 = self.deduplicate_data(data2)

                if deduplicated_data1 is not None and deduplicated_data2 is not None:
                    # 合并数据
                    merged_data = self.merge_data(deduplicated_data1, deduplicated_data2)

                    if merged_data is not None:
                        st.write('合并后的数据：')
                        st.dataframe(merged_data)

                
def main():
    """
    主函数
    """
    tool = DataDeduplicationMergeTool()
    tool.run_tool()

if __name__ == '__main__':
    main()