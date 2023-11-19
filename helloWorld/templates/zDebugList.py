
model_fields = ['id', 'year', 'make', 'model']


class Automobile():
    # Class variable
    id = 0
    year = 0
    make = 'test'
    model = 'test'
    
    def __init__(self, id, year, make, model):
        self.id = id
        self.year = year
        self.make = make
        self.model = model


# create object
c1 = Automobile(1, 2022, 'Nissan', 'GTR')
c2 = Automobile(2, 2022, 'Lexus', 'IS500')

object_list = [c1, c2]

for car in object_list:
    for field in model_fields:
        print(car.__getattribute__(field))