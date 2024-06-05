class Dosen:
    def __init__(self,id, nidn, nama):
        self.id = id
        self.nidn = nidn
        self.nama = nama
        
    @staticmethod
    def from_dict(data):
        
        return Dosen(
            id=data['id'],
            nidn=data['nidn'],
            nama=data['nama']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'nidn': self.nidn,
            'nama': self.nama
        }