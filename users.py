"""
Авторизация пользователя
Проверяется логин и пароль
"""

login = 'KiselevMY'
password = '12345678'

def user_authorization(l,p):
    if l != login:
        print('Вы не зарегистрированы в интернет-магазине')
        # reg_user(login) # здесь можно добавить регистрацию
    if p != password:
        print('Введен неверный пароль')
    else:
        print(f'Поздравляем, Вы успешно авторизовались {login} ')

