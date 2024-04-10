from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import AuthorForm, QuoteForm
from django.contrib import messages
from .models import Author, Quote

def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html",
                  context={"quotes": quotes_on_page})

def author_info(request, author):
    author = Author.objects.get(fullname=author)
    return render(request, 'quotes/author_info.html', {'author': author})

def new_author(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author successfully added.')
            return redirect('quotes:new_author')
    else:
        form = AuthorForm()
    return render(request, 'quotes/new_author.html',
                  {'form': form, 'authors_set': authors})


def new_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # author_name = form.cleaned_data['author']
            # author, created = Author.objects.get_or_create(fullname=author_name)
            # quote_text = form.cleaned_data['quote']
            # tags = form.cleaned_data['tags']
            # quote = Quote(author=author, quote=quote_text, tags=tags)
            form.save()
            messages.success(request, 'Quote successfully added.')
            return redirect('quotes:success_url')
    else:
        form = QuoteForm()
    return render(request, 'quotes/new_quote.html', {'form': form})


def success_url(request):
    context = {
        'message': 'You added a new quote successfully',
    }
    return render(request, 'quotes/success.html', context)
