from user import Users
import hmac

def authenticate(username,password):
    user = Users.find_by_username(username)
    if user and hmac.compare_digest(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return Users.find_by_userid(user_id)