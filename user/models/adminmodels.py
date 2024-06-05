class Admin:
    def __init__(self,id, username, password, nidn, gender, status):
        self.id = id
        self.username = username
        self.password = password
        self.nidn = nidn
        self.gender = gender
        self.status = status
        
    @staticmethod
    def from_dict(data):
        
        return Admin(
            id=data['id'],
            username=data['username'],
            password=data['password'],
            nidn=data['nidn'],
            gender=data['gender'],
            status=data['status']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'username':self.username,
            'password':self.password,
            'nidn': self.nidn,
            'gender': self.gender,
            'status': self.status
        }