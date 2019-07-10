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
			print ('')
	
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
									<th scope="col">created_at</th>
									<th scope="col">updated_at</th>
								</tr>
							</thead>
							@foreach ($datos as $dato)
								<tbody>
									<tr>
										<th scope="row">{{$dato->id}}</th>
										<td>{{$dato->created_at}}</td>
										<td>{{$dato->updated_at}}</td>
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
			print ('')

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
			print ('')
	
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
			
pixi = Pixi('C:/laragon/www/', 'CRUD')
validar = pixi.verificarPath(pixi.rutaProyecto)
if validar == 'true':
	pixi.crearC()
	pixi.crearR()
	pixi.crearU()
	pixi.crearD()



















