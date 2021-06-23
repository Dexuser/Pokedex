import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from os import mkdir, remove
import Pokedex_styles
import Formulario
import Database


class Pokedex:
	# por favor, mete los scripts en una carpeta para que funcionen
	# debido a que fueron creados con la intencion de que esten en una carpeta
	# Arriba se importan los modulos Pokedex_Styles donde se declaran los estilos que usaran
	# los widgets que mas tarde seran incializados, Formulario con este modulo se crea un objeto
	# que nos permitira hacer un toplevel con las herramientas necesarias para poder introducir informacion	
	# ala base de datos, y el modulo Database, con el creamos un objeto que nos permite interactuar con una base
	# de datos SQLite

	# Se creara una carpeta para contener las imagenes
	# aparte se crean la ventana, y se crean los Objetos para interactuar
	# con la base de datos y el formulario
	def __init__(self):
		try:
			mkdir("imagenes")
		except OSError:
			pass

		self.root = tk.Tk()
		self.root.geometry("1400x650")
		self.root.title("Pokedex, Version beta 2")
		self.root.iconbitmap("imagenes/Pokeball.ico")
		self.styles = Pokedex_styles.Styles()
		self.database = Database.Pokemons()
		self.tope()
		self.cuerpo()
		self.root.bind_all("<Control-n>", self.atajos)
		self.root.bind_all("<Control-d>", self.atajos)
		self.root.mainloop()
	
	#Los botones son los principales detonantes de acciones en la pokedex
	# Estos muestran los pokemones contenidos y permiten agregar, modificar
	# y eliminar pokemones
	def tope(self):
		self.titulo = ttk.Label(
			self.root,
			text="Pokedex", 
			style="Titulo.TLabel",
			font="titular"
			)
		self.titulo.grid(column=0, row=0, padx=50, pady=5)


		self.retroceder = ttk.Button(
			self.root, 
			text="Retroceder", 
			command=lambda: self.moverse(-1)
		)
		self.retroceder.grid(column=1, row=0, padx=5, pady=5, sticky="ens")

		self.avanzar = ttk.Button(
			self.root, 
			text="Avanzar", 
			command=lambda: self.moverse(1)
		)
		self.avanzar.grid(column=2, row=0, padx=5, pady=5, sticky="ens")

		self.agregar_modificar = ttk.Button(
			self.root, 
			text="Agregar/Modificar\n pokemones\n atajo: Control N",
			command= self.encuesta,
			)
		self.agregar_modificar.grid(column=3, row=0, padx=5, pady=5, sticky="ens")
		
		self.eliminar = ttk.Button(
			self.root, 
			text="Eliminar Pokemon\n atajo: Control D", 
			command=self.borrar
			)
		self.eliminar.grid(column=4, row=0, padx=4, pady=5, sticky="ens" )

		barra= ttk.Separator(orient=tk.HORIZONTAL)
		barra.grid(column=0, row=1,columnspan=4, sticky="we")



	# el cuerpo consiste en la interfaz grafica para poder visualizar la informacion
	# contenida en la base de datos de nuestros pokemones, el flujo de informacion aqui consiste
	# en llamar ala funcion moverse y lo que retorne introducirlas en cada una de los stringsvar de 
	# forma ordenada, aparte se crea un canvas para poder visualizar las imagenes de los pokemones
	def cuerpo(self):
		self.imagen = tk.Canvas(self.root, width=500, height=500, background="black")
		self.archivo = tk.PhotoImage(file="imagenes/default.png")
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
	

	# la funcion encuesta es llamada por el boton de Agregar/modificar
	# pokemones, se crea un toplevel para la entrada y modificacion de datos
	def encuesta(self):
		self.toplevel = Formulario.Encuesta(self.root)


	# La funcion moverse es llamada por los botones retroceder y avanzar.
	# esta recibe un parametro llamado direccion que recibe 2 numeors,
	# el 1 le indica que debe avanzar ala siguiente fila de la base de datos
	# y con el -1 debe de retroceder ala fila pasada, se utiliza el objeto database
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
	
	# La funcion borrar recupera el numero numero del pokemon que se esta
	# visualizando actualmente en la pokedexGUI y se le envia al objeto
	# database para ejecutar un metodo que elimina toda la informacion relacionada
	# a ese numero.
	def borrar(self):
		if self.numero.get() != "":
			respuesta = self.database.borrar(self.numero.get())
			if respuesta > 0:
				mb.showinfo("informacion", "Los datos del Pokemon fueron borrados!")
				self.numero.set("")
				self.pokemon.set("")
				self.nombre.set("")
				self.altura.set("")
				self.peso.set("")
				self.tipos.set("")
				self.comida.set("")
				self.texto.delete(1.0, tk.END)
				remove(self.archivo.cget("file"))
				self.archivo.configure(file="imagenes/default.png")
		else:
			mb.showerror("Error!", "No hay nada que borrar")
	
	def atajos(self, event):
		if event.keysym=="n":
			self.encuesta()
		if event.keysym=="d":
			self.borrar()
aplicacion = Pokedex()