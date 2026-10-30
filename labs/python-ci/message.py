"""Логика приветствия."""


def greeting(name):
    """Вернуть приветствие с непустым именем."""
    name = name.strip()
    if not name:
        raise ValueError("Имя не должно быть пустым")
    return f"Hello, {name}!"
