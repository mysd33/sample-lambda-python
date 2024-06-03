"""サービスクラスを定義するモジュールです。"""

from common.domain.model import User
from common.domain.repository import UserRepository


class UserService:
    """ユーザ情報のサービスクラスです。"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def find_user(self, user_id: int) -> User:
        """user_idが一致するUserを取得します。"""
        return self.user_repository.find_one(user_id)

    def register_user(self, user_name: str) -> User:
        """ユーザを登録します。"""
        return self.user_repository.create_one(user_name)
