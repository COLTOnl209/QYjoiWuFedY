# 代码生成时间: 2025-10-11 02:59:26
import streamlit as st

# 用户权限管理系统
class UserPermissionManager:
    def __init__(self):
        # 初始化用户权限列表
        self.permissions = {}

    def add_user(self, username):
        """
        添加用户
        :param username: 用户名
        """
        if username in self.permissions:
            raise ValueError(f"User {username} already exists.")
        self.permissions[username] = []
        st.write(f"User {username} added successfully.")

    def remove_user(self, username):
        """
        移除用户
        :param username: 用户名
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        del self.permissions[username]
        st.write(f"User {username} removed successfully.")

    def add_permission(self, username, permission):
        """
        为用户添加权限
        :param username: 用户名
        :param permission: 权限
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        self.permissions[username].append(permission)
        st.write(f"Permission {permission} added to user {username} successfully.")

    def remove_permission(self, username, permission):
        """
        移除用户的权限
        :param username: 用户名
        :param permission: 权限
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        if permission in self.permissions[username]:
            self.permissions[username].remove(permission)
            st.write(f"Permission {permission} removed from user {username} successfully.")
        else:
            st.write(f"Permission {permission} does not exist for user {username}.")

    def list_permissions(self, username):
        """
        列出用户的权限
        :param username: 用户名
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        st.write(f"Permissions for user {username}: {self.permissions[username]}")

# 主函数
def main():
    # 创建用户权限管理器实例
    manager = UserPermissionManager()

    # 添加用户
    st.title('User Permission Manager')
    username = st.text_input('Enter username:')
    if username:
        try:
            manager.add_user(username)
        except ValueError as e:
            st.error(e)

    # 移除用户
    remove_username = st.text_input('Enter username to remove:')
    if remove_username:
        try:
            manager.remove_user(remove_username)
        except ValueError as e:
            st.error(e)

    # 添加权限
    permission = st.text_input('Enter permission:')
    if permission:
        try:
            manager.add_permission(username, permission)
        except ValueError as e:
            st.error(e)

    # 移除权限
    remove_permission = st.text_input('Enter permission to remove:')
    if remove_permission:
        try:
            manager.remove_permission(username, remove_permission)
        except ValueError as e:
            st.error(e)

    # 列出权限
    if username:
        try:
            manager.list_permissions(username)
        except ValueError as e:
            st.error(e)

if __name__ == '__main__':
    main()