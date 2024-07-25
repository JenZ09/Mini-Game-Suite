
#final compilation

import time
import random
from words import word_list
#import nltk
#nltk.download('words')
from nltk.corpus import words
import pygame
from pygame.locals import *
from pygame import mixer
from tkinter import *
#from PIL import Image, ImageTk
from tkvideo import tkvideo

game=True

while game==True:
    for i in range(0,100):
        print()
    
    print("1)Hangman \n2)Scribble \n3)Rock Paper Scissors \n4)Exit")
    choice=int(input ("Enter the number for the game you want to play: "))

    #Shiny's code
    if choice==1:
        def get_word():
            word = random.choice(word_list)
            return word.upper()



        def play(word):
            word_completion=[]
            for i in range (0,len(word)):
                thing=" _ "
                word_completion.append(thing)
            guessed = False
            guessed_letters = []
            guessed_words = []
            tries = 7
            print(" Let's play Hangman !")
            print(stages[tries])
            print(word_completion)
            print("\n")
            while tries > 0 and guessed==False:
              #while guessed==False:
                guess = input("Guess a letter or a word: ").upper()
                if len(guess) == 1:
                    if guess in guessed_letters:
                        print("This letter has already been guessed", guess)
                    elif guess not in word:
                        print(guess, " is not in the word.")
                        tries -=1
                        print(stages[tries])
                        print(word_completion)
                        print("\n")
                        guessed_letters.append(guess)
                    else:
                        print("Correct! ", guess, " is in the word.")
                        guessed_letters.append(guess)
                        indices = [i for i, letter in enumerate(word)if letter == guess]
                        for index in indices:
                            word_completion[index] = guess
                
                        print(stages[tries])
                        print(word_completion)
                        if " _ " not in word_completion:
                            guessed = True 

                elif len(guess) == len(word):
                    if guess in guessed_words:
                        print("You've already guessed the word", guess)
                    elif guess != word:
                        print(guess, "is not the word!")
                        tries -=1
                        guessed_words.append(guess)
                    else:
                        guessed = True
                        word_completion = word
                else:
                    print("Not a valid guess!")
                    tries-=1
                    print(stages[tries])
                    print(word_completion)
                    print("\n")
       
    
            if guessed==True:
                print("Great job! you guessed the word.")
        
            elif guessed==False:
                print("Oops! you've run out of tries. The word was " + word )    
        

