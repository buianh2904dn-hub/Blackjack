import random
import time

time.sleep(1)
print("\n-------------------- WELCOME TO ANH'S BLACKJACK VERSION --------------------")

#create total function to calculate the sum of card
#mimic the card in the list that being used
#create a function that random choose a card in a list


#create a list deck of card
value = {}
card_name = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES'] #also name as key
card_value = ['Two of ', 'Three of ', 'Four of ', 'Five of ', 'Six of ', 'Seven of ', 'Eight of ', 'Nine of ', 'Ten of ']

for index, item_2 in enumerate(card_value, start = 2):
	for item_1 in card_name:
		card = item_2 + item_1
		value[card] = index

spe_card = ['JACK', 'QUEEN', 'KING', 'ACE']
for card_rank in spe_card:
	for name in card_name:
		card = card_rank + ' of ' + name
		if card_rank == 'ACE':
			value[card] = 11
		else:
			value[card] = 10


#calculate total of each hand
#'turn' used to distinguish who is being dealt a card.
def total(turn):
	total = 0
	ace = 0
	for card in turn:
		val = value[card]
		total += val
		if 'ACE' in card:
			ace += 1
	while total > 21 and ace:
		total -= 10
		ace -= 1
	return total

#create an input to start over a game if player choose play again
again = 'yes'
while again =='yes' or again == 'y':


	#create a loop to start over if player busted (using in 1 player only)
	while True:
		#deal the card by define which turn for the dealer and player
		deck = list(value.keys())
		player1_hand = []
		player2_hand = []
		dealer_hand = []
		def DealCard(turn):
			card_chose = random.choice(deck)
			turn.append(card_chose)
			deck.remove(card_chose)
			return card_chose


		#test with DealCard function
		DealCard(player1_hand)
		DealCard(player1_hand)
		DealCard(player2_hand)
		DealCard(player2_hand)
		DealCard(dealer_hand)
		DealCard(dealer_hand)

		'''#use to testing the card be drawn only
		print("\nPlayer 1's hand: ", player1_hand)
		print("Player 2's hand: ", player2_hand)
		print("Dealer's hand: ", dealer_hand)'''


		#print out final result
		time.sleep(1)
		print("\n--------------- Current Hand ---------------")
		print("\nPlayer 1's hand:")
		for card in player1_hand:
			print(f"- {card}")
		print(f"Total value: {total(player1_hand)}")

		print("\nPlayer 2's hand:")
		for card in player2_hand:
			print(f"-{card}")
		print(f"Total value: {total(player2_hand)}")

		print("\nDealer's hand:")
		print(f"- {dealer_hand[0]}")
		print("- ??? (face down)")
		print(f"Visible value: {value[dealer_hand[0]]}")



		#ask if player want to stand or hit
		time.sleep(3)
		print("\n--------------- Question ---------------")
		
		#create player2 function automatic decide how to play (to use after player1)
		def player2():
			print(f"\nTotal player 2 value is: {total(player2_hand)}")
			total_dealer = total(dealer_hand)
			
			while total(player2_hand) < 21:
				#set condition to stand for player2
				if total(player2_hand) >= total_dealer and total(player2_hand) >= 17:
					print("Player 2 chose 'Stand'")
					print(f"Total value: {total(player2_hand)}")
					break  #player2 is satisfied

				#set condition to hit for player2
				new_card = DealCard(player2_hand)
				print(f"Player 2 chose 'Hit': {new_card}")
				print(f"Player 2 total value is: {total(player2_hand)}")

			#check player2 with dealer
			if total(player2_hand) > 21:
				print("Player 2 is BUSTED!")
			else:
				print("Player 2 'Stand'")


		#add player2() after setup option for player1
		def question():
			#human player choose to stand or hit
			print(f"\nYour total value is: {total(player1_hand)}")
			while total(player1_hand) <= 21:
				ask = input("You want to Stand(S) or Hit(H): ")
				if ask.lower().startswith('h'):
					new_card = DealCard(player1_hand)
					print(f"Your new card is: {new_card}")
					print(f"Total value: {total(player1_hand)}")
					if total(player1_hand) > 21:
						print("YOU BUSTED!")
						break
				else:
					print(f"Keep your current value is: {total(player1_hand)}")
					break
			player2()
			return True
		question()
		
		
		'''player_turn = question()
		#Player busted, the game starting over at while loop (1 player)
		if not player_turn:
			print("\nStarting over...\n")
			time.sleep(2)
			continue'''



		#dealer show their card, keep the process until it greater than P1 or P2
		time.sleep(3)
		print("\n--------------- Reveal ---------------")
		print(f"\nDealer's total value is: {total(dealer_hand)}")
			
		def process():
			while total(dealer_hand) <= 21 and total(dealer_hand) <= max(total(player1_hand), total(player2_hand)): 
				new_card = DealCard(dealer_hand)
				if total(player1_hand) > 21 and total(player2_hand) > 21:
					break
				print(f"Dealer new card is: {new_card}")
				print(f"Dealer total value is: {total(dealer_hand)}")
				break


		#Define who win the game

			#Determine total values
			p1_total = total(player1_hand)
			p2_total = total(player2_hand)
			deal_total = total(dealer_hand)
			
			#Check for busts
			p1_bust = p1_total > 21
			p2_bust = p2_total > 21
			deal_bust = deal_total > 21
			
			if deal_bust:
				if not p1_bust and not p2_bust:
					print("Dealer busted. P1 and P2 win")
				elif not p1_bust and p2_bust:
					print("Dealer and P2 busted. P1 win")
				elif p1_bust and not p2_bust:
					print("Dealer and P1 busted. P2 win")
				else:
					print("All players busted. Dealer win")

			else: #dealer didn't bust
				if p1_bust and p2_bust:
					print("Player 1 and Player 2 busted. Dealer wins!")
				elif not p1_bust and p2_bust:
					if p1_total > deal_total:
						print("Player 1 wins!")
					elif p1_total < deal_total:
						print("Dealer wins!")
					else:
						print("Player 1 and Dealer tie!")
				elif p1_bust and not p2_bust:
					if p2_total > deal_total:
						print("Player 2 wins!")
					elif p2_total < deal_total:
						print("Dealer wins!")
					else:
						print("Player 2 and Dealer tie!")
				else:
					#No one busted
					p1_wins = p1_total > deal_total
					p2_wins = p2_total > deal_total

					if p1_total == deal_total and p2_total == deal_total:
						print("All tie with Dealer!")
					elif p1_total == deal_total and p2_total > deal_total:
						print("Player 2 wins! Player 1 ties with Dealer.")
					elif p2_total == deal_total and p1_total > deal_total:
						print("Player 1 wins! Player 2 ties with Dealer.")
					elif p1_wins and p2_wins:
						print("Player 1 and Player 2 win!")
					elif p1_wins:
						print("Player 1 wins!")
					elif p2_wins:
						print("Player 2 wins!")
					else:
						print("Dealer wins!")
		process()
		break
		
	print("\n---------- AGAIN? ----------")
	again = input("\nDo you want to play again?(Y/N): ").lower()

time.sleep(1)
print("\n---------- GAME IS CLOSING... ----------")
print("Thanks for playing!")
print("Game End.")





