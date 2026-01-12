from dao import connect
data_list = connect()
class services:
    def get_data(self):
        self.data = []
        for i in data_list:
            self.data.append(i)
        return self.data
