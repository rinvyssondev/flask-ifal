swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Sistema Acadêmico API",
        "description": "API REST para gerenciamento de sistema acadêmico",
        "version": "1.0.1",
        "contact": {
            "name": "Rinvysson",
            "email": "rinvysson.dev@hotmail.com"
        }
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": ["http"]
}