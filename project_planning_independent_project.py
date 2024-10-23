#A problem I found when starting soccer was that i had to use different apps in order to learn different things about soccer so I made this code fix that very problem. You can learn about the rules about soccer the top players and their individual statistics. That is the purpose of this code, to let the user learn about soccer using one app instead of multiple.
while True:
    # This app is an informational source about soccer. it includes information about the game itself and the current top five players and their statistics.
    #These are the three main rules of soccer
    rules = (f"Some rules are {'\'No touching the ball with your hands\''}, \n{'\'No being behind the opponents defense wothout the ball\''}\nand {'\'No going out of bounds.\''}")
    #These are the current top five players in soccer
    topPlayers = ("Mohamad Salah, Jude Bellingham, Kylian Mbappe, Erling Haaland and Harry Kane ")
    #These are Mohamad Solah's Statistics
    Mohamad_Solah = (f"He is {'5ft 9in'} tall,He weighs {'165lbs'},His Shooting Accuracy is {'44%'}, his Passing Accuracy is {'72.5%'} and his position is {'Forward'}")
    #These are Kylian Mbappe's Statistics
    Kylian_Mbappe = (f"He is {'5ft 10in'} tall, He weighs {'165lbs'}, His shooting accuracy is {'65.52%'}, his Passing Accuracy is {'83.3%'} and the position he plays is {'Forward'}")
    #These are Jude Bellingham's Statistics
    Jude_Bellingham = (f"He is {'6ft 1in'} tall, He weighs {'165lbs'}, His shooting accuracy is {'33.33%'}, his Passing Accuracy is {'88.5%'} and the position he plays is {'Midfielder'}")
    #These are Erling Haaland's Statistics
    Erling_Haaland = (f"He is {'6ft 4in'} tall, He weighs {'194lbs'}, His Shooting Accuracy is {'76.67%'}, his Passing Accuracy is {'68.5%'} and the position he plays is {'Forward'}")
    #These are Harry Kane's Statistics
    Harry_Kane = (f"He is {'6ft 2in'} tall, He weighs {'188lbs'}, His Shooting Accuracy is {'58.33%'}, his Passing Accuracy is {'82.5%'} and the position he plays is {'Froward'}")
    #This is a greeting and a question about what the user needs to know
    Question = input('Greetings user, what would you like to learn about?')
    #This is the function that updates the screen and shows the user what he or she chooses to learn about
    def updateScreen(rules,topPlayers,Mohamad_Solah,Kylian_Mbappe,Jude_Bellingham,Erling_Haaland,Harry_Kane):
        #These are the conditions the code checks to see if it can tell the user what he or she wants to learn about
        if Question == ('I would like to learn about Mohamad Solah'):
            print(Mohamad_Solah)
        if Question == ('I would like to learn about the rules of soccer'):
            print(rules)
        if Question == ('I would like to learn about Kylian Mbappe'):
            print(Kylian_Mbappe)
        if Question == ('I would like to learn about Jude Bellingham'):
            print(Jude_Bellingham)
        if Question == ('I would like to learn about Erling Halland'):
            print(Erling_Haaland)
        if Question == ('I would like to learn about Harry Kane'):
            print(Harry_Kane)
        if Question == ('I would like to learn about the top players of soccer'):
            print(f"The top players in soccer are {topPlayers}")
    updateScreen(rules,topPlayers,Mohamad_Solah,Kylian_Mbappe,Jude_Bellingham,Erling_Haaland,Harry_Kane)
    #This tells the code to end the loop and say goodbye to the user
    if Question == 'q':
            print("Goodbye user, hope to see you soon!")
            break
updateScreen(rules,topPlayers,Mohamad_Solah,Kylian_Mbappe,Jude_Bellingham,Erling_Haaland,Harry_Kane)
