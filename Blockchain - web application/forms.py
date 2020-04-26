from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo,Regexp
import main



class get_block(FlaskForm):
    block_number = StringField('Enter a block number',
                           validators=[DataRequired()])    
    submit = SubmitField('Get Block')

class create_wallets(FlaskForm):   
    submit = SubmitField('Create wallet')


class create_transactions(FlaskForm):
    to = StringField('To',
                           validators=[DataRequired()])    
    From = StringField('From',
                        validators=[DataRequired()]) 

    private_key = StringField('Private Key',
                        validators=[DataRequired()]) 

    amount = IntegerField('Amount',
                        validators=[DataRequired()]) 

    submit = SubmitField('Transfer')

class mine_block(FlaskForm):   
    submit = SubmitField('Mine block')

class check_blockchain(FlaskForm):   
    submit = SubmitField('Check blockchain')
