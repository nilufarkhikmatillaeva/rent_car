from typing import Any

from psycopg2.extras import DictRow

from core.config import ADMIN_USERNAME, ADMIN_PASSWORD
from core.db_settings import execute_query


async def register() -> bool:
    """
    Register new users
    :return: True if success else False
    """
    username: str = input("Username: ")
    password: str = input("Password: ")

    # check email if exists or not
    # ask password twice
    query: str = "INSERT INTO users (username, password) VALUES (%s, %s)"
    params: tuple[str, str] = (username, password,)

    if execute_query(query=query, params=params):
        print("Successfully registered ✅")
        return True
    else:
        print("Something went wrong, try again later ❌")
        return False


async def login() -> str | None:
    """
    Login by email
    :return: True if success else False
    """
    username: str = input("Username: ")
    password: str = input("Password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return "admin"

    query: str = "SELECT * FROM users WHERE username=%s AND password=%s"
    params: tuple[str, str] = (username, password,)

    if execute_query(query=query, params=params, fetch="one"):
        query2 = "UPDATE users SET is_login=True WHERE username = %s"
        params2 = (username,)
        execute_query(query=query2, params=params2)
        return "user"
    return None


def get_active_user() -> DictRow | None | list[tuple[Any, ...]]:
    """
    Get active user that is login currently
    :return:
    """
    query = "SELECT * FROM users WHERE is_login=TRUE"
    return execute_query(query=query, fetch="one")


def logout_all() -> None:
    """
    Update all user is_login to False
    :return:
    """
    query1 = "UPDATE users SET is_login=False WHERE id > 0"
    execute_query(query=query1)