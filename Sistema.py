from Cliente import Cliente
from Pet import Pet

c1 = Cliente(1, "Rodrigo", 29, "83988276325","Avenida Elpidio de almeida", "01577269403")
c2 = Cliente(2, "Aline", 22,  "83987249255","Rua Henrique Sáles MonteiroCampina", "33322211100")

pet1 = Pet(1, "Marley", "Labrador", "Cachorro")
pet2 = Pet(1, "Luna", "Salmoieda", "Cachorro")

c1.adicionaPets(pet1)
c1.adicionaPets(pet2)

#c1.toString()
#print(30*"-")
c1.mostraListaDePets()