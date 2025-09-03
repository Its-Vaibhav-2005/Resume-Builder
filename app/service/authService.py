from app.repository.userRepository import getUserByEmail, createUser

def registerUser(name, email, password):
    if getUserByEmail(email):
        raise ValueError("Email already registered")
    user = createUser(name, email, password)
    return user

def authenticate(email, password):
    user = getUserByEmail(email)
    if user and user.checkPassword(password):
        return user
    return None
