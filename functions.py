def greet_user(name):
    """
    Функція вітає користувача за його ім'ям.

    Parameters:
    name (str): Ім'я користувача.

    Returns:
    str: Привітання.
    """
    return f"Привіт, {name}!"

# Приклад використання функції
user_name = "Андрій"
print(greet_user(user_name))