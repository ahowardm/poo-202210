import logging

logging.basicConfig(
    filename='clase.log',
    encoding='utf-8',
    level = logging.DEBUG
    )

logging.warning('Este es un warning')
logging.info('El programa pasó por acá')
logging.critical('Pasó un desastre')