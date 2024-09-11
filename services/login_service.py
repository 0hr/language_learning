class LoginService:
    def __init__(self):
        pass

    def login(self, username, password):
        if username == "admin" and password == "<PASSWORD>":
            return True
        return False

def login_service() -> LoginService:
    return LoginService()