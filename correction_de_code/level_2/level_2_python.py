class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
    
    def setAge(self, age):
        self.age = age
        return self
        
    def setSex(self, sex):
        self.sex = sex
        return self
        
    def setName(self, name):
        self.name = name
        return self
        
    def hello(self):
        return "Hello. My name is {}. I am {}. I am {}.".format(self.name, self.age, "male" if self.sex=='M' else "female")
