from django import forms

class MathProblemForm(forms.Form):
    latex_input = forms.CharField(widget=forms.Textarea, label="Enter an integral problem")