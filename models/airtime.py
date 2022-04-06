from utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

#channel table model
class Airtime(db.Model):
    __tablename__ = 'airtime'

#channel table fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number =  db.Column(db.String(15), nullable=False)
    amount =  db.Column(db.String(100), nullable=False)
    request_code = db.Column(db.String(100), nullable=False)
    request_message = db.Column(db.String(100), nullable=False)
    request_transaction_id = db.Column(db.String(100), nullable=False)
    reference_id = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(50), nullable=False)
    callback_code = db.Column(db.String(10), nullable=False)
    callback_message = db.Column(db.String(100), nullable=False)
    callback_timestamp = db.Column(db.String(50), nullable=False)
    callback_transaction_id = db.Column(db.String(100), nullable=False)


    def __init__(self, phone_number, amount, request_code, request_message, request_transaction_id, reference_id, client_email, callback_code, \
                    callback_message, callback_timestamp, callback_transaction_id):
        self.phone_number = phone_number
        self.amount = amount
        self.request_code = request_code
        self.request_message = request_message
        self.request_transaction_id = request_transaction_id
        self.reference_id = reference_id
        self.client_email = client_email
        self.callback_code = callback_code
        self.callback_message = callback_message
        self.callback_timestamp = callback_timestamp
        self.callback_transaction_id = callback_transaction_id
    
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

#products database with flask marshmallow
class AirtimeSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Airtime
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    phone_number = fields.String(required=True)
    amount = fields.String(required=True)
    request_code = fields.String(required=True)
    request_message = fields.String(required=True)
    request_transaction_id = fields.String(required=True)
    reference_id = fields.String(required=True)
    client_email = fields.String(required=True)
    callback_code = fields.String(required=True)
    callback_message = fields.String(required=True)
    callback_timestamp = fields.String(required=True)
    callback_transaction_id = fields.String(required=True)