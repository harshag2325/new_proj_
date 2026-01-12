import dao

class services:
    def get_data(self):
        data_list = dao.connect()
        self.data = []
        for i in data_list:
            self.data.append(i)
        return self.data
    def get_certain_data(self, id):
        data_list = dao.connect()
        self.data = []
        for i in data_list:
            if i.get("id")==id:
                self.data.append(i)
        return self.data
    def create_car(self, name, milege, model, id, color):
        if dao.get_connection_insert(name, milege, model, id, color):
            return True
        return False
    def modify_car(self, id, type, val):
        if dao.get_connection_update(id, type, val):
            return True
        return False
    def delete_car(self, id):
        if dao.get_connection_delete(id):
            return True
        return False
