from __future__ import unicode_literals

import re
import sys

from django.db import models
from django.shortcuts import HttpResponse, redirect, render

import bcrypt

rejectEmail = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# class UserManager(models.Manager):
#     def verify(self, postData):
#         errors = {}
#         if len(postData['password']) < 3:
#             errors["password"] = "Password should be more than 3 characters"
#         if len(postData['email']) < 5 or not rejectEmail.match(
#                 postData['email']):
#             errors['email'] = "Email cannot be empty!"
#         if len(postData['password']) < 1:
#             errors['password'] = "Password cannot be empty"
#         return errors

#     def creater(self, postData):
#         errors = {}
#         if len(postData['cPassword']) < 3:
#             errors["cPassword"] = "Password should be more than 3 characters"

#         if len(postData['conPassword']) < 3:
#             errors["conPassword"] = "Password should be more than 3 characters"

#         if len(postData['eEmail']) < 5:
#             errors['eEmail'] = "Email cannot be empty!"

#         if not rejectEmail.match(postData['eEmail']):
#             errors['eEmail'] = "Email is invalid!"

#         if postData['cPassword'] != postData['conPassword']:
#             errors['cPassword'] = "Passwords do not match!"

#         if postData['nName'] < 2:
#             errors['nName'] = "Full name must be longer than 2 characters."
#         return errors

#     def addItem(self, postData):
#         errors = {}
#         if len(postData['item']) < 2:
#             errors["item"] = "Item name should be more than 2 characters"
#         return errors
