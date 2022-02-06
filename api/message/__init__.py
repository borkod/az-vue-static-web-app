import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = json.dumps({'text': 'This HTTP triggered function executed successfully.'})

    return func.HttpResponse(body=message, status_code=200)
