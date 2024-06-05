from config.database_config import DatabaseConnector
from dosendanprodi.models.dosenmodels import Dosen
import mysql.connector

class dosencontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_dosen(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from dosen")
            results = cursor.fetchall()
            cursor.close()
            
            dosen_list=[]
            for dosen in results:
                dosen = Dosen(dosen['id'],dosen['nidn'],dosen['nama'])
                dosen_list.append(dosen)
                
            return dosen_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_dosen(self):
        all_dosen = self.get_all_dosen()
        if all_dosen is not None:
            dosen_data = [dosen.to_dict() for dosen in all_dosen]
            return {'dosen': dosen_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data dosen'}, 500
        
    def cari_dosen(self,id):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from dosen where id = %s", (id,))
            dosen = cursor.fetchone()
            cursor.close()
            
            if dosen:
                dosenobj = Dosen(dosen['id'],dosen['nidn'],dosen['nama'])
                return {'dosen': dosenobj.to_dict()}, 200
            else:
                return {'massage': 'Data dosen tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat mencari data dosen '}, 500
        
    def tambah_dosen(self,data):
        try:
            nidn=data.get('nidn')
            nama=data.get('nama')
            
            cursor = self.db.cursor()
            query = "insert into dosen (nidn,nama) VALUES (%s,%s)"
            cursor.execute(query, (nidn,nama))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data dosen telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data dosen '}, 500
        
    def update_dosen(self,id,data):
        try:
            if not data:
                return {'massage' : 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from dosen where id = %s"
            cursor.execute(query, (id,))
            dosen = cursor.fetchone()
            cursor.close()
            
            if not dosen:
                return{'massage' : 'Data dosen tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update dosen SET nidn = %s, nama = %s where id = %s"
            cursor.execute(query, (data['nidn'], data['nama'] , id))
            self.db.commit()
            cursor.close()
            
            return {'masssage':'Data dosen berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print (f"Error: {e}")
            return{'massage':'Terjadi kesalahan saat memperbarui data dosen'}, 500
        
    def hapus_dosen(self,id):
        try:
            cursor = self.db.cursor()
            query = "delete from dosen where id = %s"
            cursor.execute(query, (id,))
            self.db.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            
            if affected_rows > 0:
                return{'massage':'Data dosen berhasil di hapus'}, 200
            else:
                return{'massage':'Data dosen tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f'Error: {e}')
            return{'massage': 'Terjadi kesalahan saat menghapus data dosen'}, 500