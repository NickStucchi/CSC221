#!/usr/bin/env python3
# Nick Stucchi
# 02/23/2017
# Play Rock Paper Scissors with the computer

import random

def randomDraw():
   draws = ["rock", "paper", "scissors"]
   return draws[random.randrange(0,3)]

def main():
   computer = randomDraw()
   player_wins = 0
   computer_wins = 0
   ties = 0
   player = False
   while player == False:
      player = input("Rock, Paper, or Scissors ('exit' to leave)? ")
      if player == computer:
         ties += 1
         print("Computer chose " + computer + ". Tie!")
      elif player == "rock":
         if computer == "paper":
            computer_wins += 1
            print("Computer chose paper. You lose!")
         else:
            player_wins += 1
            print("Computer chose scissors. You win!")
      elif player == "paper":
         if computer == "scissors":
            computer_wins += 1
            print("Computer chose scissors. You lose!")
         else:
            player_wins += 1
            print("Computer chose rock. You win!")
      elif player == "scissors":
         if computer == "rock":
            computer_wins += 1
            print("Computer chose rock. You lose!")
         else:
            player_wins += 1
            print("Computer chose paper. You win!")
      else:
         continue
      player = False
      computer = randomDraw()
   if player_wins == computer_wins:
      print("DRAW! You and the computer tied " + str(player_wins) + " - " + str(computer_wins) + ". Game ended.")
   if player_wins > computer_wins:
      print("WIN! You beat the computer " + str(player_wins) + " - " + str(computer_wins) + " There were " + str(ties) + " ties. Game ended.")
   if player_wins < computer_wins:
      print("LOSE! The computer beat you " + str(computer_wins) + " - " + str(player_wins) + " There were " + str(ties) + " ties. Game ended.")
         
if __name__ == '__main__':
   main()
         

