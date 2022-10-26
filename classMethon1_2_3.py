class Seed:
       count_seed=0 #Class varibale
       def __init__(self,nam):
              self.Name=nam   #Instance variable  
              Seed.count_seed +=1
              #Seed.count_seed=Seed.count_seed+1
              print(nam+'  is created')
       def descrip(self): # Instance Method (Function)
              print(self.Name+" 's desciption")
       def SeedNumber(cls):
              print("Creation of tree from seed ")
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
