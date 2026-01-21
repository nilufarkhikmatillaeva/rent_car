"""
All tables qieries
"""
users = """
        CREATE TABLE IF NOT EXISTS users
        (
            id         BIGSERIAL PRIMARY KEY,
            username   VARCHAR(255) NOT NULL,
            email      VARCHAR(255) NOT NULL UNIQUE,
            password   VARCHAR(128) NOT NULL,
            is_login   BOOLEAN   DEFAULT FALSE,
            is_active  BOOLEAN   DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) 
        """


cars = """
        CREATE TABLE IF NOT EXISTS cars
        (
            id  BIGSERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            model VARCHAR(255) NOT NULL,
            is_active BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            """

orders = """
        CREATE TABLE IF NOT EXISTS orders
        (
            id BIGSERIAL PRIMARY KEY,
            user_id BIGSERIAL REFERENCES users(id) ON DELETE CASCADE NOT NULL,
            ordered_car VARCHAR(255) NOT NULL,
            is_active BOOLEAN DEFAULT FALSE,
            activated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            """