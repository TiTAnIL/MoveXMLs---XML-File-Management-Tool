from tkinter import Tk, Label, Button, filedialog, messagebox
import os
import shutil
import random as rn


filelist = ''
allXMLs = "R:\\ITV\\All XML"
folder = os.getcwd() # Script Dir
if not os.path.exists(folder + '\\' + 'Output'):
	output = folder + "\\" + 'Output'
	os.makedirs(output)
else:
	output = folder + "\\" + 'Output'
logfile = open(output + "\\" + 'Missing.txt', 'w')

	
userName = os.getlogin()
CoolExit = [("Goodbye to all that"), ("Hello Goodbye"), ("I am a camera with its shutter open\nquite passive, recording, not thinking"),
("Time to Say Goodbye"), ("Bang, zoom, straight to the moon"),
("Wish me luck as you wave me goodbye"), ("Did I do that?"), ("D'oh!"), ("Here it is, your moment of Zen"), ("I love it when a plan comes together"),
("You are the weakest link, goodbye"), ("No soup for you!"), ("Schwing!"), ("Tell me what you don't like about yourself"), ("The Tribe has spoken"),
("You can kiss that one goodbye"), ("This tape will self-destruct in five seconds"), ("To the Batmobile!"), ("Two thumbs up"), ("I'll be back"), 
("May the force be with you"),("Im king of the world!"),("Yippee Ki Yay, Motherfucker"),("You've got to ask yourself one question:\nDo I feel lucky? Well, do ya, punk?"),("Go ahead, make my day"),("I love the smell of napalm in the morning"),("Hasta la vista, baby"),
("To infinity…and beyond!"), ("Alrighty then!"), ("They call me Mr. Tibbs!"), ("Shall…we…play…a…game?"), ("It’s showtime!"), ("I know kung fu"), ("I have a feeling we're not in Kansas anymore"), ("Why so serious?"),
("Thank you for your cooperation"), ("Beam me up Scotty"), ("exterminate!"), ("Shit just got real"), ("I know you are\nbut what am I"), ("I have come here to chew bubblegum and kick ass\nand I’m all out of bubblegum"), ("Well, la-de-da"),
("I have a feeling we’re not in Kansas anymore"), ("I see dead people"), ("Bazinga!"), ("Cowabunga!"), ("Hoo-ah!"), ("SHOW ME THE MONEY!!!"), ("Yeah baby"), 
("Are we having fun yet?"), ("You got it, dude"), ("Hakuna Matata!"), ("Ssssssssssssmokin!"), ("Gooble gobble, gooble gobble"), ("It’s alive! It’s alive! IT’S ALIVE!!!"), ("My momma always said, Life is like a box of chocolates\nyou never know what you’re gonna get"), 
("Game over"), ("Been there, done that, got the T-shirt"), ("All over again"), ("All done and dusted"), ("If opportunity doesn’t knock, build a door"), ("If you cannot do great things, do small things in a great way"), ("Be who you are and say what you feel, because\nthose who mind don’t matter and those who matter don’t mind"), 
("Bring me a bucket, and I'll show you a bucket!"), ("Job's Done"), ("I Need A Weapon"), ("The Cake Is A Lie!"), ("Thank You! But Our Princess Is In Another Castle!"), ("Finish Him!"), ("Done!", "OK, You go now"), 
("Yippie ka-yay, motherfucker!"), ("Why so serious?"), ("Wohoo!"), ("Let's rock!"), ("Go ahead, make my day"), ("Get back to work, you slacker!"), ("Stand in the ashes of a trillion dead souls, and ask the ghosts\nif honor matters. The silence is your answer"), 
("Okay, I've just gotta concentrate!"), ("Agh, just... I just gotta get it through here..."), ("Okay, you know what? That's close enough.\nJust hold tight"), ("Just say 'Apple'. Classic. Very simple."), ("Simple word. 'Apple'."), ("HA! I knew someone was alive in here"), ("Hello? Anyone in there?"),
("Your destination's probably not going to\ncome meet us here. Is it? So go on"), ("On ya go"), ("Go on"), ("So, once again, just... move along. One small step and everything."), ("Yeah, it's alright. Go ahead."), ("Alright, off you go!"), ("Aggh, see, now I hit that one, I hit that one..."),
("I can't do it if you're watching.\nIf you.... just turn around?"), ("I can't... I can't do it if you're watching. [nervous laugh]"), ("I'm not joking. Could you just turn around for a second?"), ("Ummmm. Yeah, I can't do it if you're watching."), ("Look down. Where am I? Where am I?"), ("On three. Ready? One... Two..."), ("Come on through to the other side"), ("There should be a portal device\non that podium over there"), ("Hey hey! You made it!"),
("Alright, you can turn around now!"), ("Okay, I've decided not to kill you. IF you press the button"), ("Oh! Wow! Good! I didn't think that was going to work"), ("Hello! This is the part where I kill you"), ("Oh! Oh! Did it kill you? Oh,\nthat would be amazing if it killed you"), ("I forbid you to press the button!"), ("Do not press that button!"), ("Ohhhhhh, we just made it! That was close"), ("We're good! Appreciate it!"), ("And off we go"),
("Huh. That was easy"), ("Agh! You're alive! Great!"), ("There. Bing! Perfect. On you go"), ("Ever have that feeling where you’re not sure\nif you’re awake or dreaming? "),
("Follow the white rabbit"), ("This Window will self destruct, ok?"), ("For a moment, nothing happened. Then, \nafter a second or so, nothing continued to happen"),
("DON’T PANIC"), ("Time is an illusion.\nLunchtime doubly so."), ("What is my purpose?"), ("Please call me Eddie if it will help you to relax"), ("If you don’t open that exit hatch this moment\nI shall zap straight off to your major data banks and\nreprogram you with a very large axe, got that?"), ("So long, and thanks for all the fish"),
("I really Cronenberged up the whole place"), ("I'm about to do to you what Limp-\n-Bizkit did to music in the late '90s"), ("We interrupt this program to annoy you\nand make things generally more irritating"), ("The mice will see you now"), ("I could have more fun in cat litter"), ("keep banging the rocks together"), ("I only know as much about myself as my mind can work out under its current conditions.\nAnd its current conditions are not good."),
('Do geese see goD?'),('Step on no petS'),('As I pee, sir, I see PisA'),
('Was it a car or a cat I saW?'),('Taco caT'),('A nut for a jar of tunA'),('Never Odd Or EveN'),
('Another day, another dollar'), ('Mi scuziii'), ('How you doin?'), ('I am cornholio'), ('Keep the change ya filthy animal'), 
('Chop your own wood\nit will warm you twice'), ('Do you wanna get high?'), ('OH MY GOD!\nI think i killed Kenny'), ('No soup for you'), ('I RUN! slower then internet explorer on a dial up connection,\nbut i run!'), ('You got it dude'), ('It takes as much energy to wish as it does to plan'), 
('Jew!'), ('Whateva, I do what I want!'), ('Aw! God-damn it!'), ('Respect ma authoritah!'), ('Wibbly-Wobbly, Timey-Wimey...Stuff\nDONE!'), ('Wer`re not worthy'), ('Resistance is futile'), 
('Member Ghostbusters?'), ('Member Dagobah? Thats where Yoda lives!'), ('Member Yoda?'), ('Member Jurassic Park?'), ('Member Chewbacca?'), ('Welcome to Shitty Wok. Can I take a order prease?'),
('Dont forget to bring a towel!'), ('TIMMAH!'), 
('Member Chewbacca again?'), ('Wubba Lubba Dub Dub!'), ('There is no Spoon' + userName), ('So we meet again' + userName + '...')]
Coool = rn.randrange(0,168)

