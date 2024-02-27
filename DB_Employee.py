from sqlalchemy import create_engine
from sqlalchemy.sql import text

class DB_Employee:
    scripts = {
        'select': text('select * from employee WHERE company_id = :company_id'),
        # 'get max id': text(),
        'delete company by id': text('delete from company where id = :id_to_delete'),
        'delete last employee': text('DELETE FROM employee WHERE id = (SELECT MAX(id) FROM employee)')
    }

    db_connection_string = 'postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet'

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self, id):
        return self.db.execute(self.scripts['select'], company_id=id).fetchall()

    def get_max_id(self):
        return self.db.execute(self.scripts['get max id']).fetchall()[0][0]

    def delete_company(self, id):
        self.db.execute(self.scripts['delete company by id'], id_to_delete=id)

    def delete_employee(self):
        return self.db.execute(self.scripts['delete last employee'])