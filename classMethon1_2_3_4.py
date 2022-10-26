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
















jam=Seed('Jam')
print(jam.Name)
print(jam.count_seed)


Pepe=Seed('pepe')
print(Pepe.Name)
print(Seed.count_seed)

Pepe.SeedNumber()
class mango_seed:
       count_seed=0 #class varibale
       def __init__(self,nam):
              self.Name=nam   #instance variable  
              Seed.count_seed +=1
              #Seed.count_seed=Seed.count_seed+1
              print(nam+'  is created')
              
class tree(mango_seed):
       pass
yr=tree('Jambura')

