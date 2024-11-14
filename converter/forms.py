from django import forms

length_choices = [
    ("mm", "Millimeter"),
    ("cm", "Centimeter"),
    ("m", "Meter"),
    ("km", "Kilometer"),
    ("in", "Inch"),
    ("ft", "Foot"),
    ("yd", "Yard"),
    ("mi", "Mile"),
]

weight_choice = [
    ("mg", "Milligram"),
    ("g", "Gram"),
    ("kg", "Kilogram"),
    ("t", "Ton"),
    ("oz", "Ounce"),
    ("lb", "Pound"),
]

temperature_choices = [
    ("c", "Celsius"),
    ("f", "Fahrenheit"),
    ("k", "Kelvin"),
]


class LengthConversion(forms.Form):
    value = forms.FloatField(label="Enter the length to convert")
    from_unit = forms.ChoiceField(
        choices=length_choices,
        widget=forms.Select,
        label="Unit to convert from",
    )
    to_unit = forms.ChoiceField(
        choices=length_choices,
        widget=forms.Select,
        label="Unit to convert to",
    )

class WeightConversion(forms.Form):
        value = forms.FloatField(label="Enter the weight to convert")
        from_unit = forms.ChoiceField(
            choices=weight_choice,
            widget=forms.Select,
            label="Unit to convert from",
        )
        to_unit = forms.ChoiceField(
            choices=weight_choice,
            widget=forms.Select,
            label="Unit to convert to",
        )
        
class Temperature(forms.Form):
        Value = forms.FloatField(label="Enter the temperature to convert")
        from_unit = forms.ChoiceField(
            choices=temperature_choices,
            widget=forms.Select,
            label="Unit to convert from",
        )
        to_unit = forms.ChoiceField(
            choices=temperature_choices,
            widget=forms.Select,
            label="Unit to convert to",
        )