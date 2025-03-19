from django.shortcuts import render
from .models import list_of_accounts
from .forms import valideForm
from .other_functions import dict_account


def deposit_and_withdraw(request, id_value):
    form = valideForm()

    if request.method == "POST":
        form = valideForm(request.POST)
        all_users = list_of_accounts.objects.all()

        final_choise = request.POST.get('choise_value')
        value = request.POST.get('value')

        list_id = dict_account(all_users)
        if id_value in list_id:
            for user in all_users:
                if getattr(user, 'account_id') == str(id_value):
                    if final_choise == '1':
                        user.quantity_cat_point += int(value)
                        user.save()
                    elif final_choise == '2':
                        user.quantity_cat_point -= int(value)
                        user.save()
        else:
            new_object = list_of_accounts(account_id=id_value, quantity_cat_point=value)
            new_object.save()

    return render(request, 'test_quest_app/core.html', context={'form': form,  'responce': id_value})


def get_balance(request, id_value):

    all_users = list_of_accounts.objects.all()
    dict_user = {}

    for user in all_users:
        if getattr(user, 'account_id') == str(id_value):
            point_value = getattr(user, 'quantity_cat_point')
            dict_user['point_value'] = point_value

    return render(request, 'test_quest_app/balance.html', context={'dict_user': dict_user})
