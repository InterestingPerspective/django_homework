from django import template

register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'

    return '#'


@register.filter()
def last_active_version(versions):
    active_versions = []
    if versions is not 'blank':
        for version in versions:
            if version.is_active:
                active_versions.append(version)
    else:
        return ''

    return f'{active_versions[-1].number} / {active_versions[-1].name}'
