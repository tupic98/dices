#/usr/bin/python

import wx
from random import randint
from time import sleep
import locale
import winsound


i=0
dado=0
turn = 0
intent = 0


class dice(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.Show()
        self.SetBackgroundColour(wx.Colour(0,0,0))
        panel=wx.Panel(self,-1, pos=(0,0), size=(800,600))
        panel.SetBackgroundColour(wx.Colour(0,0,0))

        # Cargando boton
        button1 = wx.Button(panel, -1, "Lanzar dado" ,pos=(336, 485), size=(128, 20), style=10)

        def on_lanzar_listener(event):
            global dado
            global i
            global turn
            turn = turn + 1
            i = 0
            for i in range(0,8):
                dado = randint(1, 6)
                print("=============")
                print(dado)
                roll_dice(dado)
                print("=============")
                if i == 6:
                    intent = dado
            print(intent)
            print(turn)
            set_dice_turn(intent,turn)

        def roll_dice(turn):
            if turn == 1:
                dado1verde = wx.StaticBitmap(panel, -1, wx.Bitmap('1 verde.png', wx.BITMAP_TYPE_ANY),
                                             pos=wx.Point(336, 290), size=(128, 128))
            if turn == 2:
                dado2verde = wx.StaticBitmap(panel, -1, wx.Bitmap('2 verde.png', wx.BITMAP_TYPE_ANY),
                                             pos=wx.Point(336, 290), size=(128, 128))
            if turn == 3:
                dado3verde = wx.StaticBitmap(panel, -1, wx.Bitmap('3 verde.png', wx.BITMAP_TYPE_ANY),
                                             pos=wx.Point(336, 290), size=(128, 128))
            if turn == 4:
                dado4verde = wx.StaticBitmap(panel, -1, wx.Bitmap('4 verde.png', wx.BITMAP_TYPE_ANY),
                                             pos=wx.Point(336, 290), size=(128, 128))
            if turn == 5:
                dado5verde = wx.StaticBitmap(panel, -1, wx.Bitmap('5 verde.png', wx.BITMAP_TYPE_ANY),
                                             pos=wx.Point(336, 290), size=(128, 128))
            if turn == 6:
                dado6verde = wx.StaticBitmap(panel, -1, wx.Bitmap('6 verde.png', wx.BITMAP_TYPE_ANY),
                                             pos=wx.Point(336, 290), size=(128, 128))
            sleep(0.10)

        def set_dice_turn(intent, turn):
            if turn == 1:
                texto = wx.StaticText(panel, id=-1, label="1er tiro", pos=(100, 25), size=(128, 40), style=wx.ALIGN_CENTER)
                texto.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    dado1azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 2:
                    dado2azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 3:
                    dado3azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 4:
                    dado4azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 5:
                    dado5azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 6:
                    dado6azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
            if turn == 2:
                texto2 = wx.StaticText(panel, id=-1, label="2do tiro", pos=(250, 25), size=(128, 40),
                                      style=wx.ALIGN_CENTER)
                texto2.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    dado1azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 2:
                    dado2azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 3:
                    dado3azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 4:
                    dado4azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 5:
                    dado5azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 6:
                    dado6azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
            if turn == 3:
                texto3 = wx.StaticText(panel, id=-1, label="3er tiro", pos=(400, 25), size=(128, 40),
                                      style=wx.ALIGN_CENTER)
                texto3.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    dado1azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 2:
                    dado2azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 3:
                    dado3azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 4:
                    dado4azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 5:
                    dado5azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 6:
                    dado6azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
            if turn == 4:
                texto4 = wx.StaticText(panel, id=-1, label="4to tiro", pos=(550, 25), size=(128, 40),
                                      style=wx.ALIGN_CENTER)
                texto4.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    dado1azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 2:
                    dado2azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 3:
                    dado3azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 4:
                    dado4azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 5:
                    dado5azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 6:
                    dado6azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
            if turn == 4:
                button1.Enable(False)

        button1.Bind(wx.EVT_BUTTON, on_lanzar_listener)


if __name__=='__main__':
    app = wx.App()
    fr = dice(None, -1, "Juego de dados", size=(800,600),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
    app.MainLoop()
