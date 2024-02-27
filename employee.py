import requests
class Employee:

    def __init__(self, url):
        self.my_url = url

    def get_employee_list(self, parametres_to_add=None):
        responce = requests.get(f'{self.my_url}/employee', params=parametres_to_add)
        return responce

    def get_token(self, user="raphael", password="cool-but-crude"):
        auth_data = {
            "username": user,
            "password": password
        }
        resp = requests.post(f'{self.my_url}/auth/login', data=auth_data)
        return resp.json()['userToken']

    def create_company(self, name, description=''):
        company = {
            'name': name,
            'description': description
        }

        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        responce = requests.post(f'{self.my_url}/company', json=company, headers=my_headers)
        return responce.json()

    def create_employee(self, data):
        my_headers = {'x-client-token': self.get_token()}
        response = requests.post(f'{self.my_url}/employee', json=data, headers=my_headers)
        return response

    def get_employee_id(self, id):
        response = requests.get(f'{self.my_url}/employee/{id}')
        return response

    def update_employee(self, id, data):
        headers = {'x-client-token': self.get_token()}
        response = requests.patch(f'{self.my_url}/employee/{id}', json=data, headers=headers)
        return response

    def create_employee_data(self, first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id):
        return {
            "isActive": True,
            "createDateTime": "2024-02-20T20:42:58.623Z",
            "lastChangedDateTime": "2024-02-20T20:42:58.623Z",
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "phone": phone,
            "email": email,
            "birthdate": birthdate,
            "avatar_url": avatar_url,
            "companyId": company_id
        }

    def create_update_data(self, last_name, email, url, phone, is_active):
        return {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": is_active
        }