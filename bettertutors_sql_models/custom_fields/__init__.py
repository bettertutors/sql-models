from peewee import Field, coerce_to_unicode, CharField

from validate_email import validate_email


class EmailField(CharField):
    def coerce(self, value):
        # In production, recommend using: `validate_email(value, check_mx=True, verify=True)`
        assert validate_email(value), 'Expected a valid email from: "{value}"'.format(value=value)
        return super(CharField, self).coerce(value)


class InField(CharField):
    # Discussion happening at: http://stackoverflow.com/q/28925880
    pass
