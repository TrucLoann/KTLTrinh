from turtle import Screen
import pgzrun
from pgzhelper import *

WIDTH=750                       
HEIGHT=475
chuongngaivat=[]
txuathien=0
diem=0
nhaylen=0
roixuong=1
ketthuc=False


phongnen=Actor('background')    #Them_background
khunglong=Actor('run1')         #Them hinh con khung long
khunglong.x=100                 #toa do
khunglong.y=400
hoatanhchay=['run1','run2','run3','run4','run5','run6','run7','run8']   #hoat anh chay
khunglong.images=hoatanhchay

def update():
  global txuathien, diem, nhaylen, roixuong, ketthuc, chuongngaivat
  khunglong.next_image()      # Chuyen hinh anh run1->run2->...run7
  txuathien+=1
  if txuathien > 100:
    xuongrong=Actor('catus')        #Them hinh anh xuong rong
    xuongrong.x=900                 #Toa do xuong rong
    xuongrong.y=370
    chuongngaivat.append(xuongrong)
    txuathien=0
  for xuongrong  in chuongngaivat:               #hoat anh xuong rong di chuyen
    xuongrong.x-=10
    if xuongrong.x<80:                           #cach tinh diem
      diem+=1
      chuongngaivat.remove(xuongrong)
  if keyboard.up and khunglong.y==400 :          #hoat anh nhay
    nhaylen=-25
    sounds.impact.play()
  khunglong.y+=nhaylen
  nhaylen+=roixuong
  if khunglong.y>400:                            #gooi han do cao
    nhaylen=0
    khunglong.y=400
  if khunglong.collidelist(chuongngaivat)!=-1:   #cach tinh va cham
    ketthuc=True
    chuongngaivat.remove(xuongrong)
    sounds.gameover.play()
  if keyboard.space:                        #bat dau lai
    ketthuc=False
    diem=0
    chuongngaivat=[]

  


def draw():
  phongnen.draw()               # Ve background

  if ketthuc:
      screen.draw.text( 'Game over',(280,200),color=(0,0,0),fontsize=50)
      screen.draw.text('Diem so:'+ str(diem),(280,230),color=(0,0,0),fontsize=50)
      screen.draw.text( 'Nhan SPACE de bat dau lai',(170,270),color=(255,0,255),fontsize=50)

  else:
     khunglong.draw()
     for xuongrong in chuongngaivat:
      xuongrong.draw()
  screen.draw.text('DIEM SO: '+ str(diem),(10,15),color=(255,0,255),fontsize=35)
pgzrun.go()                     #Khoi chay
