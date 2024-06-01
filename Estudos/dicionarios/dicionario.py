from random import randint

lista_npcs = []

def create_monster():
    level = randint(0, 50)
    new_npc = {
        "name": f"Monster #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level
    }

    lista_npcs.append()

create_monster()

print(lista_npcs)