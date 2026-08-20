import csv


def enter_video_games_info ():
    game = {}
    game["name"] = input ("Enter the name of the game: ")
    game["gender"] = input ("Enter the the gender of the game: ")
    game["developer"] = input ("Enter the Developer: ")
    game["classification"] = input("Enter the ESRB Classification: ")
    return game


def create_list():
    games_list = []
    while True:
        
        try:
            while True:
                option = int(input("Would you like to add a video game info, choose 1) or choose 2)?"))
                if option == 1 or option == 2:
                    break
        except ValueError as e:
            print("only numbers 1 and 2 are accepted.")
            continue   
            
        if option == 1:
            game_dict = enter_video_games_info()
            games_list.append(game_dict)
        elif option == 2:
            create_csv_file(games_list)
            print("Finish, the cvs is done.") 
            break 


def create_csv_file (video_games_list):  
    with open("Tabulado_games_csv.csv", 'w', encoding='utf-8', newline='') as file:
        headers = video_games_list[0].keys()
        writer = csv.DictWriter(file, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames = headers)
        writer.writeheader()
        writer.writerows(video_games_list)  

def main(): 
    create_list()
    

if __name__ == "__main__":
    main()