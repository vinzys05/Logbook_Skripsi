from config.database_config import DatabaseConnector
from kaprodi.models.kaprodimodels import Kapordi
import mysql.connector

class kaprodicontroller:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_kaprodi(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from kaprodi")
            results = cursor.fetchall()
            cursor.close()
            
            kaprodi_list=[]
            for kaprodi in results:
                kaprodi = Kapordi(kaprodi['id'],kaprodi['npm'],kaprodi['validasi_kaprodi'],kaprodi['nama'],kaprodi['konsultasi'],kaprodi['nidn'])
                kaprodi_list.append(kaprodi)
                
            return kaprodi_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    def lihat_kaprodi(self):
        all_kaprodi = self.get_all_kaprodi()
        if all_kaprodi is not None:
            kaprodi_data = [kaprodi.to_dict() for kaprodi in all_kaprodi]
            return {'kaprodi': kaprodi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data kaprodi'}, 500
        
    def cari_kaprodi(self,id):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from kaprodi where id = %s", (id,))
            kaprodi = cursor.fetchone()
            cursor.close()
            
            if kaprodi:
                kaprodiobj = Kapordi(kaprodi['id'],kaprodi['npm'],kaprodi['validasi_kaprodi'],kaprodi['nama'],kaprodi['konsultasi'],kaprodi['nidn'])
                return {'kaprodi': kaprodiobj.to_dict()}, 200
            else:
                return {'massage': 'Data kaprodi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat mencari data kaprodi '}, 500
        
    def tambah_kaprodi(self,data):
        try:
            npm=data.get('npm')
            validasi_kaprodi=data.get('validasi_kaprodi')
            nama=data.get('nama')
            konsultasi=data.get('konsultasi')
            nidn=data.get('nidn')
            
            cursor = self.db.cursor()
            query = "insert into kaprodi (npm, validasi_kaprodi, nama, konsultasi, nidn) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(query, (npm, validasi_kaprodi, nama, konsultasi, nidn))
            self.db.commit()
            cursor.close()
            
            return {'massage': 'Data kaprodi telah ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat menambahkan data kaprodi '}, 500
        
    def update_kaprodi(self,id,data):
        try:
            if not data:
                return {'massage' : 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from kaprodi where id = %s"
            cursor.execute(query, (id,))
            kaprodi = cursor.fetchone()
            cursor.close()
            
            if not kaprodi:
                return{'massage' : 'Data kaprodi tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "Update kaprodi SET npm = %s, validasi_kaprodi = %s, nama = %s, konsultasi = %s, nidn = %s where id = %s"
            cursor.execute(query,(data['npm'],data['validasi_kaprodi'],data['nama'],data['konsultasi'],data['nidn'], id))
            self.db.commit()
            cursor.close()
            
            return {'masssage':'Data kaprodi berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print (f"Error: {e}")
            return{'massage':'Terjadi kesalahan saat memperbarui data kaprodi'}, 500