"""Модуль функций для игры ""Рассчитай и победи""."""
from random import randint
from typing import Callable


def set_enemy_health() -> int:
    """Устанавливает значение противника."""
    return randint(80, 120)


def get_lite_attack() -> int:
    """Возвращает значение слабой атаки."""
    return randint(2, 5)


def get_mid_attack() -> int:
    """Возвращает значение средней атаки."""
    return randint(15, 25)


def get_hard_attack() -> int:
    """Возвращает значение сильной атаки."""
    return randint(30, 40)


def compare_valumes(enemy_health: int, user_total_attack: int) -> bool:
    """Сравниевает сумму атак со здоровьем противника."""
    point_difference: int = abs(enemy_health - user_total_attack)
    if 0 <= point_difference <= 10:
        return True
    return False


def get_user_attack() -> int:
    """Запрашивает тип атаки и возвращает количество очков."""
    total: int = 0
    attacks_types: dict[str, Callable] = {
        'lite': get_lite_attack,
        'mid': get_mid_attack,
        'hard': get_hard_attack,
    }

    for i in range(5):
        input_attack: str = input('Введи тип атаки: ').lower()
        attack_value: int = attacks_types[input_attack]()
        print(f'Количество очков твоей атаки: {attack_value}.')
        total += attack_value
    return total


def run_game() -> bool:
    """Запускает игру."""
    user_total_attack: int = get_user_attack()
    enemy_health: int = set_enemy_health()
    print(f'Тобой нанесён урон противнику равный {user_total_attack}.')
    print(f'Очки здоровья противника до твоей атаки: {enemy_health}.')
    if compare_valumes(enemy_health, user_total_attack):
        print('Ура! Победа за тобой!')
    else:
        print('В этот раз не повезло :( Бой проигран.')
    yes_no: dict[str, bool] = {
        'Y': True,
        'N': False,
        'y': True,
        'n': False,
    }
    replay: str = input('Чтобы сыграть ещё раз, введи "y"; '
                        'если не хочешь продолжать игру, введи "n": ')
    if replay not in yes_no:
        raise ValueError('Такой команды в игре нет.')
    return yes_no[replay]
