from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *







bot= ChatBot("My Bot")




convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot',
    'how are you ?',
    'I am doing great these days',
   'thank you',
    'In which city you live ?',
    'I live in NAGPUR',
    'In which language you talk?',
    ' I mostly talk in english',
    'who is your owner? ',
    'My owner is Chetan',
    'How many wife does atharva have?',
    'He has two wives . first wife name is asawari and other name is anushree',
    'who is sakshi"s best friend?',
    'Sakthi'
    'who is the beautiful girl in this world',
    'Your Dumbo',
    'what is your favourite color?',
    'my favourite colour is blue',
    'who is the dangerous girl in nagpur?' ,
    'akansha',
    'who is most handsome guyin the nagpur?',
    'you ! Chetan'

]
trainer = ListTrainer(bot)

 #now training the bot with the help of trainer
trainer.train(convo)


#answer = bot.get_response("what is your name?")
#print(answer)

#print("Talk to bot ")
#while True:
     #query = input()
     #if query == 'exit':
      #   break
     #answer = bot.get_response(query)
     #print("bot : ", answer)


main = Tk()
main.geometry("500x650")
main.title("My Google Assistant")
img = PhotoImage(file="chaticon.png")



photoL= Label(main, image=img)
photoL.pack(pady=20)

def ask_from_google_Assistant():
    query= textF.get()
    answer_from_google_Assistant =bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_google_Assistant))
    textF.delete(0, END)
    msgs.yview(END)

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
#creating text field

textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)


btn= Button(main, text="Ask from Google Assistant", font=("Verdana",20), command= ask_from_google_Assistant)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()


#going to bind main window with enter key...
main.bind('<Return>', enter_function)







main.mainloop()
