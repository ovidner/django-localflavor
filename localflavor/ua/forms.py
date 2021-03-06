from django.forms.fields import RegexField, Select
from django.utils.translation import ugettext_lazy as _

from localflavor.compat import EmptyValueCompatMixin

from .ua_regions import UA_REGION_CHOICES


class UARegionSelect(Select):
    """
    A Select widget that uses a list of Ukrainian regions as its choices.

    .. versionadded:: 1.5
    """

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = UA_REGION_CHOICES
        super(UARegionSelect, self).__init__(*args, **kwargs)


class UAVatNumberField(EmptyValueCompatMixin, RegexField):
    """
    A form field that validates input as a Ukrainian analog of a VAT number.

    Valid format is XXXXXXXXXX.

    Whitespace around a VAT number is accepted and automatically trimmed.

    .. versionadded:: 1.5
    """

    default_error_messages = {
        'invalid': _('Enter a valid VAT number.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs['min_length'] = 10
        super(UAVatNumberField, self).__init__(r'^\d{10}$', *args, **kwargs)

    def to_python(self, value):
        value = super(UAVatNumberField, self).to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()


class UAPostalCodeField(EmptyValueCompatMixin, RegexField):
    """
    A form field that validates input as a Ukrainian postal code.

    Valid format is XXXXX. Note: first two numbers cannot be '00'.

    Whitespace around a postal code is accepted and automatically trimmed.

    .. versionadded:: 1.5
    """

    default_error_messages = {
        'invalid': _('Enter a valid postal code.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs['min_length'] = 5
        super(UAPostalCodeField, self).__init__(r'^(?!00)\d{5}$', *args, **kwargs)

    def to_python(self, value):
        value = super(UAPostalCodeField, self).to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()
