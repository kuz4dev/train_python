# -------------------------------------------------
# базовая атк оружия
class Weapon:
    def __init__(self, w_base_atk):
        self.w_base_atk = w_base_atk
        
# 
class Claymore(Weapon):     
    def buff(ch_class, base_atk):         
        if ch_class == "воин":             
            base_atk += 8         
        else:             
            base_atk += 3  

        return base_atk

# бафф для лука бард\иной 
class Bow(Weapon):     
    def buff(ch_class, base_atk, charisma):         
        if ch_class == "бард":             
            base_atk += 5             
            charisma += 3         
        else:             
            base_atk += 3  

        return base_atk, charisma
        
# бафф для посоха маг\иной 
class Wand(Weapon):         
    def buff(self, ch_class, base_atk, mana):         
        if ch_class == "маг":             
            base_atk += 5             
            mana += 3         
        else:             
            base_atk += 3  

        return base_atk, mana

            
# бафф для ножа вор\иной 
class Knife(Weapon):     
    def buff(ch_class, base_atk, agility):         
        if ch_class == "маг":             
            base_atk += 5             
            agility += 3         
        else:             
            base_atk += 3

        return base_atk, agility