# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def deposit_action(func_account: int | float) -> int | float:
    
    global counter_action
    
    while True:
        dep_number = int(input('Введите сумму пополнения кратную 50:  '))
        if not dep_number % MULTIPLICITY: # Проверяю на кратность 50
            break
    print(f'поздравляем, вы внесли {dep_number} на счет')
        
    if func_account > RICH_MAN:
        func_account *= 0.9 # Налог на богатства
        
    func_account += dep_number  # Само поплнение
    counter_action += 1
    print(func_account, counter_action)
    if counter_action % BONUS == 0: # Проверяю на кратность BONUS
        func_account *= (1+ BONUS/100)
        print(f'Добавили бонус {BONUS}% получили {func_account}')
    return func_account


def withdraw_action(func_account: int | float) -> int | float:

    global counter_action
    
    while True:
        withdraw_number = int(input('Введите сумму снятия кратную 50:  '))
        if not withdraw_number % MULTIPLICITY: # Проверяю на кратность 50
            break
    if func_account > RICH_MAN:
        func_account *= 0.9 # Налог на богатства
        print(f'У вас слишком много денег и с ваш удержали 10% = {func_account/0.9*0.1}')
        
    if withdraw_number > account:
        print('Недостаточно средств')
        return func_account # Выход из функции без пополнения
        
    withdraw_fee =  withdraw_number * WITHDRAWAL_FEE_PERCENT / 100
    if withdraw_fee < WITHDRAWAL_FEE_MIN:
        func_account = func_account -  WITHDRAWAL_FEE_MIN - withdraw_number
        print(f'Коммиссия за сеъем = {WITHDRAWAL_FEE_MIN}')
    elif WITHDRAWAL_FEE_MIN < withdraw_fee < WITHDRAWAL_FEE_MAX:
        func_account = func_account - withdraw_fee - withdraw_number
        print(f'Коммиссия за сеъем = {withdraw_fee}')
    elif withdraw_fee > WITHDRAWAL_FEE_MAX:
        func_account = func_account -  WITHDRAWAL_FEE_MAX - withdraw_number
        print(f'Коммиссия за сеъем = {WITHDRAWAL_FEE_MAX}')
        
    counter_action += 1
    print(func_account, counter_action)
    if counter_action % BONUS == 0: # Проверяю на кратность BONUS
        func_account *= (1+ BONUS/100)
    return func_account

account = 0
counter_action = 0
MULTIPLICITY = 50
BONUS = 3 # Каждую третью операцию начисляем %
RICH_MAN = 5_000_000
WITHDRAWAL_FEE_PERCENT = 1.5
WITHDRAWAL_FEE_MIN = 30
WITHDRAWAL_FEE_MAX = 600

while True:
    action = input('Введите действие: пополнить, снять, выйти, набрав: deposit, withdraw, exit:  ')
    if action == 'deposit':
        account = deposit_action(account) #Функция внесения денег
        print(account)

    elif action == 'withdraw':
        account = withdraw_action(account)
        print(f'Текущий остаток = {account}')

    elif action == 'exit':
        print(f'Завершение работы с остатком {account}')
        break
    else:
        print('Выбирите корректное действие')
