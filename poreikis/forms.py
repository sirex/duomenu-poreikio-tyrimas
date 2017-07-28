from django.forms import ModelForm

from poreikis.models import Request


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['project_name', 'author_email', 'description']
        help_texts = {
            'project_url': "Nuorodą į projekto svetainę nurodyti neprivaloma.",
            'description': (
                "Trumpai aprašykite savo idėją ar projektą ir nurodykite kokius duoemenis "
                "jau naudojate arba norėtumėte naudoti."
            ),
        }
