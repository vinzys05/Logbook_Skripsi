from config.database_config import DatabaseConnector
from dosendanprodi.models.prodimodels import Prodi
import mysql.connector

class prodicontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_prodi(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from program_studi")
            results = cursor.fetchall()
            cursor.close()
            
            prodi_list=[]
            for prodi in results:
                prodi = Prodi(prodi['id'],prodi['prodi'])
                prodi_list.append(prodi)
                
            return prodi_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_prodi(self):
        all_prodi = self.get_all_prodi()
        if all_prodi is not None:
            prodi_data = [prodi.to_dict() for prodi in all_prodi]
            return {'prodi': prodi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data prodi'}, 500
        
    def tambah_prodi(self,data):
        try:
            prodi=data.get('prodi')
            
            cursor = self.db.cursor()
            query = "insert into program_studi (prodi) VALUES (%s)"
            cursor.execute(query, (prodi,))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data prodi telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data prodi '}, 500
        
    def update_prodi(self,id,data):
        try:
            if not data:
                return {'massage' : 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from program_studi where id = %s"
            cursor.execute(query, (id,))
            prodi = cursor.fetchone()
            cursor.close()
            
            if not prodi:
                return{'massage' : 'Data prodi tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update program_studi SET prodi = %s where id = %s"
            cursor.execute(query, (data['prodi'], id))
            self.db.commit()
            cursor.close()
            
            return {'masssage':'Data prodi berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print (f"Error: {e}")
            return{'massage':'Terjadi kesalahan saat memperbarui data prodi'}, 500
        
    def hapus_prodi(self,id):
        try:
            cursor = self.db.cursor()
            query = "delete from program_studi where id = %s"
            cursor.execute(query, (id,))
            self.db.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            
            if affected_rows > 0:
                return{'massage':'Data prodi berhasil di hapus'}, 200
            else:
                return{'massage':'Data prodi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f'Error: {e}')
            return{'massage': 'Terjadi kesalahan saat menghapus data prodi'}, 500