class MoveXML:
	def __init__(self, master):
		self.master = master
		master.title("MoveXMLs")

		self.label = Label(master, text="Move XML`S from ALL XML folder")
		self.label.pack()

		self.greet_button = Button(master, text='Load Files', activebackground="Yellow", activeforeground="blue", command=lambda: load_files())
		self.greet_button.pack()
		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()
		
def load_files():
	file = filedialog.askopenfilename(initialdir=folder, filetypes=[("Only Text", "*.txt")])
	crimefile = open(file, 'r')
	crimefile = crimefile.readlines()
	crimefile = [x.strip() for x in crimefile] 
	count = 0
	for id in crimefile:
		filelist = "asset-" + id + ".xml"
		fullpath = allXMLs + "\\" + filelist
		if os.path.isfile(fullpath) == True:
			shutil.copy(fullpath, output)
		else:
			if os.path.isfile(output + "\\" + 'Missing.txt') == False:
				logfile = open(output + "\\" + 'Missing.txt', 'a')
				logfile.write(filelist + '\n')
				count =+ 1
			else:
				count =+ 1
				logfile = open(output + "\\" + 'Missing.txt', 'a')
				logfile.write(filelist + '\n')
	if count >= 1:
		logfile = open(output + "\\" + 'Missing.txt', '+a')
		messagebox.showerror("OOPS!", "I d'idnt find some files! Check missing.log")
		os.startfile(output)
	elif count == 0:
		os.startfile(output)
		messagebox.showinfo("Done!", CoolExit[Coool])

root = Tk()
my_gui = MoveXML(root)
root.mainloop()