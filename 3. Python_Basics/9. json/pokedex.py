import json

def convert_pokedex():
    with open("pokedex.json", 'r') as file:
        read_pokedex = json.load(file)
        return read_pokedex
    
def enter_data(pokedex_converted):    
    pokemon = {}
    pokemon["name"] = input("Enter name: ")
    pokemon["type"] = input("Enter type: ")
    pokemon["level"] = int(input("Enter level: "))
    pokemon["weight_kg"] = int(input("Enter weight kg: "))
    pokemon["is_shiny"] = input("Is shiny: ")

    list_skills = []
    stats = {}

    while True:
        option = input("1)add skill ---- 2)enter stats: 3)finish")
        if option == "1":
            skill = input("Enter skill. ")
            list_skills.append(skill)
            pokemon["skills"]=list_skills
            print(pokemon)
            
        if option == "2":
                    
                    stats["attack"] = int(input("Ataque: ")) 
                    stats["defense"] = int(input("Defense: "))
                    stats["hp"] = int(input("hp: "))
                    stats["sp_attack"] = int(input("sp atack: "))
                    stats["sp_defense"] = int(input("sp_defense: "))
                    stats["speed"] = int(input("speed: "))   
            
        if option == "3":
            pokemon["stats"] = stats
            pokedex_converted.append(pokemon)
            return pokedex_converted
        
        
        
            

def save_data (pokemon_file):
    with open('pokedex.json', 'w') as file:
        json.dump(pokemon_file, file, indent=4, sort_keys=True)
        
def main():    
    pokemon_final_list = enter_data(convert_pokedex())  
    save_data(pokemon_final_list)    
    
if __name__ == "__main__":
    main()   
    