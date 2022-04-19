import logging

def ask_name():
    logging.info('Solicitando nombre al usuario')
    name = input('Cual es tu nombre? ')
    logging.debug(f'El usuario ingresó el nombre {name}')
    return name

def greet(name):
    logging.info(f'Saludando al usuario con nombre {name}')
    print(f'Hola {name}')
    logging.debug(f'Usuario {name} ha sido saludado')

if __name__ == '__main__':
    logging.basicConfig(
        filename = 'este-es-el-archivo-que-va-a-tener-los-logs.log',
        # filemode = 'w',
        format='%(asctime)s - %(levelname)s - %(message)s',
        # encoding = 'utf-8',
        level = logging.DEBUG
    )
    logging.info('Comenzando la ejecución de programa')
    name = ask_name()
    greet(name)