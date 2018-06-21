import json


class Asset(object):

    @staticmethod
    def list(connection):
        response = connection.request("/list-assets")

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def get_asset(connection, asset_id):
        asset_list = Asset.list(connection)
        for asset in asset_list:
            if asset['id'] == asset_id:
                return asset

    @staticmethod
    def get_asset_by_alias(connection, asset_alias):
        asset_list = Asset.list(connection)
        for asset in asset_list:
            if asset['alias'] == asset_alias.upper():
                return asset

    @staticmethod
    def create(connection, root_xpubs, alias, quorum):
        body_json = {"root_xpubs": root_xpubs, "alias": alias, "quorum": quorum}
        response = connection.request("/create-asset", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def update_alias(connection, asset_id, new_alias):
        body_json = {"id": asset_id, "alias": new_alias}
        response = connection.request("/update-asset-alias", body_json)

        resp_json = json.loads(response.text)

        return resp_json