# final state: head, torso, both arms, and both legs
        stages={
                0:"""
                     --------
                    |      |
                    |      O
                    | -GAME-OVER-
                    |     \|/
                    |      |
                    |     / /
                    -
                               """,
                1:"""
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / /
                    -
                               """,
# head, torso, both arms, and one leg
                2:"""
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / 
                    -
                               """,
# head, torso, and both arms
                3:"""
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |      
                    -
                               """,
# head, torso, and one arm
                4:"""
                    --------
                    |      |
                    |      O
                    |      |/
                    |      |
                    |     
                    -
                               """,
# head and torso
                5:"""
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                               """,
# head
                6:"""
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                               """,
# initial empty state
                7:"""
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                              """}
       
 


        def main():
            word = get_word()
            play(word)
            while input("Play Again? (Y/N): ").upper() == "Y":
                print()
                word = get_word()
                play(word)
            else:
                print("Thank you!")
                time.sleep(3)


        if __name__ == "__main__":
            main()

        
    #nikkercow's code    
    elif choice==2:
        #s= letter bag
        s={"E":12,"A":9,"I":9,"O":8,"N":6,"R":6,"T":6,"L":4,"S":4,"U":4,          #1 point 
        "D":4,"G":3,                                                              #2 pts 
        "B":2,"C":2,"M":2,"P":2,                                                  #3 POINTS
        "F":2,"H":2,"V":2,"W":2, "Y":2,                                           #4 POINTS 
        "K":1,                                                                    #5 POINTS
        "J":1,"X":1,                                                              #8 PTS 
        "Q":1,"Z":1}                                                              #10 PTS
        score={"E":1,"A":1,"I":1,"O":1,"N":1,"R":1,"T":1,"L":1,"S":1,"U":1,"D":3,"G":3,"B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4, "Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}
        play_again="Y"
        fullscore=0

 
        pygame.init() 
        mixer.init()
        mixer.music.load("C:/jenitemp/where-the-light-is-15702.wav")
        mixer.music.play()


        def pick_set_of_letters(n):

            letters_to_choose_from = []
            for key in s:
                if s[key] != 0:
                    letters_to_choose_from += [key] * s[key] # makes a list so that the probability of picking a letter increases with its repetition
            randoms1=random.sample(letters_to_choose_from,7)
            print()
            print("Your set of letters are ["+randoms1[0]+" "+randoms1[1]+" "+randoms1[2]+" "+randoms1[3]+" "+randoms1[4]+" "+randoms1[5]+" "+randoms1[6]+"]")
 
            for i in randoms1:
                s[i]=s[i]-1
                if s[i]==0:
                    break
            return randoms1

        while play_again.upper()=="Y":
            player1letters = pick_set_of_letters(7)
    
            from nltk.corpus import words
            c=input("Enter a word OR  ;  to pass : ")

            if c!=";":
                checking= True
                total_score=0
                for ell in c.upper():
                    if ell in player1letters:
                        player1letters.remove(ell)
                        total_score=total_score+score[ell]
                    else:
                        checking= False
                if checking==True and c.lower() in words.words():
                    print (c.upper()+" is a valid word. You scored "+str(total_score)+" points")
                    fullscore=fullscore+total_score

                else:
                    print ("Sorry,"+c.upper()+" is not a valid word")
            print()
            play_again=input("Do you wish to play again? (Y/N) ")
        print()
        print ("Your total score is: "+ str(fullscore))
        print()
        print("Thank you for playing with me :)")
        print()
        print()
        pygame.quit()
        time.sleep(3)



    #jenny's code        
    elif choice==3:
        def stop_music():
            pygame.mixer.music.stop()

        def winner(play,comp):
  
          if (comp=="rock" and play=="paper"):
              result="Player"
          elif(comp=="rock" and play=="scissor"):
              result= "Computer"
          elif(comp=="paper" and play=="rock"):
              result= "Computer"
          elif(comp=="paper" and play=="scissor"):
              result= "Player"
          elif(comp=="scissor" and play=="rock"):
              result= "Player"
          elif(comp=="scissor" and play=="paper"):
              result= "Computer"
          elif (comp==play):
              result= "Draw"
          else:
              result= "Invalid Input"

          return result


        computer=0
        player=0

        def button_choice(choice):
  
            global computer,player
            global play_image,comp_image
            global rock_image,paper_image,scissor_image
            global lose, won, draw
    
    
            options=["rock","paper","scissor"]
            main_comp=options[random.randint(0,2)]
            if choice=="rock":
                main_play="rock"
                play_image = rock_image
        
            elif choice=="paper":
                main_play="paper"
                play_image = paper_image
        
            elif choice=="scissor":
                main_play="scissor"
                play_image =  scissor_image

            if main_comp=="rock":
                comp_image = rock_image
        
            elif main_comp=="paper":
                comp_image = paper_image
        
            elif main_comp=="scissor":
               comp_image = scissor_image

            comp_image = comp_image.zoom(100)
            comp_image = comp_image.subsample(50)
            play_image = play_image.zoom(100)
            play_image = play_image.subsample(50)
    
            comp_label=Label(root,text="COMPUTER",image=comp_image,compound=TOP,bg="turquoise",font=("Helvetica 10 bold")).grid(row=1,column=0)
            play_label=Label(root,text=" PLAYER ",image=play_image,compound=TOP,bg="turquoise",font=("Helvetica 10 bold")).grid(row=1,column=2)
    
            z=winner(main_play,main_comp)
            winner_label=Label(root,text="WINNER : "+z.upper(),width=20,height=8,bg="turquoise",fg="coral",font=("Helvetica 25 bold")).grid(row=1,column=1)
    
            if z=="Computer":
              computer+=1

            elif z=="Player":
              player+=1
              
            elif z=="Draw":
              computer+=1
              player+=1

            score_label=Label(root,text=("COMPUTER : "+str(computer)+ "  PLAYER : "+str(player)),width=30,height=5,bg="black",fg="gold",font=("Arial",12))
            score_label.grid(row=0,column=1)
    
            if computer==5 or player==5:
              pygame.mixer.music.stop()
              if computer>player:
                lose_window=Toplevel()
                lose_window.attributes("-fullscreen",True)

                pygame.mixer.music.load("C:/jenitemp/lose_sound.mp3")
                pygame.mixer.music.play(loops=100)
                #lose_window.configure(bg="black")
        
                lose=PhotoImage(file="C:/jenitemp/lose.png")
                lose_label=Label(lose_window,image=lose,width=650,height=650).pack()
                button_close=Button(lose_window,text="EXIT",command=lambda: [root.destroy(),stop_music()],width=20,height=50,bg="grey",fg="white").pack(pady=20)

              elif computer<player:
                won_window=Toplevel()
                won_window.attributes("-fullscreen",True)

                pygame.mixer.music.load("C:/jenitemp/win_sound.mp3")
                pygame.mixer.music.play(loops=100)
                #won_window.configure(bg="black")
      
                won=PhotoImage(file="C:/jenitemp/win.png")
                won_label=Label(won_window,image=won,width=650,height=650).pack(pady=3)
                button_close=Button(won_window,text="EXIT",command=lambda: [root.destroy(),stop_music()],width=20,height=50,bg="grey",fg="white").pack(pady=20)

              elif computer==player:
                draw_window=Toplevel()
                draw_window.attributes("-fullscreen",True)
        
                pygame.mixer.music.load("C:\jenitemp\draw_sound.mp3")
                pygame.mixer.music.play(loops=100)
                #draw_window.configure(bg="black")
      
                draw=PhotoImage(file="C:/jenitemp/draw.png")
                draw_label=Label(draw_window,image=draw,width=650,height=650).pack()
                button_close=Button(draw_window,text="EXIT",command=lambda: [root.destroy(),stop_music()],width=20,height=50,bg="grey",fg="white").pack(pady=20)

      
            return
    
    
    
    

        #graphics and button functions
        
        root = Tk()
        root.configure(bg="turquoise") 
        root.state("zoomed")
        root.title("Rock Paper Scissor")
        pygame.mixer.init()

        rock_image=PhotoImage(file = "C:/jenitemp/rock.png")
        paper_image=PhotoImage(file = "C:/jenitemp/paper.png")
        scissor_image=PhotoImage(file = "C:/jenitemp/scissor.png")


        rock_img=PhotoImage(file = "C:/jenitemp/rock1.png")
        paper_img=PhotoImage(file = "C:/jenitemp/paper1.png")
        scissor_img=PhotoImage(file = "C:/jenitemp/scissor1.png")


        rock_button= Button(root,image=rock_img,bg="gold",width=340,height=200,command=lambda *args: button_choice("rock"))
        paper_button= Button(root,image=paper_img,bg="gold",width=340,height=200,command=lambda *args: button_choice("paper"))
        scissor_button= Button(root,image=scissor_img,bg="gold",width=340,height=200,command=lambda *args: button_choice("scissor"))


        rock_button.grid(row=2,column=0)
        paper_button.grid(row=2,column=1)
        scissor_button.grid(row=2,column=2)


        fillup_label1=Label(root,text="            ",width=85,height=23,bg="turquoise").grid(row=1,column=1)
        rule_label=Label(root,text="First to get\n 5 points\n wins!",bg="turquoise",font=10).grid(row=1,column=1)


        score_label=Label(root,text=("COMPUTER : "+str(computer)+ "  PLAYER : "+str(player)),width=30,height=5,bg="black",fg="gold",font=("Arial",12))
        score_label.grid(row=0,column=1)



        open_window = Toplevel()
        open_window.attributes("-fullscreen",True)
        open_window.attributes("-topmost", True)
        #open_window.wm_transient(root)



        pygame.mixer.music.load("C:/jenitemp/house_lo.mp3")
        pygame.mixer.music.play(loops=100)

        Video_label=Label(open_window)
        Video_label.pack()
        
        video_player=tkvideo("C:/jenitemp/rps_vid.mp4",
                       Video_label,
                       loop=1,
                       size=(1200,680))
        video_player.play()
        

        startgame_button = Button(open_window, text = "START GAME",command=open_window.destroy,bg="orange").pack(pady=4)


 
        root.mainloop()



    elif choice==4:
        print()
        print("THANK YOU!")
        game=False

    else:
        print()
        print("Invalid choice")
        print()
        



























        
