from config.database_config import DatabaseConnector
from skripsi.models.skripsimodels import Skripsi
import mysql.connector

class skripsicontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_skripsi(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from skripsi")
            results = cursor.fetchall()
            cursor.close()
            
            skripsi_list=[]
            for skripsi in results:
                skripsi = Skripsi(skripsi['id'],skripsi['judul_skripsi'],skripsi['npm'],skripsi['prodi'],skripsi['konsultasi_pembimbing'])
                skripsi_list.append(skripsi)
                
            return skripsi_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_skripsi(self):
        all_skripsi = self.get_all_skripsi()
        if all_skripsi is not None:
            skripsi_data = [skripsi.to_dict() for skripsi in all_skripsi]
            return {'skripsi': skripsi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data skripsi'}, 500
        
    def cari_skripsi(self,id):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from skripsi where id = %s", (id,))
            skripsi = cursor.fetchone()
            cursor.close()
            
            if skripsi:
                skripsiobj = Skripsi(skripsi['id'],skripsi['judul_skripsi'],skripsi['npm'],skripsi['prodi'],skripsi['konsultasi_pembimbing'])
                return {'skripsi': skripsiobj.to_dict()}, 200
            else:
                return {'massage': 'Data skripsi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat mencari data skripsi '}, 500
        
    def tambah_skripsi(self,data):
        try:
            judul_skripsi=data.get('judul_skripsi')
            npm=data.get('npm')
            prodi=data.get('prodi')
            konsultasi_pembimbing=data.get('konsultasi_pembimbing')
            
            cursor = self.db.cursor()
            query = "insert into skripsi (judul_skripsi, npm, prodi, konsultasi_pembimbing) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (judul_skripsi, npm, prodi, konsultasi_pembimbing))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data skripsi telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data skripsi '}, 500
        
    def update_skripsi(self,id,data):
        try:
            if not data:
                return {'massage' : 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from skripsi where id = %s"
            cursor.execute(query, (id,))
            skripsi = cursor.fetchone()
            cursor.close()
            
            if not skripsi:
                return{'massage' : 'Data skripsi tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update skripsi SET judul_skripsi = %s , npm = %s, prodi = %s, konsultasi_pembimbing = %s where id = %s"
            cursor.execute(query, (data['judul_skripsi'],data['npm'], data['prodi'], data['konsultasi_pembimbing'], id))
            self.db.commit()
            cursor.close()
            
            return {'masssage':'Data skripsi berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print (f"Error: {e}")
            return{'massage':'Terjadi kesalahan saat memperbarui data skripsi'}, 500