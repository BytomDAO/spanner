import json


class Keys(object):
    def __init__(self, alias, xpub, file, *args, **kwargs):
        self.alias = alias
        self.xpub = xpub
        self.file = file

    @staticmethod
    def list(connection):
        response = connection.request("/list-keys")

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            key_list = list(map(lambda x: Keys(**x), resp_json['data']))
            return key_list
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def find_by_alias(connection, alias):
        key_list = Keys.list(connection)
        for key in key_list:
            if key.alias == alias:
                return key

    @staticmethod
    def create(connection, alias, password):
        body_json = {"alias": alias, "password": password}
        response = connection.request("/create-key", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return Keys(**resp_json['data'])
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def delete(connection, xpub, password):
        body_json = {"xpub": xpub, "password": password}

        response = connection.request("/delete-key", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return "true"
        else:
            return "false"

    @staticmethod
    def delete_by_alias(connection, alias, password):
        key = Keys.find_by_alias(connection, alias)
        key_xpub = key.xpub
        return Keys.delete(connection, key_xpub, password)

    @staticmethod
    def reset_password(connection, xpub, old_password, new_password):
        body_json = {"xpub": xpub, "old_password": old_password, "new_password": new_password}

        response = connection.request("/reset-key-password", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == "success":
            return "true"
        else:
            return "false"
