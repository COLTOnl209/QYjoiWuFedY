# 代码生成时间: 2025-09-23 06:33:14
import streamlit as st

"""
Streamlit-based Inventory Management System
=====================================

This script creates a simple inventory management system using Streamlit.
Features include viewing and updating inventory items."""

# Initialize inventory data structure
inventory = {"items": []}

# Function to load inventory data from a file
def load_inventory(file_path):
    try:
        with open(file_path, 'r') as file:
            return eval(file.read())
    except FileNotFoundError:
        st.error("Inventory file not found.")
        return {}
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return {}

# Function to save inventory data to a file
def save_inventory(inventory, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(str(inventory))
    except Exception as e:
        st.error(f"An error occurred during save: {e}")

# Function to add a new item to the inventory
def add_item(item_name, quantity):
    if item_name and quantity:
        inventory["items"].append({"name": item_name, "quantity": quantity})
        st.success("Item added successfully.")
    else:
        st.error("Invalid item name or quantity.")

# Function to update an existing item in the inventory
def update_item(item_name, new_quantity):
    for item in inventory["items"]:
        if item["name"] == item_name:
            item["quantity"] = new_quantity
            st.success("Item updated successfully.")
            return
    st.error("Item not found.")

# Streamlit interface
def main():
    st.title("Inventory Management System")

    # Load inventory data
    inventory_path = "inventory.txt"
    global inventory
    inventory = load_inventory(inventory_path)

    # Display inventory items
    st.write("Current Inventory:")
    if inventory["items"]:
        for item in inventory["items"]:
            st.write(f"Name: {item['name']}, Quantity: {item['quantity']}")
    else:
        st.write("There are no items in the inventory.")

    # Add new item form
    with st.form("add_item_form"):
        item_name = st.text_input("Item Name")
        quantity = st.number_input("Quantity", min_value=0, value=0)
        submit_button = st.form_submit_button("Add Item")
        if submit_button:
            add_item(item_name, quantity)
            save_inventory(inventory, inventory_path)

    # Update item form
    with st.form("update_item_form"):
        item_name = st.text_input("Item Name\)
        new_quantity = st.number_input("New Quantity", min_value=0, value=0)
        submit_button = st.form_submit_button("Update Item\)
        if submit_button:
            update_item(item_name, new_quantity)
            save_inventory(inventory, inventory_path)

if __name__ == "__main__":
    main()