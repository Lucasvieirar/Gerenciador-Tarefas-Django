from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Permite acessar um dicionário por chave dinâmica nos templates.
    Uso: {{ meu_dicionario|get_item:minha_variavel }}
    """
    return dictionary.get(key)