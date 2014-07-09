from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class CarreraForm(ModelForm):
	nombre	= forms.CharField(label="Nombre de Carrera",widget=forms.TextInput())
	direccion	= forms.CharField(label="La Direccion",widget=forms.TextInput())
	telefono	= forms.CharField(label="El Telefono",widget=forms.TextInput())
	class Meta:
		model=Carrera
		fields=["nombre","direccion","telefono"] 


class ContactForm(ModelForm):
	class Meta:
		model=Carrera
		fields=["nombre","direccion","telefono"] 


class LoginEstudianteForm(forms.Form):
	username = forms.CharField(widget=forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class LoginDocenteForm(forms.Form):
	username = forms.CharField(widget=forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))



class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))





class RegistrarEstudiante(ModelForm):
	nombre=forms.CharField(error_messages={"required":"El nombre esta vacio"})
	apellido=forms.CharField(error_messages={"required":"El apellido esta vacio"})
	ci=forms.CharField(error_messages={"required":"El ci esta vacio"})
	email=forms.EmailField(error_messages={"required":"El email esta vacio"})

	class Meta:
		model=Estudiante
		fields=["nombre","apellido","ci","email"] 

class Registro_Estudiante(ModelForm):
	class Meta():
		model=Estudiante
		fields=["nombre","apellido","ci","email","password"]

class Registro_Docente(ModelForm):
	class Meta():
		model=Docente
		fields=["nombre","apellido","ci","email","password"]



class RegistrarDocente(ModelForm):
	nombre=forms.CharField(error_messages={"required":"El nombre esta vacio"})
	apellido=forms.CharField(error_messages={"required":"El apellido esta vacio"})
	ci=forms.CharField(error_messages={"required":"El ci esta vacio"})
	email=forms.EmailField(error_messages={"required":"El email esta vacio"})
	class Meta:
		model=Docente
		fields=["nombre","apellido","ci","email"] 

class RegistrarMateria(forms.ModelForm):
	class Meta():
		model=Materia
		fields=["nombre","sigla","nivel","descripcion","notamin","notamax","notamindeaprovacion"] 


class RegistrarNotas(forms.ModelForm):
	class Meta():
		model=Notas
		fields=["poderacionparcial","poderacionpracticas","poderacionlaboratorio","poderacionexamenfinal","primerparcial","segundoparcial","tercerparcial","practicas","laboratorio","examenfinal","notafinal","id_Mat"]


class RegistrarRelCarMat(forms.ModelForm):
	class Meta():
		model=rel_car_mat
		fields=["id_Car","id_Mat"]


class RegistrarRelEstCar(forms.ModelForm):
	class Meta():
		model=rel_estudiante_carrera
		fields=["idCarrera"]

class RegistrarRelEstMat(forms.ModelForm):
	class Meta():
		model=rel_estudiante_materia
		fields=["idEstudiante","idMateria"]


class AutorForm(ModelForm):
	class Meta:
		model=Autor
		fields=["nombre","apellido_pat","apellido_mat"] 

class DocumentForm(ModelForm):
	class Meta:
		model=Document
		fields=["nombre","imagen","docfile","autor"] 


class RegistrarRelCarDoc(forms.ModelForm):
	class Meta():
		model=rel_docente_carrera
		fields=["idCarrera","idDocente"]
class RegistrarRelDocMat(forms.ModelForm):
	class Meta():
		model=rel_docente_materia
		fields=["idDocente","idMateria"]