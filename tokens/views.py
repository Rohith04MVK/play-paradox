from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import TokenForm
from .models import TokenAccount

def add_play_tokens(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            card_id = form.cleaned_data['card_id_input']
            amount = form.cleaned_data['amount_input']
            operation_input = form.cleaned_data['operation_input']
            print(operation_input)
            try:
                account = TokenAccount.objects.get(card_id=card_id)   
            except TokenAccount.DoesNotExist:
                account = TokenAccount(card_id=card_id)
            if operation_input == '+':
                account.play_tokens += amount
                account.save()
                return HttpResponse(f"{amount} play tokens added to card {card_id}")
            elif operation_input == '-':
                account.play_tokens -= amount
                account.save()
                return HttpResponse(f"{amount} play tokens have been removed from card {card_id}")
    else:
        form = TokenForm()
    return render(request, 'add_play_tokens.html', {'form': form})

def add_play_tokens_page(request):
    form = TokenForm()
    return render(request, 'add_play_tokens.html', {'form': form})

def account_balances(request):
    accounts = TokenAccount.objects.all()
    return render(request, 'account_balances.html', {'accounts': accounts})