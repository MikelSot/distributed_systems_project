from model.user import User

user_data = {}

class UserData:
    @staticmethod
    def user_exist(user: User ):
        return user_data.get(user.name)

    def add_user(self, user: User) -> User | bool:
        if self.user_exist(user):
            return False

        user_data[user.name] = user
        return user

    def delete_user(self, user: User):
        if self.user_exist(user):
            user_data.pop(user.name)

    def user_data_info(self):
        return  user_data