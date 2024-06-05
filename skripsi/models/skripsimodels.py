class Skripsi:
    def __init__(self,id, judul_skripsi, password, prodi, konsultasi_pembimbing):
        self.id = id
        self.judul_skripsi = judul_skripsi
        self.password = password
        self.prodi = prodi
        self.konsultasi_pembimbing = konsultasi_pembimbing
        
    @staticmethod
    def from_dict(data):
        
        return Skripsi(
            id=data['id'],
            judul_skripsi=data['judul_skripsi'],
            password=data['password'],
            prodi=data['prodi'],
            konsultasi_pembimbing=data['konsultasi_pembimbing']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'judul_skripsi':self.judul_skripsi,
            'password':self.password,
            'prodi': self.prodi,
            'konsultasi_pembimbing': self.konsultasi_pembimbing
        }
            