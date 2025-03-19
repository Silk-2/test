def dict_account(object_user):
    list_id = []
    for object in object_user:
        value = getattr(object, 'account_id')
        list_id.append(value)
    return list_id
