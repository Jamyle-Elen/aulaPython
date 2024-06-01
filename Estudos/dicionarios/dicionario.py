from random import randint

lista_npcs = []

def create_npc():
    level = randint(0, 50)
    new_npc = {
        "name": f"Monster #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level
    }

    lista_npcs.append(new_npc)

def display_npc():
    for npc in lista_npcs:
        print(f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']} // HP: {npc['hp']}")

def generate_npcs(n_npcs):
    for x in range(n_npcs):
        print(x)
        create_npc()



generate_npcs(5)
