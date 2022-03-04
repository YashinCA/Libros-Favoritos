from django.db import models

from acceso.models import Usuario


# class Usuario(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     username = models.CharField(
#         max_length=20, unique=True, verbose_name="Nombre de Usuario")
#     email = models.EmailField(max_length=200, unique=True)
#     password = models.CharField(max_length=72)
#     description = models.TextField(default='')
#     # birthday = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# liked_books = a una lista de libros que le gustan a un usuario determinado
# books_uploaded = una lista de libros cargados por un usuario determinado

#     class Meta:
#         verbose_name = "Usuario"
#         verbose_name_plural = "Usuarios"

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    uploaded_by = models.ForeignKey(
        Usuario, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(
        Usuario, related_name="liked_books")
    # a list of users who like a given book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
