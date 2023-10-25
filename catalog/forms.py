from django import forms
from catalog.models import UserReview

class UserFavoriteForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput)

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['rating', 'comment']

    rating = forms.ChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    )