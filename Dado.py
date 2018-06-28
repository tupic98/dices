from random import randint
from time import sleep

import wx

#Creando variables
i=0
dado=0
turn = 0
intent = 0
intent1 = 0
intent2 = 0
intent3 = 0
intent4 = 0
win = 0
wins = 0
loses = 0

class Dice(wx.Frame):
    def __init__(self,*args,**kwargs):
        # Levantar ventana
        wx.Frame.__init__(self,*args,**kwargs)
        self.Show()
        self.SetBackgroundColour(wx.Colour(0,0,0))
        # Creando un lienzo para poder empezar a trabajar en el
        panel=wx.Panel(self,-1, pos=(0,0), size=(800,600))
        # Cambiando el fondo del lienzo a negro
        panel.SetBackgroundColour(wx.Colour(0,0,0))

        # Cargando botones
        button1 = wx.Button(panel, -1, "Lanzar dado" ,pos=(336, 485), size=(128, 20), style=10)
        refresh = wx.BitmapButton(
            panel, -1, wx.Bitmap('refreshing.png', wx.BITMAP_TYPE_ANY), wx.Point(368, 463), wx.Size(64, 64), 0);
        refresh.Hide()
        # Cargando texto
        Perdidas = wx.StaticText(self, id=-1, label="Partidas perdidas: %d" %loses, pos=(550, 400),
                                 size=(200, 50), style=wx.ALIGN_LEFT)

        Ganadas = wx.StaticText(self, id=-1, label="Partidas ganadas: %d" %wins, pos=(550, 450),
                                 size=(200, 50), style=wx.ALIGN_LEFT)
        # CAmbiando color de los textos a blanco
        Perdidas.SetForegroundColour((255,255,255))
        Ganadas.SetForegroundColour((255,255,255))

        # Definiendo funcion para el evento cuando el boton de lanzar dado
        def on_lanzar_listener(event):
            global dado
            global i
            global turn
            turn = turn + 1
            i = 0
            # Creando un bucle de 8 iteraciones para que el dado "gire" 8 veces
            for i in range(0,8):
                # Creando un numero al azar para saber que cara del dado mostrat
                dado = randint(1, 6)
                print("=============")
                print(dado)
                # Llamando funcion de "girar" dado
                roll_dice(dado)
                print("=============")
                # Esto es porque en la iteracion de 8, se genera 8 veces un numero pero solo se llama la funcion de girar 7 veces
                # entonces solo se toma el septimo valor generado que es en el que se basa que cara del dado se mostrara
                if i == 6:
                    intent = dado
            print(intent)
            print(turn)
            # Llamando la funcion para poner en los turnos que lado del dado cayo
            set_dice_turn(intent,turn)

        # Funcion de girar dado
        def roll_dice(turn):
            global dado1verde
            global dado2verde
            global dado3verde
            global dado4verde
            global dado5verde
            global dado6verde
            # Variable turn es para saber que numero se genero para empezar a girar el dado
            # Dependiendo de que numero es, este muestra la imagen de la cara del dado correspondiente al numero
            # por 0.1 segundos, para que despues se muestre la siguiente hasta que se acaben las 8 iteraciones
            if turn == 1:
                # Renderizando imagen de la cara del dado
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

        # Definiendo funcion para poner la cara del dao que corresponda a cada turno
        def set_dice_turn(intent, turn):
            global dado1azulfirst, dado2azulfirst, dado3azulfirst, dado4azulfirst, dado5azulfirst, dado6azulfirst
            global dado1azulsecond, dado2azulsecond, dado3azulsecond, dado4azulsecond, dado5azulsecond, dado6azulsecond
            global dado1azulthird, dado2azulthird, dado3azulthird, dado4azulthird, dado5azulthird, dado6azulthird
            global dado1azulfourth, dado2azulfourth, dado3azulfourth, dado4azulfourth, dado5azulfourth, dado6azulfourth
            global intent1, intent2, intent3, intent4
            global win, wins, loses
            # En este, se toma en cuenta que turno es y que cara del dado cayo en la funcion de girar el dado
            # Solo son 4 turnos, y en cada turno se evalua que cara del dado cayo, y al identificar cual es, este
            # renderiza la imagen correspondiente a esa cara
            if turn == 1:
                # Se renderiza texto del primer turno
                texto = wx.StaticText(panel, id=-1, label="1er tiro", pos=(100, 25), size=(128, 40), style=wx.ALIGN_CENTER)
                texto.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    # Seteando una variable para saber que cara se puso en el turno, para luego ocuparla
                    # en la funcion de resetear, en donde solo se eliminan las imagenes que se setearon
                    intent1 = 1
                    # Renderizando imagen del primer turno
                    dado1azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 2:
                    intent1 = 2
                    dado2azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 3:
                    intent1 = 3
                    dado3azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 4:
                    intent1 = 4
                    dado4azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 5:
                    intent1 = 5
                    dado5azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                if intent == 6:
                    intent1 = 6
                    dado6azulfirst = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(100, 75), size=(128, 128))
                    win = win + 1
            if turn == 2:
                texto2 = wx.StaticText(panel, id=-1, label="2do tiro", pos=(250, 25), size=(128, 40),
                                      style=wx.ALIGN_CENTER)
                texto2.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    intent2 = 1
                    dado1azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 2:
                    intent2 = 2
                    dado2azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 3:
                    intent2 = 3
                    dado3azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 4:
                    intent2 = 4
                    dado4azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 5:
                    intent2 = 5
                    dado5azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                if intent == 6:
                    intent2 = 6
                    dado6azulsecond = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(250, 75), size=(128, 128))
                    win = win + 2
            if turn == 3:
                texto3 = wx.StaticText(panel, id=-1, label="3er tiro", pos=(400, 25), size=(128, 40),
                                      style=wx.ALIGN_CENTER)
                texto3.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    intent3 = 1
                    dado1azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 2:
                    intent3 = 2
                    dado2azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 3:
                    intent3 = 3
                    dado3azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 4:
                    intent3 = 4
                    dado4azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 5:
                    intent3 = 5
                    dado5azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                if intent == 6:
                    intent3 = 6
                    dado6azulthird = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                     pos=wx.Point(400, 75), size=(128, 128))
                    win = win + 1
            if turn == 4:
                texto4 = wx.StaticText(panel, id=-1, label="4to tiro", pos=(550, 25), size=(128, 40),
                                      style=wx.ALIGN_CENTER)
                texto4.SetForegroundColour((255, 255, 255))
                if intent == 1:
                    intent4 = 1
                    dado1azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('1azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 2:
                    intent4 = 2
                    dado2azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('2 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 3:
                    intent4 = 3
                    dado3azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('3 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 4:
                    intent4 = 4
                    dado4azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('4 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 5:
                    intent4 = 5
                    dado5azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('5 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
                if intent == 6:
                    intent4 = 6
                    win = win + 1
                    dado6azulfourth = wx.StaticBitmap(panel, -1, wx.Bitmap('6 azul.png', wx.BITMAP_TYPE_ANY),
                                                      pos=wx.Point(550, 75), size=(128, 128))
            # Si el turno es el ultimo, se entra a la condicional para poder contar si hubo algun 6 en los
            # intentos y mostrar si se gano o no, ademas de que se muestra el boton de reset
            if turn == 4:
                if win == 1 or win == 2 or win == 3 or win == 4:
                    wins = wins + 1
                else:
                    loses = loses + 1
                Ganadas.SetLabel("Partidas ganadas: %d" % wins)
                Perdidas.SetLabel("Partidas perdidas: %d" % loses)
                button1.Enable(False)
                button1.Hide()
                refresh.Show()
        # Se define la funcion que hara lo que sea necesario para resetear y ya no mostrar nada
        def on_reset(event):
            global turn
            global win
            # Se resetea auxiliar para contar cuantas veces cayo un 6
            win = 0
            # Se esconde el boton de reset
            refresh.Hide()
            # Dependiendo que imagen de la cara del dado este renderizda, oculta estas
            if intent1 == 1:
                dado1azulfirst.Hide()
            if intent1 == 2:
                dado2azulfirst.Hide()
            if intent1 == 3:
                dado3azulfirst.Hide()
            if intent1 == 4:
                dado4azulfirst.Hide()
            if intent1 == 5:
                dado5azulfirst.Hide()
            if intent1 == 6:
                dado6azulfirst.Hide()
            if intent2 == 1:
                dado1azulsecond.Hide()
            if intent2 == 2:
                dado2azulsecond.Hide()
            if intent2 == 3:
                dado3azulsecond.Hide()
            if intent2 == 4:
                dado4azulsecond.Hide()
            if intent2 == 5:
                dado5azulsecond.Hide()
            if intent2 == 6:
                dado6azulsecond.Hide()
            if intent3 == 1:
                dado1azulthird.Hide()
            if intent3 == 2:
                dado2azulthird.Hide()
            if intent3 == 3:
                dado3azulthird.Hide()
            if intent3 == 4:
                dado4azulthird.Hide()
            if intent3 == 5:
                dado5azulthird.Hide()
            if intent3 == 6:
                dado6azulthird.Hide()
            if intent4 == 1:
                dado1azulfourth.Hide()
            if intent4 == 2:
                dado2azulfourth.Hide()
            if intent4 == 3:
                dado3azulfourth.Hide()
            if intent4 == 4:
                dado4azulfourth.Hide()
            if intent4 == 5:
                dado5azulfourth.Hide()
            if intent4 == 6:
                dado6azulfourth.Hide()
            # Oculta las imagenes que se muestran a la hora de "girar" el dado
            dado1verde.Hide()
            dado2verde.Hide()
            dado3verde.Hide()
            dado4verde.Hide()
            dado5verde.Hide()
            dado6verde.Hide()
            # Mostrar boton de lanzar dado
            button1.Show()
            button1.Enable(True)
            # Setear los turnos a cero para que empiecen a contar otra vez
            turn = 0
        # Evento del boton lanzar dado
        button1.Bind(wx.EVT_BUTTON, on_lanzar_listener)
        # Evento del boton reset
        refresh.Bind(wx.EVT_BUTTON, on_reset)

# Cosas de wxpython para que se pueda renderizar la ventana
if __name__ == '__main__':
    app = wx.App()
    fr = Dice(None, -1, "Juego de dados", size=(800 ,600), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
    app.MainLoop()
