from typing import Any
from core.db_settings import execute_query

def show_active_cars() -> list[Any]:
    """
    Show all cars that are currently active (available).
    :return: list of active cars
    """
    query = """
    SELECT id, name, model, is_active, created_at
    FROM cars
    WHERE is_active = TRUE
    ORDER BY id ASC
    """
    return execute_query(query=query, params=None, fetch="all")

def show_my_orders(user_id: int) -> list[Any]:
    """
    Show all orders made by a specific user.
    :param user_id: the ID of the user
    :return: list of orders
    """
    query = """
    SELECT id, user_id, ordered_car, is_active, activated_date
    FROM orders
    WHERE user_id = %s
    ORDER BY activated_date DESC
    """
    params = (user_id,)
    return execute_query(query=query, params=params, fetch="all")