from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ExampleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'someId'
        self.helper.form_class = 'some-class'
        self.helper.form_method = 'post'
        self.helper.form_action = 'sample_form_name'

        # Note that the submit button is added separately, with a Semantic UI class.
        self.helper.add_input(Submit('submit', 'Submit',
                              css_class='ui button'))

    like_website = forms.TypedChoiceField(
        label='Do you like this website?',
        choices=((1, 'Yes'), (0, 'No')),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )

    favorite_food = forms.CharField(
        label='What is your favorite food?',
        max_length=80,
        required=True,
    )

    favorite_color = forms.CharField(
        label='What is your favorite color?',
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label='Favorite number',
        required=False,
    )

    notes = forms.CharField(
        label='Additional notes or feedback',
        required=False,
    )