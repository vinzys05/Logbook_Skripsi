from datetime import datetime
class Logbook:
    def __init__(self,id, npm, judul_skripsi, tanggal, permasalahan_skripsi, solusi, tugas_mingdep, pendapat_pembimbing, progress_skripsi, status_validasi, id_bimbingan, id_skripsi,tanggal_sumbit=None ):
        self.id = id
        self.npm = npm
        self.judul_skripsi = judul_skripsi
        self.tanggal = tanggal
        self.permasalahan_skripsi = permasalahan_skripsi
        self.solusi = solusi
        self.tugas_mingdep = tugas_mingdep
        self.pendapat_pembimbing = pendapat_pembimbing
        self.progress_skripsi =progress_skripsi
        self.status_validasi = status_validasi
        self.id_bimbingan = id_bimbingan
        self.id_skripsi = id_skripsi  
        self.tanggal_sumbit = tanggal_sumbit.strftime("%Y-%m-%d %H:%M:%S") if tanggal_sumbit else None
        
    @staticmethod
    def from_dict(data):
        
        return Logbook(
            id=data['id'],
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
            tanggal_sumbit=datetime.strptime(data['tanggal_sumbit'], "%Y-%m-%d %H:%M:%S") if data.get('tanggal_sumbit') else None
            
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'judul_skripsi':self.judul_skripsi,
            'permasalahan_skripsi':self.permasalahan_skripsi,
            'solusi': self.solusi,
            'pendapat_pembimbing': self.pendapat_pembimbing,
            'progress_skripsi':self.progress_skripsi,
            'status_validasi':self.status_validasi,
            'id_bimbingan':self.id_bimbingan,
            'id_skripsi':self.id_skripsi,
            'tanggal_sumbit':self.tanggal_sumbit
        }
            