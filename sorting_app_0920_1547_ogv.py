# 代码生成时间: 2025-09-20 15:47:40
import streamlit as st

"""
# NOTE: 重要实现细节
Streamlit application for sorting algorithms.
This application demonstrates different sorting algorithms allowing users to input a list of numbers and see the result.
# FIXME: 处理边界情况
"""

# Define sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
# FIXME: 处理边界情况
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
# NOTE: 重要实现细节
            j -= 1
        arr[j + 1] = key
    return arr

# Streamlit interface
def main():
    st.title('Sorting Algorithms Visualization')
    
    # Input section
    st.subheader('Input List')
    input_list = st.text_input('Enter a list of numbers separated by commas', value='', help='e.g., 1,2,3,4,5')
    if input_list:
        # Error handling for input
# 添加错误处理
        try:
            input_list = input_list.split(',')
            input_list = [int(i.strip()) for i in input_list]
        except ValueError:
# 扩展功能模块
            st.error('Invalid input. Please enter a list of numbers only.')
            return
    
        # Sorting selection section
        st.subheader('Choose Sorting Algorithm')
        sorting_algorithm = st.selectbox(
            'Algorithm:',
            ('Bubble Sort', 'Selection Sort', 'Insertion Sort')
        )
        
        if st.button('Sort List'):
# FIXME: 处理边界情况
            if sorting_algorithm == 'Bubble Sort':
# 添加错误处理
                sorted_list = bubble_sort(input_list.copy())
            elif sorting_algorithm == 'Selection Sort':
                sorted_list = selection_sort(input_list.copy())
            elif sorting_algorithm == 'Insertion Sort':
                sorted_list = insertion_sort(input_list.copy())
            
            # Display sorted list
            st.subheader('Sorted List')
            st.write(sorted_list)

if __name__ == '__main__':
# 添加错误处理
    main()
# NOTE: 重要实现细节