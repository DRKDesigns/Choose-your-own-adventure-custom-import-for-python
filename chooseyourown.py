num = 1
import time
gamepoints = 0

def gameover(number, reason, restart, remove):
    global num
    global gamepoints
    if num == number:
        print('Game Over! '+str(remove)+' points have been lost')
        print(reason)
        input('Try again? (Press enter/return)')
        num = restart
        gamepoints -= int(remove)



def story(number, text, optiona, optionb, anext, bnext):
    global num
    if num == number:
        response = input(text + ' Option A: ' + optiona + ' Option B: ' + optionb + ' ')
        if response == 'B' or response == 'b':
            num = bnext
        else:
            num = anext

def text(number,text,wait,next):
  global num
  if num == number:
    print(text)
    time.sleep(wait)
    num = next

def points(number,amount):
  if num == number:
    global gamepoints
    gamepoints += amount

def end(number,text):
  global num
  global gamescore
  if num == number:
    print('You completed the game! Your final score was '+ str(gamepoints))
    print(text)
    input('Play again? The game addapts to your choices so it is different every time. (Press enter/return)')
    num = 1
    gamescore = 0
