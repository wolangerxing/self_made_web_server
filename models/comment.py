from models.model_basic import SQLModel
from models.user import User


class Comment(SQLModel):
    sql_create = """
    CREATE TABLE `Comment` (
        `id`         INT NOT NULL AUTO_INCREMENT,
        `content` VARCHAR(255) NOT NULL,
        `weibo_id`   INT NOT NULL,
        `user_id`    INT NOT NULL,
        PRIMARY KEY (`id`)
    );
    """

    def __init__(self, form, user_id=-1):
        super().__init__(form)
        self.content = form.get('content', '')
        self.user_id = form.get('user_id', user_id)
        self.weibo_id = int(form.get('weibo_id', -1))

    def user(self):
        u = User.one(id=self.user_id)
        return u

    def weibo(self):
        w = Weibo.one(id=self.weibo_id)
        return w


from models.weibo import Weibo



