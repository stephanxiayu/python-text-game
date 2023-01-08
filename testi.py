
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
task1=input("Möchtest du den Schatz finden oder zu Hause bleiben? Y für Schatz finden und N für zu Hause bleiben: ").lower()




tod1="Du gehts in den Wald, wo du nach drei Metern von einer riesigen giftigen Spinne gebissen wirst. Das Gift ist so stark, dass du innerhalb von 20 Minuten qualvoll stirbst! GAME OVER!"
tod2=" du läufst weiter und leider fällt dir eine Kokusnuss auf den Kopf. Die erleidest eine schere Kopfverletzung und stirbst quallvoll dort am Strand. GAME OVER!"
tod3="Der Mann möchte dir ein geschenk machen, eine junge hübsche Frau, mit der du dich verknügen kannst. Du fängst an sie und dich auszuziehen und Sex zu haben. Wärend des Sexes erschießt der Mann dich und du stirbst quallvoll... GAME OVER"
sieg="Die Frau ist dir so Dankbar, dass sie dich heiratet. Sie ist eine Millardärin. Ihr lebt glücklich zusammen und werdet beide 100 Jahre alt. SCHATZ GEFUNDEN!"
dummeAntwort="alter, bist du wirklich zu dämlich die richtige Tase zu drücken?!"

if task1=="y":
  task2=input("Deine Reise beginnt jetzt... Du bist am Strand angekommen, möchtest du nach rechts den Strand entlang gehen und schauen, oder gradeaus in den Wald gehen? schreibe r für rechts und g für geradeaus: ").lower()
  if task2=="r":
    task3=input("du findest beim spazieren ein kleines Haus mit Tür möchtest du zum Haus gehen und einfach die Tür öffnen oder am Strand weitergehen? O für öffnen oder W für weitergehen: ").lower()
    if task3 =="o":
      task4=input("gehst zum Haus und öffnest die Tür und triffst einen alten Mann... Möchtest du in ansprechen oder totschlagen? A für anspreche und t für totschlagen: ").lower()
      if task4=="t":
        task5=input("nach dem du den Mann totgeschlagen hast, entdeckst du eine gefangene hübsche Frau. Möchtest du sie befreien oder doch lieber abhauen? b für befreien oder g für gehen").lower()
        if task5 == "b":
          print(sieg)
        elif task5 == "g":
          print(tod2)
        else: print(dummeAntwort)
        
      elif task4=="a":
        print(tod3)
    elif task3== "w":
      print(tod2)
    
    else:
      print(dummeAntwort)
    
  elif task2=="g":
    print(tod1)
    
  else:
    print(dummeAntwort)
elif task1=="n": 
  print("mach es dir zu Hause gemütlich :-)")
else: 
  print(dummeAntwort)
 