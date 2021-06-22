import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from os import mkdir
from tkinter.constants import ANCHOR
import Pokedex_styles
import Formulario
import Database


class Pokedex:

	def __init__(self):
		try:
			mkdir("imagenes")
		except OSError:
			pass

		self.root = tk.Tk()
		self.root.geometry("1130x650")
		self.root.title("Pokedex, Version beta 1")
		self.styles = Pokedex_styles.Styles()
		self.database = Database.Pokemons()
		self.tope()
		self.cuerpo()
		self.root.mainloop()
	
	def tope(self):
		self.titulo = ttk.Label(
			self.root,
			text="Pokedex", 
			style="Titulo.TLabel",
			font="titular"
			)
		self.titulo.grid(column=0, row=0, padx=50, pady=5)

		# Agregar el Command
		self.retroceder = ttk.Button(
			self.root, 
			text="Retroceder", 
			width=15,
			command=lambda: self.moverse(-1)
		)
		self.retroceder.grid(column=1, row=0, padx=5, pady=5, sticky="ens")

		self.avanzar = ttk.Button(
			self.root, 
			text="Avanzar", 
			width=15,
			command=lambda: self.moverse(1)
		)
		self.avanzar.grid(column=2, row=0, padx=5, pady=5, sticky="ens")

		self.agregar = ttk.Button(
			self.root, 
			text="Agregar pokemon",
			command= self.encuesta
			)
		self.agregar.grid(
			column=3, row=0, 
			padx=5, pady=5, 
			sticky="ens",
			)
		barra= ttk.Separator(orient=tk.HORIZONTAL)
		barra.grid(column=0, row=1,columnspan=4, sticky="we")


	def cuerpo(self):
		self.imagen = tk.Canvas(self.root, width=300, height=500, background="black")
		self.archivo = tk.PhotoImage()
		self.imagen.create_image(0, 0, image=self.archivo, anchor="nw")
		self.imagen.grid(column=0, row=2, padx=5, pady=5)

		#datos
		self.informacion = ttk.Labelframe(self.root, text="Informacion")
		self.informacion.grid(column=1, row=2, padx=5, pady=5, sticky="wn")
		
		self.label2 = ttk.Label(
			self.informacion,
			text="Numero:", 
			style="Datos.TLabel",
			font="datos"
			)
		self.label2.grid(column=1, row=0, padx=5, pady=5, sticky="n")
		self.numero = tk.StringVar()
		self.numero_entry= ttk.Entry(
			self.informacion,
			state="readonly",
			textvariable=self.numero
			)
		self.numero_entry.grid(column=2, row=0, padx=5, pady=5, sticky="n")

		self.label3 = ttk.Label(
			self.informacion,
			text="Pokemon:",
			style="Datos.TLabel",
			font="datos"
			)	
		self.label3.grid(column=1, row=1, padx=5, pady=5, sticky="n")
		self.pokemon = tk.StringVar()
		self.pokemon_entry = ttk.Entry(
			self.informacion,
			state="readonly",
			textvariable=self.pokemon
			)
		self.pokemon_entry.grid(column=2, row=1, padx=5, pady=5, sticky="n")

		self.label4 = ttk.Label(
			self.informacion,
			text="Nombre:",
			style="Datos.TLabel",
			font="datos"
			)
		self.label4.grid(column=1, row=2, padx=5, pady=5, sticky="n")
		self.nombre = tk.StringVar()
		self.nombre_entry = ttk.Entry(
			self.informacion,
			state="readonly",
			textvariable=self.nombre)
		self.nombre_entry.grid(column=2, row=2, padx=5, pady=5, sticky="n")

		self.label5 = ttk.Label(
			self.informacion,
			text="Altura",
			style="Datos.TLabel",
			font="datos"
			)
		self.label5.grid(column=3, row=0, padx=5, pady=5, sticky="n")
		self.altura = tk.StringVar()
		self.altura_entry = ttk.Entry(
			self.informacion, 
			state="readonly", 
			textvariable=self.altura
			)
		self.altura_entry.grid(column=4, row=0, padx=5, pady=4, sticky="n")

		self.label6 = ttk.Label(
			self.informacion,
			text="Peso",
			style="Datos.TLabel",
			font="datos"
			)
		self.label6.grid(column=3, row=1, padx=5, pady=5, sticky="n")
		self.peso = tk.StringVar()
		self.peso_entry = ttk.Entry(
			self.informacion, 
			state="readonly", 
			textvariable=self.peso
			)
		self.peso_entry.grid(column=4, row=1, padx=5, pady=5, sticky="n")

		self.label7 = ttk.Label(
			self.informacion, 
			text="Tipo/Subtipo:",
			style="Datos.TLabel",
			font="datos"
			)
		self.label7.grid(column=3, row=2, padx=5, pady=5, sticky="n")
		self.tipos = tk.StringVar()
		self.tipos_entry = ttk.Entry(
			self.informacion,
			state="readonly",
			textvariable=self.tipos
			)
		self.tipos_entry.grid(column=4, row=2, padx=5, pady=5, sticky="n")

		self.label8 = ttk.Label(
			self.informacion, 
			text="Comida favorita",
			style="Datos.TLabel",
			font="datos"
			)
		self.label8.grid(column=2, row=3, padx=5, pady=5, sticky="ne")
		self.comida = tk.StringVar()
		self.comida.entry = ttk.Entry(
			self.informacion,
			state="readonly",
			textvariable=self.comida
			)
		self.comida.entry.grid(column=3, row=3, padx=5, pady=5, sticky="nw")
	
		self.labelframe = ttk.LabelFrame(self.informacion, text="Decripcion")
		self.labelframe.grid(
			column=1, row=4,
			padx=5, pady=20,
			columnspan=4, sticky="n"
			)
		self.texto = st.ScrolledText(self.labelframe, width=60, height=6)
		self.texto.grid(column=0, row=0, padx=5, pady=5, sticky="we")
	
	def encuesta(self):
		self.toplevel = Formulario.Encuesta(self.root)

	def moverse(self, direccion):
		respuesta = self.database.iterar(direccion)
		if respuesta != None:
			self.numero.set(respuesta[0])
			self.pokemon.set(respuesta[1])
			self.nombre.set(respuesta[2])
			self.altura.set(respuesta[3])
			self.peso.set(respuesta[4])
			self.tipos.set(respuesta[5])
			self.comida.set(respuesta[6])
			self.archivo.configure(file=respuesta[7])
			self.texto.delete(1.0, tk.END)
			self.texto.insert(tk.END, respuesta[8])

aplicacion = Pokedex()