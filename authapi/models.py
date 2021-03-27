from django.db import models

class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password