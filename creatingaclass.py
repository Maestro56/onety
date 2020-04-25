
class Giraffes():
    # TODO - create three functions for this class: move(), eat(), leaves from trees()
    def move(self):
        print('its_a_run')
    def eat(self):
        print('leaves_from_trees')
    pass

reginald = Giraffes()    
reginald.move()
reginald.eat()

class Things():
    pass

#creating a derived class (from base class)
class Inanimate(Things):
    pass

class Bacterium(Inanimate):
    pass
   
class infusorium(Bacterium):
    """ check if infusorium can move, eat or breathe"""
    def move(self):
        print('its_a_run')
    def eat(self):
        print('eat')
    def breathe(self):
        print('breathe')
    pass

one_ty = infusorium()
one_ty.move()
one_ty.eat()
one_ty.breathe()
                        
    



