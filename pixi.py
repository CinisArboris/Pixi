import os

class Pixi:
	nombreVista = ''
	rutaProyecto = ''
	nombreProyecto = ''

	def __init__(self, rutaProyecto, nombreProyecto):
		self.nombreVista = input('Dame el nombre de tu vista: ')
		self.nombreVista = self.nombreVista.split(" ")
		self.nombreProyecto = nombreProyecto
		self.rutaProyecto = rutaProyecto + self.nombreProyecto + '/resources/views/'
		
	def verificarPath(self, rutaProyecto):
		if os.path.isdir(rutaProyecto):
			print ('>>> Es directorio')
			return 'true'
		else:
			print('No es un directorio')
			return 'false'
	
	def crearCRUD(self):
		print ('crear leer actualizar eliminar')
		for item in self.nombreVista:
			#crear carpeta
			if os.path.isdir(self.rutaProyecto + item):
				print('')
			else:
				os.mkdir(self.rutaProyecto + item)
			print (item)
			#Crear archivo [create]
			file = open(self.rutaProyecto+item+"/"+
						'crear' + item +
						".blade.php", "w")
			file.write ("""
@extends('layouts.app')
@section('content')
<div class="container">
	<div class="row justify-content-center">
		<div class="col-md-8">
			<div class="card">
				<div class="card-header">""" + item + """</div>

				<div class="card-body">
					
				</div>
			</div>
		</div>
	</div>
</div>
@endsection
			""")
			file.close()
			print ('Listo :)' + ' crear' + item)
			
			#Crear archivo [leer]
			file = open(self.rutaProyecto+item+"/"+
						'leer' + item +
						".blade.php", "w")
			file.write ("""
@extends('layouts.app')
@section('content')
<div class="container">
	<div class="row justify-content-center">
		<div class="col-md-8">
			<div class="card">
				<div class="card-header">""" + item + """</div>

				<div class="card-body">
					
				</div>
			</div>
		</div>
	</div>
</div>
@endsection
			""")
			file.close()
			print ('Listo :)' + ' leer' + item)
			
			#Crear archivo [actualizar]
			file = open(self.rutaProyecto+item+"/"+
						'actualizar' + item +
						".blade.php", "w")
			file.write ("""
@extends('layouts.app')
@section('content')
<div class="container">
	<div class="row justify-content-center">
		<div class="col-md-8">
			<div class="card">
				<div class="card-header">""" + item + """</div>

				<div class="card-body">
					
				</div>
			</div>
		</div>
	</div>
</div>
@endsection
			""")
			file.close()
			print ('Listo :)' + ' actualizar' + item)
			
			#Crear archivo [eliminar]
			file = open(self.rutaProyecto+item+"/"+
						'eliminar' + item +
						".blade.php", "w")
			file.write ("""
@extends('layouts.app')
@section('content')
<div class="container">
	<div class="row justify-content-center">
		<div class="col-md-8">
			<div class="card">
				<div class="card-header">""" + item + """</div>

				<div class="card-body">
					
				</div>
			</div>
		</div>
	</div>
</div>
@endsection
			""")
			file.close()
			print ('Listo :)' + ' eliminar' + item)
			
			
			print ('')

pixi = Pixi('C:/laragon/www/', 'CRUD')
validar = pixi.verificarPath(pixi.rutaProyecto)
if validar == 'true':
	pixi.crearCRUD()



















