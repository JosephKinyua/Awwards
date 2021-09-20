class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)