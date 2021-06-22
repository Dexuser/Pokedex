from os import name
import tkinter as tk
from tkinter import ttk	
from tkinter import font


class Styles:

	def __init__(self):
		# Fuentes
		self.fuente_titulo = font.Font(size=50, name="titular")
		self.fuente_datos = font.Font(size=13, name="datos")
		self.fuente_subtitulo = font.Font(size=25, name="subtitulo")

		
		self.titulo = ttk.Style()
		self.titulo.configure("Titulo.TLabel", foreground="red")
		self.datos = ttk.Style()
		self.datos.configure("Datos.TLabel", foreground="Blue")