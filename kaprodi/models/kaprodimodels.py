class Kapordi:
    def __init__(self,id, npm, validasi_kaprodi, nama, konsultasi, nidn):
        self.id = id
        self.npm = npm
        self.validasi_kaprodi = validasi_kaprodi
        self.nama = nama
        self.konsultasi = konsultasi
        self.nidn = nidn
        
    @staticmethod
    def from_dict(data):
        
        return Kapordi(
            id=data['id'],
            npm=data['npm'],
            validasi_kaprodi=data['validasi_kaprodi'],
            nama=data['nama'],
            konsultasi=data['konsultasi'],
            nidn=data['nidn']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'npm':self.npm,
            'validasi_kaprodi':self.validasi_kaprodi,
            'nama': self.nama,
            'konsultasi':self.konsultasi,
            'nidn': self.nidn
        }