#from tkinter import CASCADE
#from unicodedata import name
from django.db import models

# Create your models here.


class Task(models.Model):
	title= models.CharField(max_length=200)
	description= models.CharField(max_length=250)
	counters= models.IntegerField()


class livre(models.Model):
	fields = [
		('id', models.AutoField(auto_created=True,primary_key=True,serialize=False)),
		('titre', models.CharField(max_length=255)),
		('auteurs', models.CharField(max_length=255)),
		('secteur', models.CharField(max_length=255)),
		('description', models.TextField(max_length=300)),
		('image', models.CharField(max_length=255)),
		('fichier', models.CharField(max_length=255)),
		('etablissement', models.CharField(max_length=255)),
		('type', models.CharField(max_length=255)),
		('statut', models.BooleanField(max_length=2)),
		('created_at', models.DateTimeField()),
		('updated_at', models.DateTimeField()),
	]


class Client(models.Model):
	fields =[
		('id', models.AutoField(auto_created=True,primary_key=True,serialize=False)),
		('name', models.CharField(max_length=100)),
		('nbvisitors', models.IntegerField(max_length=255)),
		('id_art', models.ForeignKey('Product',on_delete=models.CASCADE)),
	]


