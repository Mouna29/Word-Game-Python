from string import punctuation
import PySimpleGUI as sg
alphabets={}
print(type(alphabets))
counter=1
while counter<=26:
  alphabets[chr(64+counter)]=counter
  counter+=1

print(alphabets)

sg.theme("DarkBrown")
l1=sg.Text("Welcome to the game 👊",expand_x=True, justification='center',font=('Arial Bold', 20))
l2=sg.Text("Enter your word here",font=('Arial', 15))
t1=sg.Input('', key='-WORD-', font=('Arial', 20),text_color="ivory",size=(30,25),justification='left',do_not_clear=True)
b1=sg.Button("Get score",size=(10,1),font=('Arial', 13),button_color=("#008080","#E1C16E"),border_width=0)
layout=[[l1],[l2],[t1],[b1]]
window=sg.Window("Word Score",layout)
while True:
  event,values=window.read()
  if event==sg.WIN_CLOSED:
    break
  elif event == "Get score":
    has_digits=False
    score=0
    word=values["-WORD-"]
    for char in list(word.upper()):
      if char in ('0123456789') or char in punctuation:
        has_digits=True
        break 
      elif char in alphabets:
        score+=alphabets[char]
    if score==0 or has_digits:
      sg.popup("Please enter a valid word",button_color=("#008080","#E1C16E"),font=('Arial', 15))
    else:
      sg.popup("Your word:",values["-WORD-"],"has a score of :",score,button_color=("#008080","#E1C16E"),font=('Arial', 15)) 
window.close()