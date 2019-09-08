from models.model_basic import SQLModel
from models.comment import Comment
from models.user import User


class Weibo(SQLModel):
    sql_create = """
    CREATE TABLE `Weibo` (
        `id`         INT NOT NULL AUTO_INCREMENT,
        `content`    VARCHAR(255) NOT NULL,
        `user_id`    INT NOT NULL,
        PRIMARY KEY (`id`)
    );
    """

    def __init__(self, form):
        super().__init__(form)
        self.content = form.get('content', '')
        self.user_id = form.get('user_id', None)

    @classmethod
    def add(cls, form, user_id):
        form['user_id'] = user_id
        w = Weibo.new(form)
        return w

    def comments(self):
        cs = Comment.all(weibo_id=self.id)
        return cs

    def user(self):
        u = User.one(id=self.user_id)
        return u
