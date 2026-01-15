import random

# Soldier

class Soldier:
    
    def __init__(self, health:int, strength:int):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self) -> int:
        # your code here
        return self.strength

    def receiveDamage(self, damage:int):
        # your code here
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health:int, strength:int):
        # your code here
        super().__init__(health, strength)
        self.name = name
    
    def battleCry(self) -> str:
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage) -> str:
        # your code here
        super().receiveDamage(damage)
        if(self.health>0):
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

# Saxon

class Saxon(Soldier):
    def __init__(self, health:int, strength:int):
        super().__init__(health, strength)

    def receiveDamage(self, damage:int) -> str:
        # your code here
        super().receiveDamage(damage)
        if(self.health>0):
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"


# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy:list = []
        self.saxonArmy:list = []

    def addViking(self, viking:Viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon:Saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        Saxon_w = random.choice(self.saxonArmy)
        Viking_w = random.choice(self.vikingArmy)
        output_msg = Saxon_w.receiveDamage(Viking_w.strength)

        for s_w in self.saxonArmy:
            if(s_w.health<=0):
                self.saxonArmy.remove(s_w)

        return output_msg
    
    def saxonAttack(self): 
        # your code here
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        output_msg = Viking.receiveDamage(Saxon.strength)

        for v_w in self.vikingArmy:
            if(v_w.health<=0):
                self.vikingArmy.remove(v_w)

        return output_msg

    def showStatus(self):
        # your code here
        if(len(self.saxonArmy)==0):
            return "Vikings have won the war of the century!"
        
        elif(len(self.vikingArmy)==0):
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."