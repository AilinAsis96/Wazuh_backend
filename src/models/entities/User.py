
class User():

    def __init__(self, id,name = None, username=None, email= None, adress=None, phone=None, website=None, company=None) -> None:
        self.id=id
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company
    
    def to_JSON(self):
        return{
            'id':self.id,
            'name':self.name,
            'username': self.username,
            'email':self.email,
            'address': self.address,
            'phone':self.phone,
            'website':self.website,
            'company':self.company

        }