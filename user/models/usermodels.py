class User:
    def __init__(self,id, username, password, npm, gender, status):
        self.id = id
        self.username = username
        self.password = password
        self.npm = npm
        self.gender = gender
        self.status = status
        
    @staticmethod
    def from_dict(data):
        
        return User(
            id=data['id'],
            username=data['username'],
            password=data['password'],
            npm=data['npm'],
            gender=data['gender'],
            status=data['status']
        )
        
    def to_dict(self):
        
        return {
            'id': self.id,
            'username':self.username,
            'password':self.password,
            'npm': self.npm,
            'gender': self.gender,
            'status': self.status
        }