import string
import secrets

def generate_short_code():
    
    alphabet = string.ascii_letters + string.digits
    short_code = ''.join(secrets.choice(alphabet) for i in range(6))
    
    return short_code
