import logging
import json
import base64
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = json.dumps({
        'text': 'This HTTP triggered function executed successfully.',
    })

    principal = req.headers['x-ms-client-principal']
    decoded = base64.b64decode(principal)

    logging.info("PARAMS:")
    logging.info(req.params)
    logging.info("HEADERS:")
    logging.info(list(req.headers.keys()))
    logging.info("VALUES:")
    logging.info(list(req.headers.values()))
    logging.info("USER:")
    logging.info(decoded)

    return func.HttpResponse(body=message, status_code=200)
