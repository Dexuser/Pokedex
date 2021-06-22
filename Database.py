import sqlite3
from tkinter import messagebox as mb

class Pokemons:

	def __init__(self):
		self.lugar = -1
		try:
			conexion = sqlite3.connect("Pokemones.db")
			cursor = conexion.cursor()
			sql = """create table pokemones (
						numero integer primary key,
						pokemon text,
						nombre text,
						altura real,
						peso real,
						tipos text,
						comida text,
						imagenPath text,
						descripcion text
					)"""
			cursor.execute(sql)
		except sqlite3.OperationalError:
			pass

	def abrir(self):
		conexion = sqlite3.connect("Pokemones.db")
		return conexion
	
	def subir(self,datos):
	
		cone = self.abrir()
		cursor = cone.cursor()
		sql = """insert into pokemones(
					numero,
					pokemon,
					nombre,
					altura,
					peso,
					tipos,
					comida,
					imagenPath,
					descripcion

				) values (?,?,?,?,?,?,?,?,?)"""
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()

	def iterar(self, direccion):
		try:
			self.lugar += direccion
			cone = self.abrir()
			cursor = cone.cursor()
			sql = "select * from pokemones"
			if self.lugar < 0:
				mb.showinfo("Informacion", "Estas en el principio de los registros de la Pokedex, intenta avanzar")
				self.lugar = 0
			cursor.execute(sql)
			informacion = cursor.fetchall()
			return informacion[self.lugar]
		except IndexError:
			mb.showinfo("Informacion", "Llegaste al final de la Pokedex, intenta atrapar mas Pokemones!")
			self.lugar -= 1
		finally:
			cone.close()