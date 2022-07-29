from django.urls import path, include

from .import views_user, views_staff, views

urlpatterns =[
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup), 
    path('accounts/profile', views.profile, name='profile'),

    path('', views_user.home, name='home'),
    path('view_book/<int:id>', views_user.viewBook, name='view-book'),
    path('borrow/<int:id>', views_user.borrow, name='borrow'),
    path('borrow_confirm/<int:id>', views_user.borrowConfirm, name='borrow-confirm'),    
    path('pending_list', views_user.pendingList, name='pending-list'),
    path('borrow_cancel/<int:id>', views_user.borrowCancel, name='borrow-cancel'),
    path('borrowing_list', views_user.borrowingList, name='borrowing-list'),    
        
    path('staff', views_staff.listBook, name='book-list'),
    path('staff/book_create', views_staff.createBook, name='book-create'),  
    path('staff/book_update/<int:id>', views_staff.updateBook, name='book-update'),  
    path('staff/book_delete/<int:id>', views_staff.deleteBook, name='book-delete'),  

    path('staff/book_rent_list', views_staff.listBookRent, name='book-rent-list'),
    path('staff/book_deliver/<int:rentId>', views_staff.deliverBook, name='book-deliver'),
    path('staff/book_return/<int:rentId>', views_staff.returnBook, name='book-return'),

    path('staff/author_list', views_staff.listAuthor, name='author-list'),
    path('staff/author_create', views_staff.createAuthor, name='author-create'),  
    path('staff/author_update/<int:id>', views_staff.updateAuthor, name='author-update'),  
    path('staff/author_delete/<int:id>', views_staff.deleteAuthor, name='author-delete'),  

    path('staff/publisher_list', views_staff.listPublisher, name='publisher-list'),
    path('staff/publisher_create', views_staff.createPublisher, name='publisher-create'),  
    path('staff/publisher_update/<int:id>', views_staff.updatePublisher, name='publisher-update'),  
    path('staff/publisher_delete/<int:id>', views_staff.deletePublisher, name='publisher-delete'),  

    path('staff/category_list', views_staff.listCategory, name='category-list'),
    path('staff/category_create', views_staff.createCategory, name='category-create'),  
    path('staff/category_update/<int:id>', views_staff.updateCategory, name='category-update'),  
    path('staff/category_delete/<int:id>', views_staff.deleteCategory, name='category-delete'),  
]