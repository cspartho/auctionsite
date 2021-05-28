from django.forms import ModelForm 
from .models import Bid

class BidForm(forms.ModelForm):
    """Form definition for Bid."""

    class Meta:
        """Meta definition for Bidform."""

        model = Bid
        fields = ('bid_price',)
    
    
