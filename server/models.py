class User:
    def __init__(self, username=None, password=None):
        self._username = username
        self._password = password

    def getusername(self):
        return self._username

    def setusername(self, value):
        self._username = value

    def getpassword(self):
        return self._password

    def setpassword(self, value):
        self._password = value

user = User()