import random, time, os #importerar funktionerna för random, time och os så att vi kan använda dem senare.
ai = 0 #sätter värde på variabeln så att programmet inte kraschar vid debug.
player2 = 0 
score2 = 0 
score = 0 
scoreai = 0 
print("Welcome to GITCommitDie") #skriver ut ett välkomstmeddelande.

meny = 0 

while meny !=489: #vilket nummer det är spelar ingen roll igentligen, den är bara där för att fortsätta loopen tills någon har vunnit. 
    try: #programmet fortsätter försöka få nedanstående input från användaren...
        meny = int(input("Tryck 1 för AI eller 2 för 2 spelare: ")) 
    except: 
        print("Försök igen, 1 för AI eller 2 för 2 spelare: ")
    if meny == 1: #om tidigare input är 1 så körs AI versionen av spelet...
        for x in range(1, 11):
            os.system('cls') 
            ai = random.randint(1,3) #använder random funktionen för att slumpa ett tal mellan 1 och 3 som motsvarar de 3 alternativen.
            print("==============================================") #avskärning för att det ska vara stilrent.
            print("Option 1: Sten")
            print("Option 2: Sax")
            print("Option 3: Påse")
            print("==============================================")
            time.sleep(0.5) #använder time funktionen för att lägga till en kort fördröjning (stilrent).
            print("Player:", score)
            print("AI", scoreai)
            player = int(input("Choose an option: "))
            if player == ai: #om Player och AI valde samma alternativ...
                print("Tie") #skriver den ut "Tie" utan att lägga till fler poäng till någon sida.
            elif player == 2 and ai == 1:
                scoreai += 1 #när AI vinner får den +1 till det nuvarande värdet i sin poäng-variabel.
                print("AI wins", scoreai)
            elif player == 3 and ai == 2:
                scoreai += 1
                print("AI wins", scoreai)
            elif player == 1 and ai == 3:
                scoreai += 1
                print("AI wins", scoreai)
            else: 
                score += 1
                print("Player wins", score)
            if score > 2: #om poängen överskrider 2, (alltså 3) så vinner Player.
                print("Player wins")
                print("""
  _____  _                                  _           
 |  __ \| |                                (_)          
 | |__) | | __ _ _   _  ___ _ __  __      ___ _ __  ___ 
 |  ___/| |/ _` | | | |/ _ \ '__| \ \ /\ / / | '_ \/ __|
 | |    | | (_| | |_| |  __/ |     \ V  V /| | | | \__ /
 |_|    |_|\__,_|\__, |\___|_|      \_/\_/ |_|_| |_|___/
                  __/ |                                 
                 |___/                                  
                """)
                break
            if scoreai > 2: 
                print("AI wins")
                print("""
           _____  __          ___           
     /\   |_   _| \ \        / (_)          
    /  \    | |    \ \  /\  / / _ _ __  ___ 
   / /\ \   | |     \ \/  \/ / | | '_ \/ __|
  / ____ \ _| |_     \  /\  /  | | | | \__ /
 /_/    \_\_____|     \/  \/   |_|_| |_|___/
                                            
                                            
                """)
                break
    if meny == 2:
        for x in range(1, 11):
            os.system('cls')
            print("==============================================")
            print("Option 1: Sten")
            print("Option 2: Sax")
            print("Option 3: Påse")
            print("==============================================")
            time.sleep(0.5)
            print("Player1: ", score)
            print("Player2: ", score2)
            player = int(input("Choose an option: "))
            os.system('cls')
            print("==============================================")
            print("Option 1: Sten")
            print("Option 2: Sax")
            print("Option 3: Påse")
            print("==============================================")
            print("Player1: ", score)
            print("Player2: ", score2)
            player2 = int(input("Choose an option: "))
            print("==============================================")

            if player == player2:
                print("Tie",)
            elif player == 2 and player2 == 1: 
                score2 += 1
                print("Player 2 wins", score2)
            elif player == 3 and player2 == 2:
                score2 += 1
                print("Player 2 wins", score2)
            elif player == 1 and player2 == 3:
                score2 += 1
                print("Player 2 wins", score2)
            else:
                score += 1 
                print("Player1 wins", score)
            if score > 2:
                print("Player1 wins")
                print("""
                ______  _                        __          ___           
                |  __ \| |                       \ \        / (_)          
                | |__) | | __ _ _   _  ___ _ __   \ \  /\  / / _ _ __  ___ 
                |  ___/| |/ _` | | | |/ _ \ '__|   \ \/  \/ / | | '_ \/ __|
                | |    | | (_| | |_| |  __/ |       \  /\  /  | | | | \__ /
                |_|    |_|\__,_|\__, |\___|_|        \/  \/   |_|_| |_|___/
                                __/  |                                     
                                |___/                                      
                """)
                break
            if score2 > 2:
                print("Player2 wins")
                print("""
                    ______  _                         ___             _           
                    |  __ \| |                       |__ \           (_)          
                    | |__) | | __ _ _   _  ___ _ __     ) | __      ___ _ __  ___ 
                    |  ___/| |/ _` | | | |/ _ \ '__|   / /  \ \ /\ / / | '_ \/ __|
                    | |    | | (_| | |_| |  __/ |     / /_   \ V  V /| | | | \__ /
                    |_|    |_|\__,_|\__, |\___|_|    |____|   \_/\_/ |_|_| |_|___/
                                     __/ |                                        
                                    |___/                                         
                """)
                break
