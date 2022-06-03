import base64
import string
b = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0987654321/+'
b1 = string.ascii_uppercase + string.ascii_lowercase + string.digits + '/+'

base = str.translate(
    'mTyqm7wjODkrNLcWl0eqO8K8gc1BPk1GNLgUpI==', str.maketrans(b, b1))

print(base64.b64decode(base).decode())
