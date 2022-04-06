from flask import Blueprint, request, g, jsonify, make_response
from datetime import datetime
from utils.database import db
from models.airtime import Airtime, AirtimeSchema
from utils.randoms import random_string, random_number
import requests
import json


#registering routes to the blueprint, which is used to create endpoint
airtime_routes = Blueprint("airtime_routes", __name__)
webhook = Blueprint("webhook", __name__)


#the function for charge endpoint it requires authorization to be accessed
@airtime_routes.route('/', methods=['POST'])
def create_transaction():
    try:
        data = request.get_json()

        reference_id = random_number(10)

        #making request to BEEM API
        url = "https://apiairtime.beem.africa/v1/transfer"

        payload = json.dumps({
        "dest_addr": str(data['phone_number']),
        "amount": data['amount'],
        "reference_id": reference_id
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic '
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        beem_response = json.loads(response.text) 


        #update the data from the request
        data.update(
            {
                "request_code": beem_response['code'],
                "request_transaction_id": beem_response['transaction_id'],
                "request_message": beem_response['message'],
                "reference_id": reference_id,
                "callback_code": "None",
                "callback_message": "None",
                "callback_timestamp": "None",
                "callback_transaction_id": "None",

            })

        #post data to the database
        airtime_schema = AirtimeSchema()
        airtime = airtime_schema.load(data)
        result = airtime_schema.dump(airtime.create())
        
        response_header = {'Access-Control-Allow-Origin': '*'}
        return make_response(jsonify(beem_response), headers=response_header)

    except Exception as e:
        return make_response(jsonify(
            {"Status": "Missing Parameter",
            "message": "Missing Parameters"
            }), 422)
    



@webhook.route('/', methods=['POST'])
def get_webhook():

    #receiving webhook from beem
    data = request.get_json()

    #update transaction data after receiving webhook
    transaction_id=data['args']['transaction_id']

    update = Airtime.query.filter_by(request_transaction_id=transaction_id).update(dict(
                                                                                    callback_code=data['code'],
                                                                                    callback_message=data['message'], 
                                                                                    callback_timestamp=data['args']['timestamp'], 
                                                                                    callback_transaction_id=data['args']['transaction_id']
                                                                                    ))
    db.session.commit()

    
    return data
