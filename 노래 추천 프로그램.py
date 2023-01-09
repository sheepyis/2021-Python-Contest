from tkinter import *
from tkinter import messagebox
import random, winsound

root=Tk()
root.title("오늘의 추천 곡")
root.geometry("800x700+500+200")

wall=PhotoImage(file="배경.png")
wall_label=Label(root, image=wall)
wall_label.place(x=0, y=0)

def 팝송():
    pop=["Birthday","Goodbyes","Liability","85%","Dynasty"]
    if random.choice(pop)=="Birthday":
        la2.configure(text="Birthday - Anne-Marie", font="고딕 12", background="yellow")
        la3.configure(image=photo1)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Birthday.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Don't Play(2021.01.15)")
        
    elif random.choice(pop)=="Goodbyes":
        la2.configure(text="Goodbyes - Post Malon", font="고딕 12", background="yellow")
        la3.configure(image=photo2)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Goodbyes.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Goodbyes(2019.07.04)")
        
    elif random.choice(pop)=="Liability":
        la2.configure(text="Liability - Lorde", font="고딕 12", background="yellow")
        la3.configure(image=photo3)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Liability.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Melodrama(2017.06.16)")
        
    elif random.choice(pop)=="85%":
        la2.configure(text="85% - Loote", font="고딕 12", background="yellow")
        la3.configure(image=photo4)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("85.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: lost(2019.06.14)")

    elif random.choice(pop)=="Dynasty":
        la2.configure(text="Dynasty - Miia", font="고딕 12", background="yellow")
        la3.configure(image=photo17)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Dynasty.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Dynasty(2020.06.11)")

