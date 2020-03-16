import logging
import json
import datetime
import uuid
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    response = []

    # Pull in data from get request.
    name = req.params.get('name')

    if name:
        logging.warning('Function has been executed: {}'.format(datetime.datetime.now()))

        responseDict = {'name': name, 
                        'runTime': str(datetime.datetime.now()), 
                        'id': str(uuid.uuid1())}

        response.append(responseDict)

        return json.dumps(response)

    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
