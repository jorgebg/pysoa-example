from pysoa.common.transport.redis_gateway.constants import REDIS_BACKEND_TYPE_STANDARD

SOA_SERVER_SETTINGS = {  # Mandatory for simple_server
    'transport': {
        'path': 'pysoa.common.transport.redis_gateway.server:RedisServerTransport',
        'kwargs': {
            'backend_type': REDIS_BACKEND_TYPE_STANDARD,
            'default_serializer_config': {
                'path': 'pysoa.common.serializer.json_serializer:JSONSerializer',
            }
        },
    },
}

SOA_CLIENT_SETTINGS = {  # Not required
    'transport': {
        'path': 'pysoa.common.transport.redis_gateway.client:RedisClientTransport',
        'kwargs': {
            'backend_type': REDIS_BACKEND_TYPE_STANDARD,
            'default_serializer_config': {
                'path': 'pysoa.common.serializer.json_serializer:JSONSerializer',
            }
        },
    },
}
