# 代码生成时间: 2025-10-02 19:15:47
import streamlit as st
from typing import Dict

"""
Learning Resources App
=======================
A Streamlit application that serves as a learning resource library.
"""

# Define a dictionary to hold learning resources
learning_resources: Dict[str, Dict[str, str]] = {
    'Math': {
        'Course': 'Calculus 101',
        'Link': 'https://example.com/math-course'
    },
    'Science': {
        'Course': 'Introduction to Physics',
        'Link': 'https://example.com/science-course'
    },
    'Programming': {
        'Course': 'Python Basics',
        'Link': 'https://example.com/programming-course'
    }
}

"""
Function to display a learning resource
"""
def display_resource(subject: str, resource: Dict[str, str]) -> None:
    """Displays the learning resource for a given subject."""
    st.subheader(f'{subject} Learning Resource')
    st.write(f'**Course:** {resource[