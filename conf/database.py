from .global_vars import POSTGRES_HOST, POSTGRES_NAME, POSTGRES_PORT, POSTGRES_USERNAME,  POSTGRES_PASSWORD


TORTOISE_CONFIG = {
    "connections": {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': POSTGRES_HOST,
                'port': POSTGRES_PORT,
                'user': POSTGRES_USERNAME,
                'password': POSTGRES_PASSWORD,
                'database': POSTGRES_NAME,
            }
        }
    },
    'apps': {
        'models': {
            'models': ["models", "aerich.models"],
            'default_connection': 'default',
        }
    }
}