def 케이팝():
    kpop=["우아하게","Universe","Dynamite","으르렁","전야"]
    if random.choice(kpop)=="우아하게":
        la2.configure(text="우아하게 - TWICE", font="고딕 12", background="pink")
        la3.configure(image=photo5)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("OOH-AHH.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: THE STORY BEGINS(2015.10.20)")
        
    elif random.choice(kpop)=="Universe":
        la2.configure(text="Universe - 민현(뉴이스트)", font="고딕 12", background="pink")
        la3.configure(image=photo6)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Universe.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Single 'Universe'(2019.04.03)")
        
    elif random.choice(kpop)=="Dynamite":
        la2.configure(text="Dynamite - 방탄소년단", font="고딕 12", background="pink")
        la3.configure(image=photo7)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Dynamite.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Dynamite(DayTime Version(2020.08.21)")

    elif random.choice(kpop)=="으르렁":
        la2.configure(text="으르렁 - EXO", font="고딕 12", background="pink")
        la3.configure(image=photo8)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("으르렁.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: The 1st Album 'XOXO(Kiss&Hug)' Repackage(2013.08.05)")

    elif random.choice(kpop)=="전야":
        la2.configure(text="전야 - EXO", font="고딕 12", background="pink")
        la3.configure(image=photo18)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("전야.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: The War - The 4th Album(2017.07.18)")

def 발라드():
    ballad=["신촌을 못가","바람이 불었으면 좋겠어","초록빛","눈사람","Hello"]
    if random.choice(ballad)=="신촌을 못가":
        la2.configure(text="신촌을 못가 - 포스트맨", font="고딕 12", background="skyblue")
        la3.configure(image=photo9)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("신촌을 못가.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 신촌을 못가(2013.01.21)")

    elif random.choice(ballad)=="바람이 불었으면 좋겠어":
        la2.configure(text="바람이 불었으면 좋겠어 - 길구봉구", font="고딕 12", background="skyblue")
        la3.configure(image=photo10)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("바람이 불었으면 좋겠어.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 바람이 불었으면 좋겠어(2014.01.03)")

    elif random.choice(ballad)=="초록빛":
        la2.configure(text="초록빛 - 폴킴", font="고딕 12", background="skyblue")
        la3.configure(image=photo11)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("초록빛.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 초록빛(2019.01.17)")

    elif random.choice(ballad)=="눈사람":
        la2.configure(text="눈사람 - 정승환", font="고딕 12", background="skyblue")
        la3.configure(image=photo12)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("눈사람.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 그리고 봄(2018.02.19)")

    elif random.choice(ballad)=="Hello":
        la2.configure(text="Hello - 허각", font="고딕 12", background="skyblue")
        la3.configure(image=photo19)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Hello.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Like 1st Mini Album 'First Story'(2011.09.16)")

def 랩():
    rap=["사람","우리서로사랑하지는말자","Achoo","METEOR","시차"]
    if random.choice(rap)=="사람":
        la2.configure(text="사람 - 지코", font="고딕 12", background="lightgreen")
        la3.configure(image=photo13)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("사람.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: THINKING Part.1(2019.09.30)")

    elif random.choice(rap)=="우리서로사랑하지는말자":
        la2.configure(text="우리서로사랑하지는말자 - 기리보이", font="고딕 12", background="lightgreen")
        la3.configure(image=photo14)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("우리서로사랑하지는말자.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 영화같게(2020.10.04)")
        
    elif random.choice(rap)=="Achoo":
        la2.configure(text="Achoo - 미란이", font="고딕 12", background="lightgreen")
        la3.configure(image=photo15)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Achoo.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 쇼미더머니 9 Episode 3(2020.12.05)")

    elif random.choice(rap)=="METEOR":
        la2.configure(text="Meteor - 창모", font="고딕 12", background="lightgreen")
        la3.configure(image=photo16)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Meteor.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Boyhood(2019.11.29)")

    elif random.choice(rap)=="시차":
        la2.configure(text="시차 - 우원재", font="고딕 12", background="lightgreen")
        la3.configure(image=photo20)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("시차.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 시차(We Are)(2017.09.04)")

def 듀엣곡():
    song=["널 사랑하지 않아","그리워","이별은 늘 그렇게","우리 사랑 이대로","Dinosaur"]
    if random.choice(song)=="널 사랑하지 않아":
        la2.configure(text="널 사랑하지 않아 - 어반자카파", font="고딕 12", background="orange")
        la3.configure(image=photo21)
        la4.configure(text="오늘의 듀엣곡 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("널 사랑하지 않아.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Still(2016.05.27)")

    elif random.choice(song)=="그리워":
        la2.configure(text="그리워 - 효린, 양다일", font="고딕 12", background="orange")
        la3.configure(image=photo22)
        la4.configure(text="오늘의 듀엣곡 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("그리워.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 그리워(2016.08.31)")

    elif random.choice(song)=="이별은 늘 그렇게":
        la2.configure(text="이별은 늘 그렇게 - 허각, 정은지", font="고딕 12", background="orange")
        la3.configure(image=photo23)
        la4.configure(text="오늘의 듀엣곡 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("이별은 늘 그렇게.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 이별은 늘 그렇게(2019.10.31)")

    elif random.choice(song)=="우리 사랑 이대로":
        la2.configure(text="우리 사랑 이대로 - 서인국, 정은지", font="고딕 12", background="orange")
        la3.configure(image=photo24)
        la4.configure(text="오늘의 듀엣곡 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("우리 사랑 이대로.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: 응답하라 1997 Love Story Part 2(2012.09.04)")

    elif random.choice(song)=="Dinosaur":
        la2.configure(text="Dinosaur - 악동뮤지션", font="고딕 12", background="orange")
        la3.configure(image=photo25)
        la4.configure(text="오늘의 듀엣곡 추천 곡은?", font="고딕 15 bold", background="mistyrose")
        winsound.PlaySound("Dinosaur.wav", winsound.SND_ASYNC)
        messagebox.showinfo("곡 정보","앨범명: Summer Episode(2017.07.20)")

photo1=PhotoImage(file="1.png")
photo2=PhotoImage(file="2.png")
photo3=PhotoImage(file="3.png")
photo4=PhotoImage(file="4.png")
photo5=PhotoImage(file="5.png")
photo6=PhotoImage(file="6.png")
photo7=PhotoImage(file="7.png")
photo8=PhotoImage(file="8.png")
photo9=PhotoImage(file="9.png")
photo10=PhotoImage(file="10.png")
photo11=PhotoImage(file="11.png")
photo12=PhotoImage(file="12.png")
photo13=PhotoImage(file="13.png")
photo14=PhotoImage(file="14.png")
photo15=PhotoImage(file="15.png")
photo16=PhotoImage(file="16.png")
photo17=PhotoImage(file="17.png")
photo18=PhotoImage(file="18.png")
photo19=PhotoImage(file="19.png")
photo20=PhotoImage(file="20.png")
photo21=PhotoImage(file="21.png")
photo22=PhotoImage(file="22.png")
photo23=PhotoImage(file="23.png")
photo24=PhotoImage(file="24.png")
photo25=PhotoImage(file="25.png")

la1=Label(root, text="<오늘의 추천 곡>", font="고딕 20 bold", background="lightsalmon")
la2=Label(root, text="")
la3=Label(root, text="")
la4=Label(root, text="")
la5=Label(root, text="IT공과대학 2171339 양인서", font="고딕 10 bold", background="white")

bt1=Button(root, text="팝송", bg="yellow", command=팝송, width=30, height=2)
bt2=Button(root, text="케이팝", bg="pink", command=케이팝, width=30, height=2)
bt3=Button(root, text="발라드", bg="skyblue", command=발라드, width=30, height=2)
bt4=Button(root, text="랩/힙합", bg="lightgreen", command=랩, width=30, height=2)
bt5=Button(root, text="듀엣곡", bg="orange", command=듀엣곡, width=30, height=2)

la1.place(x=290, y=20)
la3.place(x=370, y=90)
la2.place(x=60, y=550)
la4.place(x=60, y=500)
la5.place(x=600, y=650)
bt1.place(x=60, y=100)
bt2.place(x=60, y=170)
bt3.place(x=60, y=240)
bt4.place(x=60, y=310)
bt5.place(x=60, y=380)

root.mainloop()
