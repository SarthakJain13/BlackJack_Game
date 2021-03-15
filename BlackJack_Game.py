import playing_cards

def display_details():

    print('File         : BlackJack.py')

    print('Author       : Sarthak Jain ')

    print('Email Id     : Sarthakjain130401@outlook.com ')

    print('LinkedIn     : www.linkedin.com/in/sarthak-jain-2659b81b6\n')

    print('General Note : ')

    print('Please feel free to reach out to me rearding any query related to the code or either way\n\n')

    

def get_hit_choice():

    choice = 'h'

    choice = str(input("\nPlease enter h or s (h = Hit, s = Stand): "))

    return choice

def get_play_choice():

    choice = str(input("\nPlay again [y|n]?: "))

    return choice

def diplay_hand(hand_text, hand):

    handValue = get_hand_total(hand)

    displayText = ""

    for card in hand:

        walker = 0

        for element in range(0, len(card)):

            if walker == 0:

                cardValue = (card[element])

                walker = 1

            else:

                suiteValue = ""

                suite = (card[element])

                if(suite == 'D'):

                    suiteValue = "of Diamonds"

                elif(suite == 'H'):

                    suiteValue = "of Hearts"

                elif(suite == 'S'):

                    suiteValue = "of Spades"

                elif(suite == 'C'):

                    suiteValue = "of Clubs"

                displayText += cardValue + " " + suiteValue + " | "

    displayText = displayText.rstrip(displayText[-3:])

    print(hand_text + " " + str(handValue) + ": " + displayText)

def get_hand_total(hand):

    handValue = 0

    aceCard = 0

    for card in hand:

        walker = 0

        for element in range(0, len(card)):

            faceValue = 0

            if walker == 0:

                value = (card[element])

                if(value == 'T' or value == 'J' or value == 'Q' or value == 'K'):

                    faceValue = 10

                elif(value.isdigit()):

                    faceValue = int(value)

                elif(value == 'A'):

                    aceCard += 1

                handValue += faceValue

                walker = 1



    if(aceCard == 0):

        return handValue

    else:

        if(handValue + 11 > 21):

            handValue = handValue + (1 * aceCard)

        else:

            handValue = handValue + 11 + (1 * aceCard) - 1

    return handValue

def play_player_hand(hand):

    playerTotal = get_hand_total(hand)

    hitChoice = get_hit_choice()

    if(hitChoice.lower() == 's' and playerTotal < 15):

        print ("--> Cannot stand")

        hitChoice = 'h'

    while hitChoice.lower() != 's' and hitChoice.lower() != 'b':

        if(hitChoice.lower() == 'h'):

            card = playing_cards.deal_one_card()

            player_hand.append(card)

            playerTotal = get_hand_total(player_hand)

            diplay_hand("Player's hand is", player_hand)

            if(playerTotal > 21):

                hitChoice = 'b'

        if(hitChoice.lower() == 'b'):

            print ("--> Player busts!")

        else:    

            hitChoice = get_hit_choice()

            if(hitChoice.lower() == 's' and playerTotal < 15):

                print ("--> Cannot stand")

                hitChoice = 'h'

def play_dealer_hand(hand):

    dealerTotal = get_hand_total(hand)

    while dealerTotal < 17:

        card = playing_cards.deal_one_card()

        dealer_hand.append(card)

        dealerTotal = get_hand_total(dealer_hand)

        diplay_hand("Dealer's hand is", dealer_hand)



        if(dealerTotal > 21):

            print ("--> Dealer busts!")

def isBlackJack(hand):

    handValue = get_hand_total(hand)

    if(handValue == 21):

        return True

    else:

        return False

display_details()

gamesPlayed = 0

playerWins = 0

dealerWins = 0

draws = 0

choice = 'y'

choice = str(input("Would you like to play BlackJack [y|n]? "))

while choice.lower() != 'y':

    choice =  str(input("Would you like to play BlackJack [y|n]? "))

while choice.lower() != 'n':

    if(choice.lower() == 'y'):

        print("\n---------------------- START GAME ----------------------")

        gamesPlayed += 1

        player_hand = []

        dealer_hand = []

        card = playing_cards.deal_one_card()

        player_hand.append(card)

        card = playing_cards.deal_one_card()

        dealer_hand.append(card)

        card = playing_cards.deal_one_card()

        player_hand.append(card)

        card = playing_cards.deal_one_card()

        dealer_hand.append(card)

        diplay_hand("Dealer's hand is", dealer_hand)

        diplay_hand("Player's hand is", player_hand)

        isDealerBackJack = isBlackJack(dealer_hand)

        isPlayerBackJack = isBlackJack(player_hand)

        if(isDealerBackJack == True and isPlayerBackJack == True):

            print ("\n*** Blackjack! Push - no winners! ***")

            draws += 1

        elif(isDealerBackJack == True):

            print ("\n*** Blackjack! Dealer Wins! ***")

            dealerWins += 1

        elif(isPlayerBackJack == True):            

            print ("\n*** Blackjack! Player Wins! ***")

            playerWins += 1

        else:

            play_player_hand(player_hand)

            play_dealer_hand(dealer_hand)

            playerTotal = get_hand_total(player_hand)

            dealerTotal = get_hand_total(dealer_hand)

            resultText = ""

            if(playerTotal > 21):

                resultText = " -> Dealer wins! ---"

                dealerWins += 1

            else:

                if(dealerTotal > 21):

                    resultText = " -> Player wins! ---"

                    playerWins += 1

                elif (playerTotal > dealerTotal):

                    resultText = " -> Player wins! ---"

                    playerWins += 1

                elif (playerTotal == dealerTotal):

                    resultText = " -> Push - no winners! ---"

                    draws += 1 

                else:

                    resultText = " -> Dealer wins! ---"

                    dealerWins += 1

            print("\n--- Dealer: " + str(dealerTotal) + " Player: " + str(playerTotal) + resultText)

        print("\n----------------------- END GAME -----------------------")

        print("That was fun!")

    choice = get_play_choice()

print("You played " + str(gamesPlayed) + " games!")

print("--> Won: " + str(playerWins))

print("--> Lost: " + str(dealerWins))

print("--> Drawn: " + str(draws))

print("\nThanks for playing! :)")