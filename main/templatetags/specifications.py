from django import template
from django.utils.safestring import mark_safe

from main.models import Shoe, Shirt, Short, Mikey

register = template.Library()


TABLE_HEAD = """
            <container>
                 <table class="table">
                    <tbody>
             """

TABLE_TAIL = """
                     </tbody>
                 </table>
            </container>
             """

TABLE_CONTENT = """
                <tr>
                     <td>{name}</td>
                     <td>{value}</td>
                </tr>
                """

PRODUCT_SPEC = {
    'shoe': {
        'Бренд': 'brand',
        'Пол': 'gender',
        'Модель': 'model',
        'Цвет': 'color',
        'Размер': 'size',
    },
    'short': {
            'Бренд': 'brand',
            'Пол': 'gender',
            'Модель': 'model',
            'Цвет': 'color',
            'Размер': 'size',
    },
    'mikey': {
            'Бренд': 'brand',
            'Пол': 'gender',
            'Модель': 'model',
            'Цвет': 'color',
            'Размер': 'size',
    },
    'shirt': {
            'Бренд': 'brand',
            'Пол': 'gender',
            'Модель': 'model',
            'Цвет': 'color',
            'Размер': 'size',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)