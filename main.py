import random
import os

def mastermind():
    listofcolor=['R', 'G', 'B', 'Y', 'P', 'W']
    machine_combination=['','','','']
    try_limit=12
    for i in range(4):
        machine_combination[i]=random.choice(listofcolor)
        game_iterator = 0
        replay = True
        reset_count = False

        if (os.path.isfile('stats/score.txt') != 1 and os.path.isfile('stats/games played.txt') != 1):
            with open('stats/score.txt', 'w') as fichier:
                fichier.write("Score :\n")
                fichier.write("0")

            with open('stats/games played.txt', 'w') as fichier:
                fichier.write("Number of games played : \n")
                fichier.write("0")

        with open('stats/score.txt', 'r') as fichier:
            lignes = fichier.readlines()
            score = lignes[1]

        with open('stats/games played.txt', 'r') as fichier:
            lignes = fichier.readlines()
            games_played = lignes[1]

        while (replay):
            print("The usable color are:" +"R, "+"G, "+"B, "+"Y, "+"P, "+"W")

            print("Your score is " + score)
            print("You have attempted " + games_played + " on 12")

            choice = input("What do you want to do : play/replay or leave or reset")

            if (choice == "play" or choice == "replay"):
                reset_count = False

                human_combination= input("write a combination")
                human_combination=list[human_combination]

                while (human_combination in listofcolor):
                    for i in range(4):
                        if (human_combination[i]==machine_combination[i]):
                            human_combination=human_combination.append(human_combination[i])
                if (game_iterator != 12):
                    print("You win")
                    score = int(score)
                    score += 1
                    score = str(score)
                else:
                    print("You lose")

                games_played = int(games_played)
                games_played += 1
                games_played = str(games_played)

                game_iterator = 0

                replay_choice = input("Do you want to play again ?")


                if (replay_choice == "no" or replay_choice == "NO" or replay_choice == "No"):
                    replay = False

            elif (choice == "leave"):
                print("You leave the game")
                replay = False

            elif (choice == "reset"):
                with open('statistiques/score.txt', 'w') as fichier:
                    fichier.write("Score :\n")
                    fichier.write("0")
                    score = int(score)
                    score = 0
                    score = str(score)

                with open('statistiques/games played.txt', 'w') as fichier:
                    fichier.write("Number of games played : \n")
                    fichier.write("0")
                    games_played = int(score)
                    games_played = 0
                    games_played = str(score)

                reset_count = True

            print("Game finish")


        print(machine_combination)

mastermind()






