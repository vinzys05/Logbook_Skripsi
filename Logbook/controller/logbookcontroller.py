import base64
 
from flask import request
from config.database_config import DatabaseConnector 
from Logbook.models.logbookmodels import Logbook
from datetime import datetime, timedelta
import mysql.connector


class logbookController:
    def __init__(self):
        self.db_connector = DatabaseConnector() 
        self.db = self.db_connector.connect_to_database()
        
    def get_all_logbook(self):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from logbook")
            results = cursor.fetchall()
            cursor.close()
            
            logbook_list=[] 
            for logbook in results:
                
                tanggal_sumbit = logbook['tanggal_sumbit']
                if isinstance(tanggal_sumbit, timedelta):
                    tanggal_sumbit = datetime.now() - tanggal_sumbit
                logbook = Logbook(logbook['id'], logbook['npm'], logbook['judul_skripsi'], logbook['tanggal'], logbook['permasalahan_skripsi'],logbook['solusi'], logbook['tugas_minggu_depan'], logbook['pendapaet_pembimbing'], logbook['progress_skripsi'], logbook['status_validasi'], logbook['id_bimbingan'], logbook['id_skripsi'], tanggal_sumbit) 
                logbook_list.append(logbook)
            
            return logbook_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
     # melihat dengan json
    def lihat_logbook(self):
        all_logbook = self.get_all_logbook()
        if all_logbook is not None:
            logbook_data = [logbook.to_dict() for logbook in all_logbook]
            return {'logbook': logbook_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data logbook'}, 500
        
    def cari_logbook(self,id):
        try:
            cursor =self.db.cursor(dictionary=True)
            cursor.execute("select * from logbook where id = %s", (id,))
            logbook = cursor.fetchone()
            cursor.close()
            
            if logbook:
                tanggal_sumbit = logbook['tanggal_sumbit']
                if isinstance(tanggal_sumbit, timedelta):
                    tanggal_sumbit = datetime.now() - tanggal_sumbit
                logbookobj = Logbook(logbook['id'], logbook['npm'], logbook['judul_skripsi'], logbook['tanggal'], logbook['permasalahan_skripsi'],logbook['solusi'], logbook['tugas_minggu_depan'], logbook['pendapaet_pembimbing'], logbook['progress_skripsi'], logbook['status_validasi'], logbook['id_bimbingan'], logbook['id_skripsi'], tanggal_sumbit) 
                return {'logbook': logbookobj.to_dict()}, 200
            else:
                return {'massage': 'Data logbook tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return{'massage': 'Terjadi kesalahan saat mencari data logbook '}, 500
        
    def tambah_logbook(self, data):
        try:
            # Handle file upload
            #file = request.files['progress_skripsi']
            #file_data = file.read()
            #encoded_file_data = base64.b64encode(file_data).decode('utf-8')
            #data['progress_skripsi'] = encoded_file_data
            npm=data['npm'],
            judul_skripsi=data['judul_skripsi'],
            tanggal=data['tanggal'],
            permasalahan_skripsi=data['permasalahan_skripsi'],
            solusi=data['solusi'],
            tugas_mingdep=data['tugas_minggu_depan'],
            pendapat_pembimbing=data['pendapat_pembimbing'],
            progress_skripsi=data['progress_skripsi'],
            status_validasi=data['status_validasi'],
            id_bimbingan=data['id_bimbingan'],
            id_skripsi=data['id_skripsi'],
            tanggal_sumbit = datetime.now()
            

            cursor = self.db.cursor()
            query="""INSERT INTO logbook ( npm, judul_skripsi, tanggal, permasalahan_skripsi, solusi, tugas_minggu_depan, pendapat_pembimbing, progress_skripsi, status_validasi, id_bimbingan, id_skripsi, tanggal_sumbit) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (id, npm, judul_skripsi, tanggal, permasalahan_skripsi, solusi, tugas_mingdep, pendapat_pembimbing, progress_skripsi, status_validasi, id_bimbingan, id_skripsi ,tanggal_sumbit))
            self.db.commit()
            cursor.close()
            
            
            return {'message': 'Logbook berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambahkan logbook'}, 500
        
    def update_logbook(self, id, data):
        try:
            if 'progress_skripsi' in request.files:
                file = request.files['progress_skripsi']
                file_data = file.read()
                encoded_file_data = base64.b64encode(file_data).decode('utf-8')
                data['progress_skripsi'] = encoded_file_data
            
            logbook = Logbook.from_dict(data)
            cursor = self.db.cursor()
            cursor.execute("""
                UPDATE logbook SET npm = %s, judul_skripsi = %s, tanggal = %s, permasalahan_skripsi = %s, solusi = %s, tugas_minggu_depan = %s, pendapat_pembimbing = %s, progress_skripsi = %s, status_validasi = %s, id_bimbingan = %s, id_skripsi = %s, tanggal_sumbit = %s
                WHERE id = %s
            """, (
                logbook.npm, logbook.judul_skripsi, logbook.tanggal, logbook.permasalahan_skripsi, logbook.solusi, logbook.tugas_mingdep, logbook.pendapat_pembimbing, logbook.progress_skripsi, logbook.status_validasi, logbook.id_bimbingan, logbook.id_skripsi, logbook.tanggal_sumbit, id
            ))
            self.db.commit()
            cursor.close()
            return {'message': 'Logbook berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui logbook'}, 500