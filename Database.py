import sqlite3
from tkinter import messagebox as mb

class Pokemons:

	# Aqui es donde se administra toda la informacion en la base de datos
	# usando estos metodos.
	# se crea un atributo llamado lugar para poder interar en 
	# las filas de la base de datos, mas abajo se va a explicar en detalles.
	# En caso de que la base de datos no exista se va a crear junto a su tabla.
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
	
	# Abre la conexion con la base de datos
	def abrir(self):
		conexion = sqlite3.connect("Pokemones.db")
		return conexion
	
	# Aqui es donde se administra la informacion mandada por el metodo
	# guardar de modulo Formulario, esta es insertada ala base de datos apenas
	# es recibida.
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

	# Iterar es un metodo llamado por el metodo guardar del modulo
	# PokedexGUI, ambos metodos reciben un parametro llamado direccion, 
	# el proposito de este parametro es el de ser sumado al atributo lugar,
	# este atributo tiene como proposito ser un idicie ala hora de iterar en
	# las filas de la base de datos, debido a que este metodo se construyo de manera
	# de que toda la informacion de la base de datos sea recibida en forma de lista,
	# siendo asi el atributo lugar en indice de ella que indicia que fila retornar ala 
	# PokedexGUI para que esta mustre su inforamcion, al summar 1 al atriubuto lugar
	# se avanza en las filas de la base de datos y viceversa cuando se suma -1
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

	def editar(self, datos):
		try:
			cone = self.abrir()
			cursor = cone.cursor()
			sql = """update pokemones set
			pokemon=?, 
			nombre=?,
			altura=?,
			peso=?,
			tipos=?,
			comida=?,
			imagenPath=?,
			descripcion=? where numero=? """
			cursor.execute(sql, datos)
			return cursor.rowcount
		finally:
			cone.commit()
			cone.close()
	
	def borrar(self, dato):
		try:
			cone = self.abrir()
			cursor = cone.cursor()
			sql = "delete from pokemones where numero=?"
			cursor.execute(sql, dato)
			return cursor.rowcount
		finally:
			cone.commit()
			cone.close()
			