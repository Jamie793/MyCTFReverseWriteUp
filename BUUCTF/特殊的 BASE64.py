import base64
modifyBase64 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0987654321/+'
standardBase64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


encData = 'mTyqm7wjODkrNLcWl0eqO8K8gc1BPk1GNLgUpI=='



print(base64.b64decode(encData.translate(str.maketrans(modifyBase64, standardBase64))).decode('utf-8'))