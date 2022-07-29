from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def SearchAuthor(keyword):
    return f'?keyword={keyword}'


@login_required
def listAuthor(request):
    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        authors = Author.objects.filter(Q(name__contains=keyword)
                                        | Q(country__contains=keyword))
    else:
        keyword = ''
        authors = Author.objects.all()
    paginator = Paginator(authors, 2)  # Show number contacts per page.

    page_number = request.GET.get('page')

    authors = paginator.get_page(page_number)
    try:
        authors = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        authors = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        authors = paginator.page(paginator.num_pages)

    searchauthor = SearchAuthor(keyword)

    filters = {
        'keyword': request.GET.get('keyword', ''),
    }
    return render(request, 'staff/author/list.html', {'authors': authors, 'searchauthor': searchauthor, 'filters': filters})


@login_required
def createAuthor(request):
    form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')

    return render(request, 'staff/author/form.html', {'form': form})


@login_required
def updateAuthor(request, id):
    author = get_object_or_404(Author, pk=id)
    form = AuthorForm(instance=author)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')

    return render(request, 'staff/author/form.html', {'form': form})


@login_required
def deleteAuthor(request, id):
    author = get_object_or_404(Author, pk=id)
    author.delete()
    return redirect('author-list')


def SearchPublisher(keyword):
    return f'?keyword={keyword}'

@login_required
def listPublisher(request):
    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        publishers = Publisher.objects.filter(Q(name__contains=keyword)
                                        | Q(code__contains=keyword))
    else:
        keyword = ''
        publishers = Publisher.objects.all()
    paginator = Paginator(publishers, 2)  # Show number contacts per page.

    page_number = request.GET.get('page')

    publishers = paginator.get_page(page_number)
    try:
        publishers = paginator.page(page_number)
    except PageNotAnInteger:
        publishers = paginator.page(1)
    except EmptyPage:
        publishers = paginator.page(paginator.num_pages)

    searchpublisher = SearchPublisher(keyword)

    filters = {
        'keyword': request.GET.get('keyword', ''),
    }
    return render(request, 'staff/publisher/list.html', {'publishers': publishers, 'searchpublisher': searchpublisher, 'filters': filters})
@login_required
def createPublisher(request):
    form = PublisherForm()

    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher-list')

    return render(request, 'staff/publisher/form.html', {'form': form})


@login_required
def updatePublisher(request, id):
    publisher = get_object_or_404(Publisher, pk=id)
    form = PublisherForm(instance=publisher)

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher-list')

    return render(request, 'staff/publisher/form.html', {'form': form})


@login_required
def deletePublisher(request, id):
    publisher = get_object_or_404(Publisher, pk=id)
    publisher.delete()
    return redirect('publisher-list')

def SearchCategory(keyword):
    return f'?keyword={keyword}'


@login_required

def listCategory(request):
    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        categories = Category.objects.filter(Q(code__contains=keyword)
                                            | Q(name__contains=keyword))
    else:
        keyword = ''
        categories = Category.objects.all()
    paginator = Paginator(categories, 1)  # Show number contacts per page.

    page_number = request.GET.get('page')

    categories = paginator.get_page(page_number)
    try:
        categories = paginator.page(page_number)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    searchcategory = SearchCategory(keyword)

    filters = {
        'keyword': request.GET.get('keyword', ''),
    }
    return render(request, 'staff/category/list.html', {'categories': categories, 'searchcategory': searchcategory, 'filters': filters})


@login_required
def createCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')

    return render(request, 'staff/category/form.html', {'form': form})


@login_required
def updateCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')

    return render(request, 'staff/category/form.html', {'form': form})


@login_required
def deleteCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('category-list')


def SearchBook(keyword):
    return f'?keyword={keyword}'


@login_required

def listBook(request):
    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        books = Book.objects.filter(Q(code__contains=keyword)
                                    | Q(title__contains=keyword))
    else:
        keyword = ''
        books = Book.objects.all()
    paginator = Paginator(books, 2)  # Show number contacts per page.

    page_number = request.GET.get('page')

    books = paginator.get_page(page_number)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        books = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        books = paginator.page(paginator.num_pages)

    searchbook = SearchBook(keyword)

    filters = {
        'keyword': request.GET.get('keyword', ''),
    }
    return render(request, 'staff/book/list.html', {'books': books, 'searchbook': searchbook, 'filters': filters})


@login_required
def createBook(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')

    return render(request, 'staff/book/form.html', {'form': form})


@login_required
def updateBook(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')

    return render(request, 'staff/book/form.html', {'form': form})


@login_required
def deleteBook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('book-list')


def SearchBookRent(keyword):
    return f'?keyword={keyword}'


@login_required
def listBookRent(request):
    bookRents = BookRent.objects.all()
    keyword = request.GET .get('keyword', '')
    if keyword:
        bookRents = bookRents.filter(
            Q(book__title__contains=keyword) | Q(book__code__contains=keyword))
    bookRents = bookRents.order_by('status')
    paginator = Paginator(bookRents, 5)  # Show number contacts per page.

    page_number = request.GET.get('page')

    bookRents = paginator.get_page(page_number)
    try:
        bookRents = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        bookRents = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        bookRents = paginator.page(paginator.num_pages)
    return render(request, 'staff/book_rent/list.html', {'bookRents': bookRents, 'keyword': keyword})

@login_required
def deliverBook(request, rentId):
    bookRent = get_object_or_404(BookRent, pk=rentId)
    book = bookRent.book
    bookRent.status = BookRent.Status.BORROWING
    bookRent.save()
    return redirect('book-rent-list')


@login_required
def returnBook(request, rentId):
    bookRent = get_object_or_404(BookRent, pk=rentId)
    book = bookRent.book
    book.numberOfAvailableCopy += 1
    book.save()
    bookRent.status = BookRent.Status.RETURNED
    bookRent.save()
    return redirect('book-rent-list')
