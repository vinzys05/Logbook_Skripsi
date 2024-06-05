from config.database_config import DatabaseConnector 
from mahasiswa.models.mahasiswamodels import mahasiswa
import mysql.connector

class mahasiswacontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_mahasiswa(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from mahasiswa")
            results = cursor.fetchall()
            cursor.close()
            
            mahasiswa_list=[]
            for Mahasiswa in results:
                Mahasiswa = mahasiswa(Mahasiswa['id'],Mahasiswa['npm'],Mahasiswa['prodi'],Mahasiswa['nama'])
                mahasiswa_list.append(Mahasiswa)
                
            return mahasiswa_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_mahasiswa(self):
        all_mahasiswa = self.get_all_mahasiswa()
        if all_mahasiswa is not None:
            mahasiswa_data = [Mahasiswa.to_dict() for Mahasiswa in all_mahasiswa]
            return {'mahasiswa': mahasiswa_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data mahasiswa'}, 500
        
    def cari_mahasiswa(self,id):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from mahasiswa where id = %s", (id,))
            Mahasiswa = cursor.fetchone()
            cursor.close()
            
            if Mahasiswa:
                Mahasiswaobj = mahasiswa(Mahasiswa['id'],Mahasiswa['npm'],Mahasiswa['prodi'],Mahasiswa['nama'])
                return {'Mahasiswa': Mahasiswaobj.to_dict()}, 200
            else:
                return {'massage': 'Data mahasiswa tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat mencari data mahasiswa '}, 500
        
    def tambah_mahasiswa(self,data):
        try:
            npm=data.get('npm')
            prodi=data.get('prodi')
            nama=data.get('nama')
            
            cursor = self.db.cursor()
            query = "insert into mahasiswa (npm, prodi, nama) VALUES (%s, %s, %s)"
            cursor.execute(query, (npm, prodi, nama))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data mahasiswa telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data mahasiswa '}, 500
        
    def update_mahasiswa(self,id,data):
        try:
            if not data:
                return {'massage' : 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from mahasiswa where id = %s"
            cursor.execute(query, (id,))
            Mahasiswa = cursor.fetchone()
            cursor.close()
            
            if not Mahasiswa:
                return{'massage' : 'Data mahasiswa tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update mahasiswa SET npm = %s, prodi = %s, nama = %s where id = %s"
            cursor.execute(query, (data['npm'], data['prodi'], data['nama'], id))
            self.db.commit()
            cursor.close()
            
            return {'masssage':'Data mahasiswa berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print (f"Error: {e}")
            return{'massage':'Terjadi kesalahan saat memperbarui data mahasiswa'}, 500