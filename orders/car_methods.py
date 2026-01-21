from typing import Any

from core.db_settings import execute_query


def show_all_cars() -> list[Any]:
    """
    Shows all the cars available in the system
    :return: list
    """
    query = """ SELECT * FROM cars ORDER BY id """
    return execute_query(query=query, params=None, fetch="all")

def add_new_car(name: str, model: str, is_active: bool = False) -> None:
    """
    Adds a new car to the system
    :return:
    """
    query = """ 
    INSERT INTO cars (name, model, is_active) VALUES (%s, %s, %s)"""
    params = (name, model, is_active)
    return execute_query(query=query, params = params, fetch = None)

def deactivate_car(car_id: int) ->None:
    query = """
    UPDATE cars 
    SET is_active = FALSE
    WHERE id = %s
    """
    params: tuple[int] = (car_id,)
    execute_query(query=query, params = params, fetch = None)
