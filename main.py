import asyncio
from typing import Callable, Any, Coroutine
from orders import car_methods, crud, user
from auth import login
from utils import menus


async def show_user_menu() -> Callable:
    """
    All functionalities of the user
    :return:
    """
    print(menus.user_menu)
    option = input("Enter your option: ")

    if option == "1":
        await user.show_active_cars()
    elif option == "2":
        await user.show_active_cars()
    elif option == "3":
        return await show_auth_menu()
    else:
        print("Invalid option")

    return await show_user_menu()


async def show_admin_menu() -> Callable:
    """
    All functionalities of the admin
    :return:
    """
    print(menus.user_menu)
    option = input("Enter your option: ")

    if option == "1":
        await car_methods.show_all_cars()
    elif option == "2":
        await car_methods.add_new_car()
    elif option == "3":
        await car_methods.deactivate_car()
    elif option == "4":
        await crud.create_an_order()
    elif option == "5":
        await crud.show_all_active_orders()

    elif option == "6":
        await crud.show_all_orders()
    elif option == "7":
        await crud.finish_an_order()
    elif option == "8":
        await crud.show_all_users()
    elif option == "9":
        return await show_auth_menu()
    else:
        print("Invalid option")

    return await show_admin_menu()


async def show_auth_menu() -> Callable | None:
    """
    Show auth menu
    :return: function based on option
    """
    print(menus.auth_menu)
    option = input("Enter your option: ")
    if option == "1":
        await login.register()

    elif option == "2":
        user_type = await login.login()
        if user_type == "admin":
            return await show_admin_menu()
        elif user_type == "user":
            return await show_user_menu()

    elif option == "3":
        print("Good bye")
        return None

    return await show_auth_menu()


if __name__ == '__main__':
    # create tables in here
    # execute_query(query=models.users)
    # execute_query(query=models.cars)
    # execute_query(query=models.orders)

    asyncio.run(show_auth_menu())
