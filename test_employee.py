from employee import Employee
from DB_Employee import DB_Employee

api = Employee('https://x-clients-be.onrender.com')
db = DB_Employee(('postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet'))
def test_get_employee_list():
    result = api.create_company(name='DannyQA', description='blabla')
    new_id = result['id']
    response = api.get_employee_list(parametres_to_add={'company': new_id})
    db_result = db.get_employees(new_id)

    db.delete_company(new_id)

    assert response.status_code == 200
    json_response = response.json()
    assert len(db_result) == len(json_response)


def test_create_new_employee():

    result = api.create_company(name='DannyQA1098', description='blabla1')
    company_id = result['id']
    employee_data = api.create_employee_data("Danny", "Test", "testing", "+79991234567", "dan2000@gmail.com", "2000-10-11", "www.path.com", company_id)
    response = api.create_employee(employee_data)

    assert response.status_code == 201

    data = api.get_employee_list(parametres_to_add={'company': company_id}).json()
    db_result = db.get_employees(company_id)
    db.delete_employee()
    db.delete_company(company_id)

    assert len(data) == len(db_result)
    assert data[0]['firstName'] == db_result[0]['first_name']
    assert data[0]['lastName'] == db_result[0]['last_name']


def test_get_employee_by_id():
    result = api.create_company(name='DannyQA2', description='blabla2')
    company_id = result['id']

    employee_data = api.create_employee_data("Danny", "Test", "testing", "+79991234567", "dan2000@gmail.com", "2000-10-11", "www.path.com", company_id)
    employee_id = api.create_employee(employee_data).json()['id']
    new_employee = api.get_employee_id(employee_id)

    db_result = db.get_employees(company_id)

    assert new_employee.status_code == 200

    json_response = new_employee.json()
    db.delete_employee()
    db.delete_company(company_id)

    assert json_response['firstName'] == db_result[0]['first_name']
    assert json_response['lastName'] == db_result[0]['last_name']


def test_edit_employee():

    result = api.create_company(name='DannyQA3', description='blabla3')
    company_id = result['id']
    employee_data = api.create_employee_data("Danny", "Test", "testing", "+79991234567", "dan2000@gmail.com", "2000-10-11", "www.path.com", company_id)
    employee_id = api.create_employee(employee_data).json()['id']

    update_data = api.create_update_data("Новая Фамилия", "новый_email@example.com", "новый_url", "новый_телефон", True)
    response = api.update_employee(employee_id, update_data)

    assert response.status_code == 200

    json_response = api.update_employee(employee_id, update_data).json()
    db_result = db.get_employees(company_id)
    db.delete_employee()
    db.delete_company(company_id)

    assert json_response['email'] == db_result[0]['email']
    assert json_response['url'] == db_result[0]['avatar_url']
