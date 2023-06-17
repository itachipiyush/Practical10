from django.shortcuts import render, redirect
from data10.models import Book

def add(request):
    if request.method == 'POST':
        auth_first_name = request.POST['auth_first_name']
        auth_email = request.POST['auth_email']
        title = request.POST['title']
        publisher = request.POST['publisher']
        publication_year = request.POST['publication_year']
        issue_status = request.POST.get('issue_status')== 'on' 
        issued_roll_no = request.POST.get('issued_roll_no', 0)
        
        book = Book.objects.create(
            auth_first_name=auth_first_name,
            auth_email=auth_email,
            Title=title,
            Publisher=publisher,
            Publication_year=publication_year,
            Issue_status= issue_status,
            Issued_roll_no=issued_roll_no,
        )
        
        return redirect('data10:display') 
    else:
        return render(request, 'add.html')

def delete(request):
    if request.method == 'POST':
        author_first_name = request.POST['author_first_name']
        Book.objects.filter(auth_first_name=author_first_name).delete()
        return redirect('data10:display')  
    else:
        return render(request, 'delete.html')

def display(request):
    books = Book.objects.all()
    return render(request, 'display.html', {'books': books})
