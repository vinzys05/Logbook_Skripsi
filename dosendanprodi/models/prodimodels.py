class Prodi:
    def __init__(self,id, prodi):
        self.id = id
        self.prodi = prodi
        
    @staticmethod
    def from_dict(data):
        
        return Prodi(
            id=data['id'],
            prodi=data['prodi']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'prodi': self.prodi
        }