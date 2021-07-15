from mongoengine import *
from mongoengine.connection import connect
from mongoengine.fields import *
from mongoengine.document import *

connect("LandingPage")

class User(DynamicDocument):
    name = StringField()
    email = EmailField()
    message = StringField()
