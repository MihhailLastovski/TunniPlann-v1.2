from tkinter import *
from tkinter.messagebox import *
import time
import os
def failist_sõnastikusse():
	tund_kirjeldus={}
	file=open("Tunnid_kirjeldused.txt","r")
	for line in file:
		tund,kirjeldus=line.strip().split(":")
		tund_kirjeldus[tund.strip()]=kirjeldus.strip()
	file.close()
	print(tund_kirjeldus)
	return tund_kirjeldus

tund_kirjeldus=failist_sõnastikusse()
def kirjeldus_aknasse(t:str):
	if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
		alam_aken=Toplevel()
		lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
		alam_aken.geometry("400x400")
		c=Canvas(alam_aken,height=500,width=500)
		file=PhotoImage(file=t)
		c.create_image(10,10,image=file,anchor=NW)
		c.pack()
		alam_aken.mainloop()
	else:
		showinfo("Vastus","Kui ei taha,siis ei taha!")

j=0
aken=Tk()
aken.geometry("1000x600")
aken.title("Tunniplan")
aken.configure(bg="white")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,10,2):
     Ep=Label(aken,text=p[j],heigh=4,width=10,font="Arial 15",fg="black",bg="white",relief="ridge").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
     j+=1
kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
     tn=Label(aken,text=str(i)+"\n"+kell[i],heigh=4,width=10,font="Arial 9",fg="black",bg="white",relief="ridge").grid(row=0,column=i+1,sticky=N+S+W+E)

multi=Button(aken,text="Multimeedia",heigh=1,width=6,font="Arial 9",fg="black",bg="#adc1ff",relief="ridge",command=lambda:kirjeldus_aknasse("aimult.png")).grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
multi2=Button(aken,text="Multimeedia",heigh=1,width=6,font="Arial 9",fg="black",bg="#adc1ff",relief="ridge",command=lambda:kirjeldus_aknasse("aimult.png")).grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
program=Button(aken,text="Programmeerimise alused",heigh=1,width=6,font="Arial 8",fg="black",bg="#ade1ff",relief="ridge",command=lambda:kirjeldus_aknasse("ProgP.png")).grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
program2=Button(aken,text="Programmeerimise alused",heigh=1,width=6,font="Arial 8",fg="black",bg="#ade1ff",relief="ridge",command=lambda:kirjeldus_aknasse("ProgP.png")).grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
ruhmatund=Button(aken,text="Rühmaju\nhataja\ntund",heigh=1,width=6,font="Arial 8",fg="black",bg="#ade1ff",relief="ridge",command=lambda:kirjeldus_aknasse("logo_4.png")).grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)
inglis=Button(aken,text="Inglise keel",heigh=1,width=6,font="Arial 9",fg="black",bg="#fffff0",relief="ridge").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
inglis2=Button(aken,text="Inglise keel",heigh=1,width=6,font="Arial 9",fg="black",bg="#e1adff",relief="ridge").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
oper=Button(aken,text="Operatsioonisüstee\nmide alused",heigh=1,width=6,font="Arial 8",fg="black",bg="#e181ff",relief="ridge").grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
fizra=Button(aken,text="Kehaline kasvatus",heigh=1,width=6,font="Arial 8",fg="black",bg="#e181c1",relief="ridge").grid(row=3,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
eesti=Button(aken,text="Eesti keel",heigh=1,width=6,font="Arial 8",fg="black",bg="#cdb5ff",relief="ridge").grid(row=3,column=9,sticky=N+S+W+E)
eesti2=Button(aken,text="Eesti keel",heigh=1,width=6,font="Arial 8",fg="black",bg="#cbb6c8",relief="ridge").grid(row=4,column=9,sticky=N+S+W+E)
ajalugu=Button(aken,text="Ajalugu,\ninimgeogr\naafia ja\ninimese\nõpetus\neesti\nkeeles",heigh=1,width=6,font="Arial 8",fg="black",bg="#ffe7b4",relief="ridge").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)
program3=Button(aken,text="Programmeerimise alused",heigh=1,width=6,font="Arial 8",fg="black",bg="#ade1ff",relief="ridge").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
multi3=Button(aken,text="Multimeedia",heigh=1,width=6,font="Arial 9",fg="black",bg="#adc1ff",relief="ridge").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
program4=Button(aken,text="Programmeerimise alused",heigh=1,width=6,font="Arial 8",fg="black",bg="#ade1ff",relief="ridge").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
multi4=Button(aken,text="Multimeedia",heigh=1,width=6,font="Arial 9",fg="black",bg="#adc1ff",relief="ridge").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
kunst=Button(aken,text="Kunstiained",heigh=1,width=6,font="Arial 9",fg="black",bg="#e181cf",relief="ridge").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)
andmedbass=Button(aken,text="Andmebaasisüstee\nmide alused (eesti\nkeeles)",heigh=1,width=6,font="Arial 8",fg="black",bg="#ff81a2",relief="ridge").grid(row=7,column=2,columnspan=2,rowspan=2,sticky=N+S+W+E)
andmedbass2=Button(aken,text="Andmebaasisüsteemide\nalused (eesti keeles)",heigh=1,width=6,font="Arial 8",fg="black",bg="#ff81a2",relief="ridge").grid(row=7,column=4,columnspan=3,rowspan=2,sticky=N+S+W+E)
ajalugu2=Button(aken,text="Ajalugu,\ninimgeogr\naafia ja\ninimese\nõpetus\neesti\nkeeles",heigh=1,width=6,font="Arial 8",fg="black",bg="#ffe7b4",relief="ridge").grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
eesti3=Button(aken,text="Eesti keel",heigh=1,width=6,font="Arial 8",fg="black",bg="#cdb5ff",relief="ridge").grid(row=7,column=8,sticky=N+S+W+E)
eesti4=Button(aken,text="Eesti keel",heigh=1,width=6,font="Arial 8",fg="black",bg="#cbb6c8",relief="ridge").grid(row=8,column=8,sticky=N+S+W+E)
kirjandus=Button(aken,text="Keel ja kirjandus",heigh=1,width=6,font="Arial 9",fg="black",bg="#e1ff81",relief="ridge").grid(row=9,column=2,columnspan=2,rowspan=2,sticky=N+S+W+E)
matem=Button(aken,text="Matemaatika",heigh=1,width=6,font="Arial 9",fg="black",bg="#fcbad2",relief="ridge").grid(row=9,column=5,columnspan=2,rowspan=2,sticky=N+S+W+E)
suhtlen=Button(aken,text="Suhtlemine ja\nklienditeenindus",heigh=1,width=6,font="Arial 9",fg="black",bg="#c1adff",relief="ridge").grid(row=9,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
ajalugu3=Button(aken,text="Ajalugu,\ninimgeogr\naafia ja\ninimese\nõpetus\neesti\nkeeles",heigh=1,width=6,font="Arial 8",fg="black",bg="#ffe7b4",relief="ridge").grid(row=9,column=9,rowspan=2,sticky=N+S+W+E)
aken.mainloop()

#def update(ind):

#    frame = frames[ind]
#    ind += 1
#    if ind == frameCnt:
#        ind = 0
#    label.configure(image=frame)
#    aken.after(100, update, ind)
#label = Label(aken)
#label.place(x=500,y=500)
#aken.after(0, update, 0)
#aken.mainloop()