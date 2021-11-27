
#%%

import os,shutil
import numpy as np
if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")

from data import data
from pets import Pet
from foods import Food
from store import Store
from teams import Team,TeamSlot
from fight import Fight

            
# %%

################################################################################
### Testing Food
################################################################################
f0 = Food()
f1 = Food("honey")
f2 = Food("apple")
f3 = Food("steak")
### Construct all possible foods
for temp_food in data["foods"]:
    Food(temp_food)

#%%

################################################################################
### Testing pets
################################################################################
p0 = Pet()
p1 = Pet("pet-ant")
p2 = Pet("pet-dodo")
p3 = Pet("pet-dragon")
p4 = Pet("pet-dragon")
p4.health += 1
### Construct all possible pets
for temp_pet in data["pets"]:
    p = Pet(temp_pet)
    p.copy()
    
#%%

################################################################################
### Eating food 
################################################################################
p1.eat(f1)
p1.eat(f2)
p1.eat(f3)

#%%

################################################################################
### Constructing Teams
################################################################################
ts = TeamSlot(p1)
t = Team()
t = Team([x for x in t])

t[0] = p1
t[1] = p2
t[2] = p3
t[4] = p4

## Test shallow copy of team
tc = Team([x for x in t])
tc.move(0,3)

### Test move_forward
tf = Team([], fight=True)
tf[-1] = p1
tf[-2] = p2
tf.move_forward()

#%%

################################################################################
### Testing abilities of all animals
################################################################################
%run /Users/ibier/Software/sapai/sapai/effects.py
### Testing all effects
t1 = Team([Pet("pet-fish")])
for temp_pet in data["pets"]:
    p = Pet(temp_pet)
    p.level = 2
    tt0 = Team([p.copy(),p.copy(),p.copy(),p.copy(),p.copy()], fight=False)
    tt1 = t1.copy()
    
    effect = p.ability["effect"]
    kind = effect["kind"]
    func = get_effect_function(kind)
    
    print(kind)
    pet_idx = (0,0)
    teams = [tt0, tt1]
    print(tt0)
    func(pet_idx, teams)
    print(tt0)
    


# %%

################################################################################
### Fights
################################################################################

%run /Users/ibier/Software/sapai/sapai/fight.py
### Testing all effects
t1 = Team([Pet("pet-fish")])
for temp_pet in data["pets"]:
    if temp_pet != "pet-dodo":
        continue
    
    temp_t0 = Team([Pet(temp_pet)])
    temp_t1 = Team([x for x in t1])
    
    f = Fight(temp_t0, temp_t1)
    f.start()
    break

# f = Fight(t, t)

    
# %%

### Construct all possible pets
triggers = []
kind = []
target = []
to = []
amount = []
pets = {}
for temp_pet in data["pets"]:
    p = Pet(temp_pet)
    # if "StartOfBattle" == p.ability["trigger"]:
    effect = p.ability["effect"]
    kind.append(effect["kind"])
    if "target" in effect:
        target.append(effect["target"]["kind"])
    elif "to" in effect:
        ### "to" is literally the same as "target". Why call it two different
        ### things.
        to.append(effect["to"])
    if "amount" in effect:
        amount.append(effect["amount"])
    else:
        amount.append(0)
    
    pets[temp_pet] = p
        

#%%



################################################################################
### Store
################################################################################
s = Store()
s.roll()
s.next_turn()
for i in range(100):
    print(s.roll())


#%%

# %%