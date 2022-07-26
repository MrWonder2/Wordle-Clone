import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from string import whitespace
from pygame.locals import *
pygame.init()

yellow = (201, 180, 88)
white = (255, 255, 255)
grey = (58, 58, 60)
black = (18, 18, 19)
brightgreen = (0, 255, 0)
green = (83, 141, 78)
red = (255, 0, 0)
cyan = (0, 255, 255)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!", True, brightgreen)
youLose = bigFont.render("You Lose!", True, red)
playAgain = bigFont.render("Play Again?", True, white)
yn = bigFont.render("y/n", True, white)


def checkGuess(turns, word, userGuess, window):
    renderList = ["", "", "", "", ""]
    spacing = 0
    guessColourCode = [grey, grey, grey, grey, grey]
    remaining_letters_in_word = word

    for x in range(0, 5):
        if word[x] == userGuess[x]:
            remaining_letters_in_word = remaining_letters_in_word.replace(
                userGuess[x], "")
            guessColourCode[x] = green

    for x in range(0, 5):
        if (userGuess[x] in remaining_letters_in_word) and (userGuess[x] != word[x]):
            remaining_letters_in_word = remaining_letters_in_word.replace(
                userGuess[x], "")
            guessColourCode[x] = yellow

    list(userGuess)

    for x in range(0, 5):
        renderList[x] = font.render(userGuess[x], True, white)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(
            400 + spacing, 70 + (turns*70), 50, 50))
        if userGuess[x] == "I":
            window.blit(renderList[x], (420 + spacing, 85 + (turns*70)))
        else:
            window.blit(renderList[x], (415 + spacing, 85 + (turns*70)))
        spacing += 70

    if guessColourCode == [green, green, green, green, green]:
        return True


def main():
    file = open("solutions.txt", "r")
    answerList = file.readlines()
    word = answerList[random.randint(0, len(answerList)-1)].upper()

    wordlist = open("words.txt", "r")
    wordlist = wordlist.readlines()
    wordlist = [x.strip() for x in wordlist]

    height = 700
    width = 1150

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    print(word)

    for x in range(0, 5):
        for y in range(0, 5):
            pygame.draw.rect(window, grey, pygame.Rect(
                400+(x*70), 70+(y*70), 50, 50), 2)

    pygame.display.set_caption("Wordle!")
    icon = pygame.image.load('wordle.jpg')
    pygame.display.set_icon(icon)

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE) or (len(guess) > 5):
                guess = guess[:-1]
                guess = guess.upper().strip()

            if (event.type == pygame.KEYDOWN and event.key != pygame.K_BACKSPACE):
                if event.unicode.upper().strip().isalpha() and turns<5:
                    guess += event.unicode.upper().strip()
                if event.unicode.upper() == "Y" and (win == True or turns >= 5):
                    main()
                elif event.unicode.upper() == "N" and (win == True or turns >= 5):
                    pygame.quit()
                    sys.exit()
                if guess.lower() in wordlist:
                    if event.key == K_RETURN and len(guess) > 4:
                        win = checkGuess(turns, word, guess, window)
                        turns += 1
                        guess = ""
                        window.fill(black, (250, 550, 500, 200))

        window.fill(black, (250, 550, 500, 200))
        renderGuess = font.render(guess, True, white)
        window.blit(renderGuess, (520, 600))

        if win == True:
            window.blit(youWin, (440, 450))
            window.blit(playAgain, (400, 500))
            window.blit(yn, (520, 550))

        if turns == 5 and win != True:
            window.blit(youLose, (420, 450))
            window.blit(playAgain, (400, 500))
            window.blit(yn, (520, 550))
            CorrectWord = bigFont.render(
                str("Answer was ") + str(word[0:5]), True, yellow)
            window.blit(CorrectWord, (300, 610))

        pygame.display.update()
        clock.tick(FPS)


main()
