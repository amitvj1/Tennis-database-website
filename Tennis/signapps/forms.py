from django import forms

from.models import SignUp
from.models import Player
from.models import H2H
from.models import recentResult
from.models import searchResult
from.models import individualRank
from.models import playerByRank
from.models import completeRanking

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
class H2HForm(forms.ModelForm):
    class Meta:
        model = H2H
class RecentResultForm(forms.ModelForm):
    class Meta:
        model = recentResult
class SearchResultForm(forms.ModelForm):
    class Meta:
        model = searchResult
class IndividualRankForm(forms.ModelForm):
    class Meta:
        model = individualRank
class PlayerRankForm(forms.ModelForm):
    class Meta:
        model = playerByRank
class CompleteRankingForm(forms.ModelForm):
    class Meta:
        model = completeRanking 
    
