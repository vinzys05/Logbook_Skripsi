from config.database_config import DatabaseConnector 
from management_pembimbing.models.managementmodels import Management
import mysql.connector

class managementcontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_management(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from management_pembimbing")
            results = cursor.fetchall()
            cursor.close()
            
            management_list=[]
            for management in results:
                management = Management(management['id'],management['npm'],management['nidn'],management['nama'],management['konsultasi_pembimbing'])
                management_list.append(management)
                
            return management_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_management(self):
        all_management = self.get_all_management()
        if all_management is not None:
            management_data = [management.to_dict() for management in all_management]
            return {'management': management_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data management'}, 500
        
    def cari_management(self,id):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from management_pembimbing where id = %s", (id,))
            management = cursor.fetchone()
            cursor.close()
            
            if management:
                managementobj = Management(management['id'],management['npm'],management['nidn'],management['nama'],management['konsultasi_pembimbing'])
                return {'management': managementobj.to_dict()}, 200
            else:
                return {'massage': 'Data management tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat mencari data management '}, 500
        
    def tambah_management(self,data):
        try:
            npm=data.get('npm')
            nidn=data.get('nidn')
            nama=data.get('nama')
            konsultasi=data.get('konsultasi_pembimbing')
            
            
            cursor = self.db.cursor()
            query = "insert into management_pembimbing (npm, nidn, nama, konsultasi_pembimbing) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (npm, nidn, nama, konsultasi))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data management telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data management '}, 500
        
    def update_management(self,id,data):
        try:
            if not data:
                return {'massage' : 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from management_pembimbing where id = %s"
            cursor.execute(query, (id,))
            management = cursor.fetchone()
            cursor.close()
            
            if not management:
                return{'massage' : 'Data management tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update management_pembimbing SET npm = %s, nidn = %s, nama = %s, konsultasi_pembimbing = %s where id = %s"
            cursor.execute(query, (data['npm'], data['nidn'], data['nama'], data['konsultasi_pembimbing'], id))
            self.db.commit()
            cursor.close()
            
            return {'masssage':'Data management berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print (f"Error: {e}")
            return{'massage':'Terjadi kesalahan saat memperbarui data management'}, 500