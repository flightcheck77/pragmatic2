from django.forms import ModelForm
from footimgapp.models import Footimg


class FootimgCreationForm(ModelForm):
    class Meta:
        model = Footimg
        fields = ['image1',
                  'nickname1',
                  'message1',
                  'image2',
                  'nickname2',
                  'message2',
                  'image3',
                  'nickname3',
                  'message3',
        ]

