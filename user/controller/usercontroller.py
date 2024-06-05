from config.database_config import DatabaseConnector
from user.models.usermodels import User
import mysql.connector

class usercontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_user(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from user")
            results = cursor.fetchall()
            cursor.close()
            
            user_list=[]
            for user in results:
                user = User(user['id'],user['username'],user['password'],user['npm'],user['gender'],user['status'])
                user_list.append(user)
                
            return user_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_user(self):
        all_user = self.get_all_user()
        if all_user is not None:
            user_data = [user.to_dict() for user in all_user]
            return {'user': user_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data user'}, 500
        
    def tambah_user(self,data):
        try:
            username=data.get('username')
            password=data.get('password')
            npm=data.get('npm')
            gender=data.get('gender')
            status=data.get('status')
            
            cursor = self.db.cursor()
            query = "insert into user (username, password, npm, gender, status) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(query, (username, password, npm, gender, status))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data user telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data user '}, 500