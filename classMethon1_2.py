class Seed:
       count_seed=0 #class varibale
       def __init__(self,nam):
              self.Name=nam   #instance variable  
              Seed.count_seed +=1
              #Seed.count_seed=Seed.count_seed+1
              print(nam+'  is created')
       def descrip(self):
              print(self.Name+" 's desciption")  
mango=Seed('Amm')
print(mango.Name)
print(Seed.count_seed)
mango.descrip()


















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
