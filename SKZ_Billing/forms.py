from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'w-[100%] p-3 border rounded-lg text-lg',  # Increased width
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border rounded-lg text-lg',
            'placeholder': 'Enter your last name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-[400px] p-3 border rounded-lg text-lg',
            'placeholder': 'Enter your email'
        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'w-[400px] p-3 border rounded-lg text-lg',
            'placeholder': 'Enter your phone number'
        })
    )
    service_choices = [
        ('web_dev', 'Web Development'),
        ('app_dev', 'App Development'),
        ('seo', 'SEO Optimization'),
        ('digital_marketing', 'Digital Marketing'),
    ]
    service = forms.ChoiceField(
        choices=service_choices,
        widget=forms.Select(attrs={'class': 'w-[400px] p-3 border rounded-lg text-lg'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-[500px] p-3 border rounded-lg text-lg',  # Wider textarea
            'rows': 4,
            'placeholder': 'Enter your message'
        }),
        required=False
    )
