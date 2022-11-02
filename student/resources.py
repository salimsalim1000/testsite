from django.contrib.auth.hashers import make_password
from gunicorn.config import User
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget

from .models import CustomUser

class UserResource(resources.ModelResource):

    def before_save_instance(self, instance, using_transactions, dry_run):
        pw = User.objects.make_random_password()
        instance.set_password(pw)

    if __name__ == '__main__':
        print("Populating the databases...")

        print('Populating Complete')

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        import_id_fields = ['id']

