from config.database_config import DatabaseConnector
from user.models.adminmodels import Admin
import mysql.connector

class admincontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_admin(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from admin")
            results = cursor.fetchall()
            cursor.close()
            
            user_list=[]
            for user in results:
                user = Admin(user['id'],user['username'],user['password'],user['nidn'],user['gender'],user['status'])
                user_list.append(user)
                
            return user_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_admin(self):
        all_user = self.get_all_admin()
        if all_user is not None:
            user_data = [user.to_dict() for user in all_user]
            return {'user': user_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data user'}, 500
        
    def tambah_admin(self,data):
        try:
            username=data.get('username')
            password=data.get('password')
            nidn=data.get('nidn')
            gender=data.get('gender')
            status=data.get('status')
            
            cursor = self.db.cursor()
            query = "insert into admin (username, password, nidn, gender, status) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(query, (username, password, nidn, gender, status))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data user telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data user '}, 500