import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
import os
from shutil import copy
from PIL import Image
import Database

class Encuesta:

	# Importamos y creamos un objeto de la database par apoder interactuar con ella
	# tanto el tope viene siendo la presentacion y la explicacion de como usar la interfaz
	# de entradas de datos, el cuerpo, imagenes, y opciones son funciones cuyo unico proposito
	# es construir la interfaz grafica para la entrada de datos
	def __init__(self, root):
		self.dialogo = tk.Toplevel(root)
		self.database = Database.Pokemons()
		self.presentacion()
		self.cuerpo()
		self.recuperar_imagen()
		self.opciones()
		self.dialogo.bind_all("<Control-e>", self.atajos)
		self.dialogo.bind("<Control-g>", self.atajos)
		self.dialogo.grab_set()

	def presentacion(self):
		self.titulo = ttk.Label(
			self.dialogo,
			text="Poke-Formulario",
			style="Titulo.TLabel",
			font="subtitulo"
		)
		self.titulo.grid(column=0, row=0, padx=5, pady=5)


		parrafo = "Introduzca los datos e imagen del pokemon (la imagen sera movida a una capeta de la Pokedex) en\n\
cambio si va a modificar la informacion de algun pokemon, primero introduzca el numero del pokemon \n\
y luego introduzca los nuevos datos que quiere que posea el pokemon."

		self.parrafo = ttk.Label(
			self.dialogo,
			text=parrafo,
			font="datos"
		)
		self.parrafo.grid(column=0, row=1, padx=5, pady=5)


	def cuerpo(self):
		self.informacion = ttk.Labelframe(self.dialogo, text="Informacion")
		self.informacion.grid(column=0, row=2, padx=5, pady=10, sticky="wn")
		
		self.label2 = ttk.Label(
			self.informacion,
			text="Numero:", 
			style="Datos.TLabel",
			font="datos"
			)
		self.label2.grid(column=0, row=0, padx=5, pady=5, sticky="n")
		self.numero = tk.StringVar()
		self.numero_entry= ttk.Entry(
			self.informacion,
			textvariable=self.numero
			)
		self.numero_entry.grid(column=1, row=0, padx=5, pady=5, sticky="n")

		self.label3 = ttk.Label(
			self.informacion,
			text="Pokemon:",
			style="Datos.TLabel",
			font="datos"
			)	
		self.label3.grid(column=0, row=1, padx=5, pady=5, sticky="n")
		self.pokemon = tk.StringVar()
		self.pokemon_entry = ttk.Entry(
			self.informacion,
			textvariable=self.pokemon
			)
		self.pokemon_entry.grid(column=1, row=1, padx=5, pady=5, sticky="n")

		self.label4 = ttk.Label(
			self.informacion,
			text="Nombre:",
			style="Datos.TLabel",
			font="datos"
			)
		self.label4.grid(column=0, row=2, padx=5, pady=5, sticky="n")
		self.nombre = tk.StringVar()
		self.nombre_entry = ttk.Entry(
			self.informacion,
			textvariable=self.nombre)
		self.nombre_entry.grid(column=1, row=2, padx=5, pady=5, sticky="n")

		self.label5 = ttk.Label(
			self.informacion,
			text="Altura",
			style="Datos.TLabel",
			font="datos"
			)
		self.label5.grid(column=2, row=0, padx=5, pady=5, sticky="n")
		self.altura = tk.StringVar()
		self.altura_entry = ttk.Entry(
			self.informacion, 
			textvariable=self.altura
			)
		self.altura_entry.grid(column=3, row=0, padx=5, pady=4, sticky="n")

		self.label6 = ttk.Label(
			self.informacion,
			text="Peso",
			style="Datos.TLabel",
			font="datos"
			)
		self.label6.grid(column=2, row=1, padx=5, pady=5, sticky="n")
		self.peso = tk.StringVar()
		self.peso_entry = ttk.Entry(
			self.informacion, 
			textvariable=self.peso
			)
		self.peso_entry.grid(column=3, row=1, padx=5, pady=5, sticky="n")

		self.label7 = ttk.Label(
			self.informacion, 
			text="Tipo/Subtipo:",
			style="Datos.TLabel",
			font="datos"
			)
		self.label7.grid(column=2, row=2, padx=5, pady=5, sticky="n")
		self.tipos = tk.StringVar()
		self.tipos_entry = ttk.Entry(
			self.informacion,
			textvariable=self.tipos
			)
		self.tipos_entry.grid(column=3, row=2, padx=5, pady=5, sticky="n")

		self.label8 = ttk.Label(
			self.informacion, 
			text="Comida favorita",
			style="Datos.TLabel",
			font="datos"
			)
		self.label8.grid(column=1, row=3, padx=5, pady=5, sticky="ne")
		self.comida = tk.StringVar()
		self.comida.entry = ttk.Entry(
			self.informacion,
			textvariable=self.comida
			)
		self.comida.entry.grid(column=2, row=3, padx=5, pady=5, sticky="nw")

		self.labelframe = ttk.LabelFrame(self.informacion, text="Decripcion")
		self.labelframe.grid(
			column=0, row=4,
			padx=5, pady=20,
			columnspan=4, sticky="n"
			)
		self.texto = st.ScrolledText(self.labelframe, width=60, height=6)
		self.texto.grid(column=0, row=0, padx=5, pady=5, sticky="we")
	

	def recuperar_imagen(self):
		self.labelframe = ttk.Labelframe(self.dialogo, text="Imagen")
		self.labelframe.grid(column=0, row=4, padx=5, pady=5, sticky="w")
		self.label = ttk.Label(self.labelframe, text="Archivo:")
		self.label.grid(column=0, row=0, padx=5, pady=5, sticky="W")
		self.ruta = tk.StringVar()
		self.entry = ttk.Entry(self.labelframe, width=50, textvariable=self.ruta)
		self.entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")
		self.btn_dialogo = ttk.Button(
			self.labelframe, 
			text="buscar", 
			command=self.buscar_mover
			)
		self.btn_dialogo.grid(column=2, row=0, padx=5, pady=5)


	def atajos(self, event):
		if event.keysym=="e":
			self.modificar()
		if event.keysym=="g":
			self.guardar()


	# hacer una copia de la imagen selecciona y introducirla en la carpeta imagenes, luego crea una
	# ruta relativa (desde el modulo Formulario hasta la carpeta imagenes hasta la imagen ejemp: imagenes/archivo.png)
	# si la imagen seleccionada no es del tipo PNG esta se convertira a ese formato para que tkinter pueda mostrarla
	# la imagen se redimencionara a 500 x 500 sea o no sea PNG
	def buscar_mover(self):
		nombrearch=fd.askopenfilename(
			initialdir = "/", 
			title = "Seleccione archivo",
			filetypes = (("archivos png", "*.png"), ("archivos jpg", "*.jpg"),("todos los archivos","*.*"))
			)
		if nombrearch != "":
			size = (500, 500)
			ruta = "imagenes/" + os.path.basename(nombrearch)
			img = Image.open(nombrearch)
			img2 = img.resize(size)
			nombre, ext = os.path.splitext(ruta)

			if img.format != "PNG":
				copy(nombrearch, "imagenes/")
				img2.save(nombre + ".png", "png")
				os.remove(ruta)
				self.ruta.set(nombre +".png")

			else:
				copy(nombrearch, "imagenes/")
				img2.save(nombre +"RSZ.png", "png")
				os.remove(ruta)
				self.ruta.set(nombre +"RSZ.png")


	def opciones(self):
		self.boton = ttk.Button(self.dialogo, text="Guardar", command=self.guardar)
		self.boton.grid(column=0, row=5, padx=5, pady=5)
		self.btn_modificar = ttk.Button(self.dialogo, text="Modificar", command=self.modificar)
		self.btn_modificar.grid(column=0, row=6, padx=5, pady=5)


	# Luego de que todas las entradas de datos estan llenas se proceden a guardar la informacion
	# en la base de datos utiliziando un metodo del objeto data base anteriormente creado.
	# Nota, la base de datos no guarda la imagen, sino que guarda la ruta relativa de esta
	def guardar(self):
		datos = (
			self.numero.get(),
			self.pokemon.get(),
			self.nombre.get(),
			self.altura.get(),
			self.peso.get(),
			self.tipos.get(),
			self.comida.get(),
			self.ruta.get(),
			self.texto.get(1.0, tk.END)
			)
		respuesta = self.database.subir(datos)
		if respuesta != None:
			mb.showinfo("Informacion", "Los datos del pokemon fueron guardados!")
			self.numero.set("")
			self.pokemon.set("")
			self.nombre.set("")
			self.altura.set("")
			self.peso.set("")
			self.tipos.set("")
			self.comida.set("")
			self.ruta.set("")
			self.texto.delete(1.0, tk.END)

	# en modificar, se crea una tupla de datos, pero esta es ordenada de manera que 
	# cuando esta llegue ala base de datos se pueda identificar la informacion del pokemon
	# se va a modificar usando su numero de identificacion
	def modificar(self):
		datos = (
		self.pokemon.get(),
		self.nombre.get(),
		self.altura.get(),
		self.peso.get(),
		self.tipos.get(),
		self.comida.get(),
		self.ruta.get(),
		self.texto.get(1.0, tk.END),
		self.numero.get()
		)
		respuesta = self.database.editar(datos)
		if respuesta > 0:
			mb.showinfo("Informacion", "Los datos del Pokemon fueron actualizados!")
		else:
			mb.showerror("Error!", "No existe ningun pokemon con ese numero")
