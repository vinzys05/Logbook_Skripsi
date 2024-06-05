class Management:
    def __init__(self,id, npm, nidn, nama, konsultasi):
        self.id = id
        self.npm = npm
        self.nidn = nidn
        self.nama = nama
        self.konsultasi =konsultasi
        
    @staticmethod
    def from_dict(data):
        
        return Management(
            id=data['id'],
            npm=data['npm'],
            nidn=data['nidn_dosen'],
            nama=data['nama_dosen'],
            konsultasi=data['konsultasi_pembimbing']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'npm': self.npm,
            'nidn_dosen': self.nidn,
            'nama_dosen': self.nama,
            'konsultasi_pembimbing':self.konsultasi
        }