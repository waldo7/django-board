from django.test import TestCase
from ..forms import SignUpForm


class SignupFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['usernama', 'email', 'password1', 'password2', ]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
