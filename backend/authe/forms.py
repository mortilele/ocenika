from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authe.models import User


class MainUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MainUserCreationForm, self).__init__(*args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'


class MainUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(MainUserChangeForm, self).__init__(*args, **kwargs)

    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'