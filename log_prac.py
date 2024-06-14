import logging

def verify_password_criteria(password):
    
    min_length = 8
    max_length = 15
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if len(password) < min_length or len(password) > max_length:
        return "Between 8 and 15 characters long."

    if not any(char.isupper() for char in password):
        return "Contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Must contain at least one digit."

    if not any(char in special_characters for char in password):
        return "Contain at least one special character."

    return "Valid password."

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

password = "Password123!"
result = verify_password_criteria(password)
logger.info(result)
