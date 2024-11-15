from django.shortcuts import render
# from django.http import HttpResponse
from .forms import LengthConversion, WeightConversion, TemperatureConversion
from pint import UnitRegistry


def get_context(section, form):
    context = {
        "form": form,
        "section": section
    }
    return context

def convert(value, from_unit, to_unit):
    ureg = UnitRegistry()
    value = ureg.Quantity(value, from_unit)
    return value.to(to_unit).magnitude

def format_value(value):
    if len(str(float(value))) > 5:
        formatted_value = "{:.2e}".format(value)
        base, exponent = formatted_value.split("e")
        formatted_value = f"{base} x 10^{int(exponent)}"
    else:
        formatted_value = value
    return formatted_value

def conversion_view(request, form_class, template, section):
    if request.method == "POST":
        form = form_class(data=request.POST)
        if form.is_valid():
            value = form.cleaned_data["value"]
            from_unit = form.cleaned_data["from_unit"]
            to_unit = form.cleaned_data["to_unit"]
            result = (convert(value, from_unit, to_unit))
            context = {
                "result": format_value(result),
                "to_unit": to_unit,
                "from_unit": from_unit,
                "value": value,
            }
        return render(request, "result.html", context)

    else:
        form = form_class()
    return render(request, template, get_context(section, form))

def home(request):
    return render(request, "base.html")


def length(request):
    return conversion_view(request, LengthConversion, "length.html", "length")

def weight(request):
    return conversion_view(request, WeightConversion, "weight.html", "weight")
def temperature(request):
    return conversion_view(request, TemperatureConversion, "temperature.html", "temp")
