from django.conf import settings
from django.core.files import File

__get_file_path = lambda file_name: str(settings.APPS_DIR.path(f"static/{file_name}"))


def get_file_to_save(file_path='assets/img/logo', file_name='logo.png') -> File:
    """
    Usage Example:
    ==============
    file_name = 'logo.png'
    file_path = 'assets/img/logo'
    obj = ModelClass.objects.create(name="My Brand", logo=None)
    file = get_file_to_save(file_name)
    obj.logo.save(obj.name, file, save=True)
    obj.save()
    """
    return File(open(__get_file_path(f'{file_path}/{file_name}'), 'rb'))
