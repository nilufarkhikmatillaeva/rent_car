from core.db_settings import execute_query


def create_an_order(user_id: int, ordered_car: str) -> None:
    """
    Create a new order in the system
    """
    query = """
    INSERT INTO orders(user_id, ordered_car) 
    VALUES( %s,%s )
    """
    params = (user_id, ordered_car)
    execute_query(query=query, params = params)

def show_all_active_orders():
    query = """
    SELECT id, user_id, ordered_car, is_active, activated_date
    FROM orders
    WHERE is_active = TRUE AND user_id = %s
    ORDER BY activated_date DESC
    """
    return execute_query(query=query)

def show_all_orders():
    query = """
    SELECT id, user_id, ordered_car, is_active, activated_date
    FROM orders
    ORDER BY activated_date DESC"""
    return execute_query(query=query)

def finish_an_order(order_id: int) -> None:
    """
    Mark an order as finished (set is_active = FALSE).
    """
    query = """
    UPDATE orders
    SET is_active = FALSE
    WHERE id = %s
    """
    params = (order_id,)
    execute_query(query=query, params=params)

def show_all_users():
    query = """
    SELECT id, username, email, is_login, is_active, created_at
    FROM users
    ORDER BY id ASC
    """
    return execute_query(query=query)
