from django import forms
from testApp.models import Comment,User,Post


class Mail_Send_Form(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' User Email ID'}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' Recipent Name'}))
    comments = forms.CharField(required=False, widget=forms.Textarea)

    widgets = {
            'name': forms.TextInput(attrs={'placeholder': ' Username'}),
            'email': forms.TextInput(attrs={'placeholder': ' User Email ID'}),
            'to': forms.TextInput(attrs={'placeholder': ' Recipent Name'}),
            'comments': forms.TextInput(attrs={'placeholder': ' Enter Your Comment Here'}),
             }


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': ' Username'}),
                'email': forms.TextInput(attrs={'placeholder': ' Email ID'}),
                 }

class Signup_Form(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
                'username': forms.TextInput(attrs={'placeholder': ' Username'}),
                'first_name': forms.TextInput(attrs={'placeholder': ' First Name'}),
                'last_name': forms.TextInput(attrs={'placeholder': ' Last Name'}),
                'email': forms.TextInput(attrs={'placeholder': ' Email ID'}),
                'password': forms.TextInput(attrs={'placeholder': ' Password'}),
        }
        fields = ['username','first_name','last_name','email','password']

class Recipe_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','category','author','user_detail','user_image','body','status','image','tags']
        widgets = {
                'title': forms.TextInput(attrs={'placeholder': ' Chicken Biryani'}),
                'slug': forms.TextInput(attrs={'placeholder': ' chicken-biryani'}),
                'category': forms.TextInput(attrs={'placeholder': ' Breakfast | Lunch | Dinner'}),
                'tags': forms.TextInput(attrs={'placeholder': 'Breakfast , Lunch , Dinner'}),
        }
        labels = {
        "image": "Food Image",
        "author":"Username",
        "body":"Recipe Content",
         }
