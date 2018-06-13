from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class TaskForm(forms.Form):
    name = forms.CharField(label='Task name', max_length=50)
    TASK_PRIORITY = (
        (3, 'HIGHER'),
        (2, 'MEDIUM'),
        (1, 'LOWER'),
    )
    priority = forms.ChoiceField(label='Task priority', choices=TASK_PRIORITY)
