
def to_dict(clazz_instance):
    if type(clazz_instance) is list:
        result = [to_dict(item) for item in clazz_instance if type(item) is object]
    elif type(clazz_instance) is dict:
        result = [{key: to_dict(clazz_instance[key])} for key in clazz_instance]
    else:
        result = {field: getattr(clazz_instance, field) for field in clazz_instance._fields}
    return result
