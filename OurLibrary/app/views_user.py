from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_user import *

@login_required
def home(request):
    queryParams = request.GET    
    
    categoryId = queryParams.get('category_id')
    title = queryParams.get('title')
    categories = Category.objects.all()
    
    books = Book.objects.all()

    if categoryId:
        books = books.filter(category=Category.objects.get(id=categoryId))

    if title:
        books = books.filter(title__contains=title)

    context = {
        'queryParams': queryParams,
        'books': books,
        'categories': categories
    }

    return render(request, 'user/index.html', context)

@login_required
def viewBook(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'user/book_detail.html', {'book': book})

@login_required
def borrow(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BorrowForm()

    if request.method == 'POST':
        form = BorrowForm(request.POST)
        
        if form.is_valid():
            BookRent.objects.create(
                book=book,
                user=request.user,
                status=BookRent.Status.PENDING,
                startDate=datetime.now(),
                dueDate=form.cleaned_data['dueDate']
            )

            book.numberOfAvailableCopy -= 1
            book.save()

        return redirect('borrow-confirm', id)

    return render(request, 'user/borrow.html', {'book': book, 'form': form})

@login_required
def borrowConfirm(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'user/borrow_confirm.html', {'book': book})

@login_required
def pendingList(request):
    bookRents = BookRent.objects.filter(user=request.user, status=BookRent.Status.PENDING)
    return render(request, 'user/pending_list.html', {'page': 1, 'bookRents': bookRents})

@login_required
def borrowCancel(request, id):    
    bookRent = get_object_or_404(BookRent, pk=id)
    book = bookRent.book
    book.numberOfAvailableCopy += 1
    book.save()
    bookRent.delete()

    return redirect('pending-list')

@login_required
def borrowingList(request):
    bookRents = BookRent.objects.filter(user=request.user, status=BookRent.Status.BORROWING)
    print(len(bookRents))
    return render(request, 'user/borrowing_list.html', {'page': 2, 'bookRents': bookRents})
