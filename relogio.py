import Tkinter
from time import strftime, datetime
#from winsound import Beep

janela = Tkinter.Tk()

janela.title("Janela")

DEFAUTL_BG = "#0275d8"
FONT_DEFAULT = "Consolas 30"
acordar = False
despertar = Tkinter.Label(text = "Despertar as")
hora_de_acordar = Tkinter.Label(text = "00:00")

def pega():
	hora = entrada_hora.get()
	minutos = entrada_minutos.get()

	if int(hora) <= 23 and int(minutos) <= 59:
		hora_de_acordar['text'] = hora+":"+minutos

def parar_barulho():
	global acordar 
	acordar = False

relogio = Tkinter.Label()
entrada_hora = Tkinter.Entry(width = 4)
entrada_minutos = Tkinter.Entry(width = 4)
dois_pontos = Tkinter.Label(text = " : ")
botao_ok = Tkinter.Button(text = " OK ", command=pega)
mensagem = Tkinter.Label()
botao_parar = Tkinter.Button(text = "Parar som", command = parar_barulho)

despertar.pack(side = Tkinter.TOP)
hora_de_acordar.pack(side = Tkinter.TOP)
relogio.pack()
mensagem.pack(side = Tkinter.TOP)
entrada_hora.pack(side = Tkinter.LEFT)
dois_pontos.pack(side = Tkinter.LEFT)
entrada_minutos.pack(side = Tkinter.LEFT)
botao_ok.pack(side = Tkinter.LEFT)

despertar['font'] = FONT_DEFAULT
hora_de_acordar['font'] = FONT_DEFAULT
relogio['font'] = "Arial 200 bold"
entrada_hora['font'] = FONT_DEFAULT
dois_pontos['font'] = FONT_DEFAULT
entrada_minutos['font'] = FONT_DEFAULT
botao_ok['font'] = "Consolas 20"
botao_parar['font'] = "Consolas 20"

mensagem['font'] = FONT_DEFAULT

janela['bg'] = DEFAUTL_BG
despertar['bg'] = DEFAUTL_BG
hora_de_acordar['bg'] = DEFAUTL_BG
relogio['bg'] = DEFAUTL_BG
entrada_hora['bg'] = DEFAUTL_BG
dois_pontos['bg'] = DEFAUTL_BG
entrada_minutos['bg'] = DEFAUTL_BG
mensagem['bg'] = DEFAUTL_BG

relogio['text'] = strftime('%H:%M:%S')

def tictac():
	agora = strftime('%H:%M:%S')
	global acordar

	if agora == hora_de_acordar['text']+":00":
		acordar = True

	if acordar:
		#Beep(3000,200)
		mensagem['text'] = "Hora de acordar!!"
		botao_parar.pack(side = Tkinter.LEFT)
	else:
		mensagem['text'] = ""


	if agora != relogio['text']:
		relogio['text'] = agora

	relogio.after(100, tictac)

tictac()
janela.mainloop()
