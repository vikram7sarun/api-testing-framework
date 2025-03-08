from api.base_api import BaseAPI

class UsersAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_users(self):
        return self.send_request("GET", "/users")

    def create_user(self, user_data):
        return self.send_request("POST", "/users", json=user_data)

    def get_user_by_id(self, user_id):
        return self.send_request("GET", f"/users/{user_id}")

    def delete_user(self, user_id):
        return self.send_request("DELETE", f"/users/{user_id}")
