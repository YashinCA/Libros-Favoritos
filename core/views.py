from core.forms import BookForm
from acceso.forms import UsuarioForm
from .models import Book
from acceso.models import Usuario
from django.shortcuts import redirect, render, HttpResponse
from django.db.models import Q
from django.urls import reverse
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        return redirect(reverse('books:books'))


class BooksAdd(View):
    def get(self, request):
        print(request.session['usuario']['id'])
        print(request.session['usuario']['nombre'])
        like_libro = Book.objects.all().filter(
            users_who_like__id=request.session['usuario']['id'])
        nolike_libro = Book.objects.all().exclude(
            users_who_like__id=request.session['usuario']['id'])
        books = Book.objects.all()
        contexto = {
            'formModel': BookForm(),
            'books': books.order_by("-created_at"),
            'like_libro': like_libro,
            'nolike_libro': nolike_libro,
        }
        return render(request, 'core/index.html', contexto)

    def post(self, request):
        if BookForm(request.POST):
            form = BookForm(request.POST)
            this_Usuario_inline = Usuario.objects.get(
                id=request.session['usuario']['id'])
            if form.is_valid():
                libro_recibido = form.save(commit=False)
                libro_recibido.uploaded_by = this_Usuario_inline
                libro_recibido.save()
                this_book_added = Book.objects.filter(
                    title__iexact=request.POST['title'])
                for book in this_book_added:
                    this_book = Book.objects.get(id=book.id)
                this_Usuario_inline.liked_books.add(this_book)
                messages.success(request, 'Libro agregado con exito')
                return redirect(reverse('books:books'))
            else:
                books = Book.objects.all()
                contexto = {
                    'formModel': form,
                    'books': books.order_by("-created_at"),
                }
                form = BookForm(request.POST)
                messages.error(request, 'Con errores, solucionar.')
                return render(request, 'core/index.html', contexto)


class BooksDetail(View):
    def get(self, request, pk):
        book_detail = Book.objects.get(id=pk)
        users_follow = Usuario.objects.all().filter(
            liked_books__id=book_detail.id)
        users_unfollow = Usuario.objects.all().exclude(
            liked_books__id=book_detail.id)
        if request.session['usuario']['id'] == book_detail.uploaded_by.id:
            fecha_creacion = Book.objects.get(id=pk).created_at
            fecha_modificacion = Book.objects.get(id=pk).updated_at
            form = BookForm(instance=book_detail)
            contexto = {
                'book_detail': book_detail,
                'formModel': form,
                'fecha_creacion': fecha_creacion,
                'fecha_modificacion': fecha_modificacion,
                'users_follow': users_follow,
                'users_unfollow': users_unfollow
            }
            return render(request, 'core/detail.html', contexto)
        else:
            contexto = {
                'book_detail': book_detail,
                'users_follow': users_follow,
                'users_unfollow': users_unfollow
            }
            return render(request, 'core/detail.html', contexto)

    def post(self, request, pk):
        # print(request.POST)
        book_detail = Book.objects.get(id=pk)
        form = BookForm(request.POST, instance=book_detail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro editado correctamente')
            return redirect(f'/books/{pk}')
        else:
            messages.error(request, 'Con errores, solucionar.')
            return redirect(f'/books/{pk}')


class BooksFollow(View):
    def get(self, request, pk):
        this_Usuario_inline = Usuario.objects.get(
            id=request.session['usuario']['id'])
        this_book = Book.objects.get(id=pk)
        this_Usuario_inline.liked_books.add(this_book)
        messages.success(request, 'Está dentro de tus favoritos.')
        return redirect(reverse('books:books'))

    def post(self, request, pk):
        # print(request.POST)
        book_detail = Book.objects.get(id=pk)
        this_Usuario_inline = Usuario.objects.get(
            id=request.session['usuario']['id'])
        this_Usuario_inline.liked_books.add(book_detail)
        messages.success(request, 'Está dentro de tus favoritos.')
        return redirect(f'/books/{pk}')


class BooksUnfollow(View):
    def get(self, request, pk):
        # print(request.GET)
        book_detail = Book.objects.get(id=pk)
        this_Usuario_inline = Usuario.objects.get(
            id=request.session['usuario']['id'])
        this_Usuario_inline.liked_books.remove(book_detail)
        messages.success(request, 'Ya no está en tus favoritos.')
        return redirect(f'/books/{pk}')


class BooksDestroy(View):
    def get(self, request, pk):
        deletebook = Book.objects.get(id=pk)
        deletebook.delete()
        return redirect(reverse('books:books'))


class BooksProfile(View):
    def get(self, request):
        favorite_books = Book.objects.all().filter(
            users_who_like__id=request.session['usuario']['id'])
        contexto = {
            'favorite_books': favorite_books
        }
        return render(request, 'core/profile.html', contexto)
