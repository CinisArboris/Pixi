import os

class Pixi:
	nombreVista = ''
	rutaProyecto = ''
	nombreProyecto = ''

	def __init__(self, rutaProyecto, nombreProyecto):
		print ("""
  ██████  ▄████▄  ▓█████  ██▀███   ██▓  ██████ 
▒██    ▒ ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒▓██▒▒██    ▒ 
░ ▓██▄   ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒▒██▒░ ▓██▄   
  ▒   ██▒▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  ░██░  ▒   ██▒
▒██████▒▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒░██░▒██████▒▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░
░  ░  ░  ░           ░     ░░   ░  ▒ ░░  ░  ░  
      ░  ░ ░         ░  ░   ░      ░        ░  
         ░
Vargas Medina Eyver Emilio / CinisArboris		 
		""")
		self.nombreVista = input('Dame el nombre de tu vista: ')
		self.nombreVista = self.nombreVista.split(" ")
		self.nombreProyecto = nombreProyecto
		self.rutaProyecto = rutaProyecto + self.nombreProyecto + '/resources/views/'
		
	def verificarPath(self, rutaProyecto):
		if os.path.isdir(rutaProyecto):
			return 'true'
		else:
			return 'false'
	
	def crearC(self):
		for item in self.nombreVista:
			#crear carpeta
			if os.path.isdir(self.rutaProyecto + item):
				print('')
			else:
				os.mkdir(self.rutaProyecto + item)
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
	
	def crearR(self):
		print ('leer')
		for item in self.nombreVista:
			#crear carpeta
			if os.path.isdir(self.rutaProyecto + item):
				print('')
			else:
				os.mkdir(self.rutaProyecto + item)
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
					<table class="table table-hover table-dark">
						@if(count($datos) == 0)
						<h1>Sin datos para mostrar...</h1>
						@else
							<thead>
								<tr>
									<th scope="col">#</th>
									<th scope="col">nombre</th>
									<th scope="col">descripcion</th>
								</tr>
							</thead>
							@foreach ($datos as $dato)
								<tbody>
									<tr>
										<th scope="row">{{$dato->id}}</th>
										<td>{{$dato->nombre}}</td>
										<td>{{$dato->descripcion}}</td>
									</tr>
								</tbody>
							@endforeach
						@endif
					</table>
				</div>
			</div>
		</div>
	</div>
</div>
@endsection
			""")
			file.close()
			print ('Listo :)' + ' crear' + item)

	def crearU(self):
		print ('actualizar')
		for item in self.nombreVista:
			#crear carpeta
			if os.path.isdir(self.rutaProyecto + item):
				print('')
			else:
				os.mkdir(self.rutaProyecto + item)
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
			print ('Listo :)' + ' crear' + item)
	
	def crearD(self):
		print ('eliminar')
		for item in self.nombreVista:
			#crear carpeta
			if os.path.isdir(self.rutaProyecto + item):
				print('')
			else:
				os.mkdir(self.rutaProyecto + item)
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
			print ('Listo :)' + ' crear' + item)
	
	def rutas(self):
		for item in self.nombreVista:
			rutas = open('C:/laragon/www/CRUD/routes/web.php', 'a+')
			rutas.write("// // \n")
			rutas.write("Route::get('/"+ item + "/leer"+ item + "', '"+ item + "Controller@index')->name('leer"+ item + "'); \n")
			rutas.write("Route::get('/"+ item + "/crear"+ item + "', '"+ item + "Controller@create')->name('crear"+ item + "'); \n")
			rutas.write("Route::post('/"+ item + "/guardar"+ item + "', '"+ item + "Controller@store')->name('guardar"+ item + "'); \n")
			rutas.write("Route::get('/"+ item + "/mostrar"+ item + "/{id}', '"+ item + "Controller@show')->name('mostrar"+ item + "'); \n")
			rutas.write("Route::get('/"+ item + "/editar"+ item + "/{id}', '"+ item + "Controller@edit')->name('editar"+ item + "'); \n")
			rutas.write("Route::put('/"+ item + "/actualizar"+ item + "/{id}', '"+ item + "Controller@update')->name('actualizar"+ item + "'); \n")
			rutas.write("Route::delete('/"+ item + "/destruir"+ item + "/{id}', '"+ item + "Controller@destroy')->name('destruir"+ item + "'); \n")
			rutas.close()
			print (item)

pixi = Pixi('C:/laragon/www/', 'CRUD')
validar = pixi.verificarPath(pixi.rutaProyecto)
if validar == 'true':
	pixi.crearC()
	pixi.crearR()
	pixi.crearU()
	pixi.crearD()
	pixi.rutas()


















