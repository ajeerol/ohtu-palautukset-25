import re
from entities.user import User
# import sys, pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):

        username_min_length = 3
        password_min_length = 8

        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < username_min_length:
            raise UserInputError("Invalid username: username too short")
      
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Invalid username: use chars between [a-z]")
      
        if len(password) < password_min_length:
            raise UserInputError("Invalid password: password too short")

        if password.isalpha():
            raise UserInputError("Invalid password: only alpha chars used")
     
