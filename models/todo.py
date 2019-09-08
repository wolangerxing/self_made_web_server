from models.model_basic import SQLModel


class Todo(SQLModel):

    sql_create = """
    CREATE TABLE `Todo` (
        `id`         INT NOT NULL AUTO_INCREMENT,
        `title`      VARCHAR(255) NOT NULL,
        `user_id`    INT NOT NULL,
        PRIMARY KEY (`id`)
    );
    """

    def __init__(self, form):
        super().__init__(form)
        self.title = form.get('title', '')
        self.user_id = form.get('user_id', -1)

    @classmethod
    def add(cls, form, user_id):
        form['user_id'] = user_id
        t = Todo.new(form)
        return t
