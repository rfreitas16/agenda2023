from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from contact.models import Contact
from django.db.models import Q

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]

    context = {
        'contacts': contacts,
        'site_title':  'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    # Q eh um model do django para trocar a consulta AND por OR envolver em parenteses
    #precisa fazer o importe do model antes.

    contacts = Contact.objects.filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(last_name__icontains=search_value)
            )\
        .order_by('-id')

    context = {
        'contacts': contacts,
        'site_title':  'Search - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    #metodo get pega um/ pk= primary key
    single_contact = get_object_or_404(Contact.objects, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name}{single_contact.last_name} -'

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )