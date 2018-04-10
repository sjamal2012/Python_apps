# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class LeadManager(models.Manager):
    def validate_lead_info(self, post_data):
        errors = []

        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("First and Last name must be at least 2 characters long!")
        elif not str(post_data['first_name']).isalpha() and not str(post_data['last_name']).isalph():
            errors.append("First and Last name must only contain letters!")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append("Name must contain letter characters only")
        if len(post_data['email']) < 1 or not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Email is not valid")

        return errors

class Lead(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    registered_datetime = models.DateTimeField(auto_now=True)

    objects = LeadManager()
