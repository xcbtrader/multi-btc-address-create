__author__ = 'deunido'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bitcoin import *
from tkinter import *
from tkinter import ttk, font
import sys
import requests
import json

class Aplicacion():
	def __init__(self):
		
		self.raiz = Tk()
		self.raiz.geometry("700x305")
         		
		self.raiz.resizable(width=False, height=False)
		self.raiz.title("Multi Create Addr Win 1.0")
		self.fuente = font.Font(weight='bold', size=11)
		
		self.etqText = ttk.Label(self.raiz, text= 'TEXTO PARA CREAR ADDR', font=self.fuente)
		self.etqAddr = ttk.Label(self.raiz, text= 'DIRECCION BTC', font=self.fuente)
		self.etqPriv = ttk.Label(self.raiz, text= 'PRIVADA',font=self.fuente)
		self.etqWif = ttk.Label(self.raiz, text= 'WIF PARA IMPORTAR',font=self.fuente)
		self.etqSaldo = ttk.Label(self.raiz, text= 'SALDO-TOT.RECIB.',font=self.fuente)
		self.etqLin = ttk.Label(self.raiz, text= '--------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

		self.msgText = StringVar()
		self.msgText.set('')
		self.msgAddr = StringVar()
		self.msgAddr.set('')
		self.msgPriv = StringVar()
		self.msgPriv.set('')
		self.msgWif = StringVar()
		self.msgWif.set('')
		self.msgSaldo = DoubleVar()
		self.msgSaldo.set(0.0)
		self.msgTotRec = DoubleVar()
		self.msgTotRec.set(0.0)
		
		self.tText = ttk.Entry(self.raiz,textvariable=self.msgText,justify= 'center',width=67,font=self.fuente)
		self.tAddr = ttk.Entry(self.raiz,textvariable=self.msgAddr,justify= 'center',width=50,font=self.fuente)
		self.tPriv = ttk.Entry(self.raiz,textvariable=self.msgPriv,justify= 'center',width=67,font=self.fuente)
		self.tWif = ttk.Entry(self.raiz,textvariable=self.msgWif,justify= 'center',width=67,font=self.fuente)
		self.tSaldo = ttk.Label(self.raiz,textvariable=str(self.msgSaldo),justify= 'center',font=self.fuente)
		self.tTotRec = ttk.Label(self.raiz,textvariable=str(self.msgTotRec),justify= 'center',font=self.fuente)

		self.BotAddrText = ttk.Button(self.raiz, text="ADDR <-> TEXT", padding=(5,5), command=self.crear_addr_text)		
		self.BotAddrAleat = ttk.Button(self.raiz, text="ADDR <-> ALEAT", padding=(5,5), command=self.crear_addr_aleat)
		self.BotAddrSaldo = ttk.Button(self.raiz, text="SALDO", padding=(5,5), command=self.b1)
		self.BotAddrGuardar = ttk.Button(self.raiz, text="GUARDAR", padding=(5,5), command=self.guardar)
		self.BotInicializar = ttk.Button(self.raiz, text="INICIALIZAR", padding=(5,5), command=self.inicializar)
		self.BotSalir = ttk.Button(self.raiz, text="SALIR", padding=(5,5), command=quit)
		
		self.etqText.place(x=220, y=10)
		self.tText.place(x=10, y=30)
		self.etqAddr.place(x=180, y=65)
		self.tAddr.place(x=10, y=85)
		self.etqSaldo.place(x=530, y=65)
		self.tSaldo.place(x=540, y=85)
		self.tTotRec.place(x=540, y=105)
		self.etqPriv.place(x=300, y=125)
		self.tPriv.place(x=10, y=145)
		self.etqWif.place(x=260, y=185)
		self.tWif.place(x=10, y=205)
		self.etqLin.place(x=10, y=240)
		
		self.BotAddrText.place(x=20, y=260)
		self.BotAddrAleat.place(x=150, y=260)
		self.BotAddrSaldo.place(x=285, y=260)
		self.BotAddrGuardar.place(x=388, y=260)
		self.BotInicializar.place(x=492, y=260)
		self.BotSalir.place(x=595, y=260)
		
		self.raiz.mainloop()

	def crear_addr_aleat(self):
		priv = random_key()
		pub = privtopub(priv)
		addr = pubtoaddr(pub)
		wif = encode_privkey(priv, 'wif')
		self.msgAddr.set(addr)
		self.msgPriv.set(priv)
		self.msgWif.set(wif)
	
	def crear_addr_text(self):
		priv = sha256(self.msgText.get())
		pub = privtopub(priv)
		addr = pubtoaddr(pub)
		wif = encode_privkey(priv, 'wif')
		self.msgAddr.set(addr)
		self.msgPriv.set(priv)
		self.msgWif.set(wif)

	def guardar(self):
		if self.msgAddr.get() != '':
			f = open(self.msgAddr.get() + '.dat', 'w')
			f.write('WIF: ' + self.msgWif.get() + '\n')
			f.write('PRIV: ' + self.msgPriv.get() + '\n')
			f.write('ADDR: ' + self.msgAddr.get() + '\n')
			f.write('SALDO: ' + str(self.msgSaldo.get()))
			f.close()
			

	def b1(self):
		try:
			request = 'http://btc.blockr.io/api/v1/address/info/' + self.msgAddr.get()
			response = requests.get(request, timeout=10)
			content = response.json()
			content1 = content['data'] ['balance']
			content2 = content['data'] ['totalreceived']
			self.msgSaldo.set(content1)
			self.msgTotRec.set(content2)
		except KeyboardInterrupt:
			exit()
		except Exception:
			self.msgSaldo.set(-1)
			self.msgTotRec.set(-1)
		
	def inicializar(self):
		self.msgText.set('')
		self.msgAddr.set('')
		self.msgPriv.set('')
		self.msgWif.set('')
		self.msgSaldo.set(0.0)		
	
def main():
	
	mi_app = Aplicacion()
	return 0

if __name__ == '__main__':
    main()
