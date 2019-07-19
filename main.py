from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import item
# create black magic
ThunderPunch = Spell("ThunderPunch", 20, 100, "black")
Blaze_kick = Spell("Blazekick", 25, 125, "black")
Ice_Beam= Spell("ice_Beam", 30, 140, "black")
Petrol_bomb = Spell("petrol_bomb", 35, 165, "black")
Poison_spray = Spell("poison_spray", 36, 170, "black")

# Create White Magic
Heal = Spell("heal", 25, 100, "White")
Health_bag = Spell("health_bag", 30, 150, "White")

# item list
portion = item("Portion", "portion", "heal 100 hp", 100)
high_portion = item("High_Portion", "portion", "heal 125 hp", 125)
elixer = item("Elixer", "elixer", "heal 30 mp", 30)

grenade = item("grenade", "attack", "deals 200 hp", 200)

# Enter player's Name
name = input("Enter Player's name : ")
# invoke person
player_spell = [ThunderPunch, Blaze_kick, Ice_Beam,
                Petrol_bomb, Poison_spray, Heal, Health_bag]
player_items = [{"item": portion, "quantity": 2}, {"item": high_portion,"quantity": 2},
                {"item": elixer, "quantity": 2}, {"item": grenade,"quantity": 2}]
player = Person(name, 500, 100, 65, 40, player_spell, player_items)
enemy = Person("Horror_beast", 900, 65, 75, 45, [], [])

running = True
i = 0

print(bcolors.LightMagenta + bcolors.Bold + "              Horror_beast Attack!            " + bcolors.End)

while running:
    print("============================================")
    player.choose_action()

    choice = input("Choose Action : ")
    index = int(choice)-1
    sample = [0, 1, 2]
    if not(index in sample):
        print("\n       please press Valid key")
        continue
    if index == 0:
        dmg = player.generate_dmg()
        enemy.take_damage(dmg)
        print(player.get_name()+"'s Attacked For", dmg, "points of damage")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic :"))-1
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.LightBlue+"\nWhoops!! No MAGIC POINTS"+bcolors.End)
            continue

        player.reduce_mp(spell.cost)
        if spell.type == "White":
            player.heal(magic_dmg)
            print(bcolors.LightMagenta + "\n" + spell.name + " heals for " + str(
                  magic_dmg) + " point" + bcolors.End)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.LightMagenta+ "\n"+spell.name+" deals "+ str(magic_dmg)+ " point of Damage"+bcolors.End)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose items :"))-1

        if item_choice == -1:
            continue
        item = player.item[item_choice]["item"]

        if player.item[item_choice]["quantity"] == 0:
            print(bcolors.LightRed + "         None left "+bcolors.End)
            continue

        player.item[item_choice]["quantity"] -= 1
        if item.type == "portion":
            player.heal(item.prop)
            print(bcolors.LightMagenta + "\n" + item.name + " heals for " + str(
                item.prop) + " point" + bcolors.End)
        elif item.type == "elixer":
            player.mp += item.prop
            player.hp += item.prop
            if player.mp > player.max_mp:
                player.mp = player.max_mp
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(bcolors.LightMagenta + "\n" + item.name + " restore HP/MP  " + str(
                item.prop) + " point" + bcolors.End)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.LightMagenta + "\n" + item.name + " deals " + str(
                item.prop) + " point of damage" + bcolors.End)




    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player.take_damage(enemy_dmg)
    print(enemy.get_name()+"'s attacks you and reduced", enemy_dmg," points")

    print("---------------------------------------------")
    print(enemy.get_name()+"'s HP " + bcolors.LightRed + str(enemy.get_hp())+"/" + str(enemy.get_max_hp())+bcolors.End)
    print(player.get_name()+"'s HP " + bcolors.LightGreen + str(player.get_hp())+"/"+str(player.get_max_hp())+bcolors.End)
    print(player.get_name()+"'s MP " + bcolors.LightBlue + str(player.get_mp())+"/"+str(player.get_max_mp())+bcolors.End)

    if enemy.get_hp() == 0:
        print(bcolors.LightGreen + "\n     YOU killed Horror_beast!!     \n"+ bcolors.End)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.LightRed + "\n"+enemy.get_name()+" has defeated you" + bcolors.End)
        running = False

