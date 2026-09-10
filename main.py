from player_class import player
import json

menu = {}
players = json.loads('{"players": []}')

menu['1'] = "Add Player."
menu['2'] = "Delete Player."
menu['3'] = "Customize Player."
menu['4'] = "Find Player."
menu['5'] = "Show LeaderBoard"
menu['6'] = "Exit"

def add_player():
    while True:
        # 1. Fixed indentation (4 spaces)
        # 2. Changed 'selection' to 'input'
        player_id = input("Enter Player ID: ")
        
        if player_id in players:
            print(f"A player with ID {player_id} already exists.")
        else:
            username = input("Enter Player Username: ")
            score = input("Enter Player Score: ")

            new_player = player(player_id, username, score)
            players[player_id] = new_player
            print(f"Player {new_player.username} added with ID {new_player.id} and score {new_player.score}.")
            
        again = input("Do you want to add another player? (y/n): ").strip().lower()
        if again != 'y':
            break

def delete_player():
    id = input("Enter Player ID to delete: ")
    if players.pop(id, None) is None:
        print(f"No player with ID {id} found.")
    else:
        print(f"Player with ID {id} deleted.")

def customize_player():
    id = input("Enter Player ID to customize: ")
    selected_player = players.get(id)
    if selected_player is None:
        print(f"No player with ID {id} found.")
        return

    selected_player.username = input("Enter new Player Username: ")
    selected_player.score = input("Enter new Player Score: ")
    print(f"Player with ID {id} customized.")

def find_player():
    id = input("Enter Player ID to find: ")
    selected_player = players.get(id)
    if selected_player is None:
        print(f"No player with ID {id} found.")
    else:
        print(f"Player {selected_player.username} has ID {selected_player.id} and score {selected_player.score}.")

def show_leaderboard():
    players = json.load(open('players.json', 'r'))['players']
    players.sort(key=lambda p: p['score'], reverse=True)

    print("LeaderBoard:")
    for i, player in enumerate(players, start=1):
        print(f"{i}. {player['username']} - {player['score']}")

while True:
    options = sorted(menu.keys())

    for entry in options:
        print(entry, menu [entry])
    selection = input("Please Select: ")
    if selection == '1':
        add_player()
    elif selection == '2':
        delete_player()
    elif selection == '3':
        customize_player()
    elif selection == '4':
        find_player()
    elif selection == '5':
        show_leaderboard()
    elif selection == '6':
        break
    else:
        print("Unknown Option Selected!")