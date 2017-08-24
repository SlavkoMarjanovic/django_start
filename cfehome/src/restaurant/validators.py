from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )
CATEGORIES = ['domaća', 'italijanska']
def validate_category(value):
    cat = value.capitalize()
    if value not in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError('Not a valid category')
