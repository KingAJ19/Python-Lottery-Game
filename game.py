import random
import time

ticket_lottery = random.sample(range(1, 20), k=7)

print("Hello!  Welcome to my lottery game.")
age = int(input("Before we start, tell me how old you are: "))
if age >= 18:
  print("It seems you are old enough to play.")
else:
  print("Looks like you're not old enough to play. Sorry!")
  time.sleep(15000)
username = input("Okay, now enter your name:")
print("Your name is: " + username)

print("Provide 7 numbers from 1 to 20 (one by one- separated by spacebars):")
ticket_input = list(map(int, input().split()))

tl = sorted(ticket_lottery)
ti = sorted(ticket_input)

points = 0
for number in ti:
   if number in tl:
       points +=1

print("Lottery numbers are: {}".format(tl))
print("       You selected: {} and got {} points".format(ti, points))

if (points < 3):
   print("       Thank you for trying!".format(points))
if (points == 3):
   print("       Your prize is R20. Congrats!")
if (points == 4):
   print("       Your prize is R400. Congrats!")
if (points == 5):
   print("       Your prize is R100. Congrats!")
if (points == 6):
   print("       Your prize is R10000. Congrats!")
if (points == 7):
   print("       Your prize is R1000000. Congrats!")