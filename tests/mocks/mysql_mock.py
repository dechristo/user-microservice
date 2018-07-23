class MysqlMock():

    def autocommit(self, value):
        self.is_auto_commit = value

    def cursor(self):
        return {}