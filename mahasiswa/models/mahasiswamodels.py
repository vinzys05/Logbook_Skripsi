class mahasiswa:
    def __init__(self,id, npm, prodi, nama):
        self.id = id
        self.npm = npm
        self.prodi = prodi
        self.nama = nama
        
    @staticmethod
    def from_dict(data):
        
        return mahasiswa(
            id=data['id'],
            npm=data['npm'],
            prodi=data['prodi'],
            nama=data['nama']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'npm': self.npm,
            'prodi': self.prodi,
            'nama': self.nama
            
        }