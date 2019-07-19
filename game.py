import random

class bcolors:
    Bold = "\033[1m"
    Underlined = "\033[4m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    End = "\033[0m"

class Person:
    def __init__(self, name, hp, mp, df, atk, magic, item):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk-10
        self.atk_h = atk+10
        self.df = df
        self.magic = magic
        self.item = item
        self.actions =["Attack", "Magic", "Action"]

    def get_name(self):
        return self.name

    def generate_dmg(self):
        return random.randrange(self.atk_l, self.atk_h)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_mp(self):
        return self.max_mp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.LightRed + bcolors.Bold + "Action" + bcolors.End)
        for items in self.actions:
            print("    "+str(i)+":", items)
            i +=1

    def choose_magic(self):
        i = 1
        print(bcolors.LightRed + bcolors.Bold + "Magic" + bcolors.End)
        for spell in self.magic:
            print("     "+ str(i)+":", spell.name, "(cost:"+ str(spell.cost) + ")")
            i += 1

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def choose_item(self):
        i = 1
        print(bcolors.LightRed + bcolors.Bold + "ITEMS" + bcolors.End)
        for item in self.item:
            print("    "+str(i)+"-"+item["item"].name, ":", item["item"].description,"(x", str(item["quantity"]),")")
            i = i+1





