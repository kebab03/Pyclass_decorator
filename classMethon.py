class Seed:
       count_seed=0 #class varibale
       def __init__(self,nam):
              self.Name=nam   #instance variable  
              Seed.count_seed +=1
              #Seed.count_seed=Seed.count_seed+1
              print(nam+'  is created')
mango=Seed('Amm')
print(mango.Name)
print(Seed.count_seed)

jam=Seed('Jam')
print(jam.Name)
print(jam.count_seed)


Pepe=Seed('pepe')
print(Pepe.Name)
print(Seed.count_seed)



              
              
