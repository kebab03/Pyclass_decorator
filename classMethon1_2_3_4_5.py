class Seed:
       count_seed=0 #Class varibale ,  static
       def __init__(self,nam):
              self.Name=nam   #Instance variable  
              Seed.count_seed +=1
              #Seed.count_seed=Seed.count_seed+1
              print(nam+'  is created')
       def descrip(self): # Instance Method (Function)
              print(self.Name+" 's desciption")
       @classmethod       
       def SeedNumber(cls): # class method 
              print("Creation of tree from seed :",cls.count_seed)
              print(cls.count_seed)
              
mango=Seed('Amm')
print(mango.Name)
#print(Seed.count_seed)
mango.descrip()

mango.SeedNumber()


Banna=Seed('Kola')


def world(year):
       print('hello guys of ', year)
world(2021)











