import logging

logging.basicConfig(filename='../log/exemplo.log'
                    , encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def log(status:str = 'debug', message: str = ''):
    
    options: dict = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    log_func = options.get(status)
    
    if not log_func:
        raise ValueError(f"Status inválido: {status}")
    
    return log_func(message)

# log(status='info', message='test')