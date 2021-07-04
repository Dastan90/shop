from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# class ShoeAdminForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = mark_safe(
#             """<span style="color:red; font-size: 14px;">При загрузке изоброжение с разрешением больше {}x{} оно будет обрезать</span>
#             """.format(
#                 *Product.MAX_RESOLUTION
#             )
#         )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     min_height, min_width = Product.MIN_RESOLUTION
    #     max_height, max_width = Product.MAX_RESOLUTION
    #     if image.size > Product.MAX_IMAGE_SIZE:
    #         raise ValidationError('Размер изображение не должен превышать 3MB')
    #     if img.height < min_height or img.width < min_width:
    #         raise ValidationError('Разрешение изображение меньше минимального')
    #     if img.height > max_height or img.width > max_width:
    #         raise ValidationError('Разрешение изображение больше максимального')
    #     return image


class ShoeAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.color:
            self.fields['color_volume_max'].vidget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def clean(self):
        if not self .cleaned_data['color']:
            self.cleaned_data['color_volume_max'] = None
        return self.cleaned_data


class ShirtAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.color:
            self.fields['color_volume_max'].vidget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def clean(self):
        if not self .cleaned_data['color']:
            self.cleaned_data['color_volume_max'] = None
        return self.cleaned_data


class ShortAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.color:
            self.fields['color_volume_max'].vidget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def clean(self):
        if not self .cleaned_data['color']:
            self.cleaned_data['color_volume_max'] = None
        return self.cleaned_data


class MikeyAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.color:
            self.fields['color_volume_max'].vidget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def clean(self):
        if not self .cleaned_data['color']:
            self.cleaned_data['color_volume_max'] = None
        return self.cleaned_data


class ShoeAdmin(admin.ModelAdmin):

    # form = ShoeAdminForm

    change_form_template = 'admin.html'
    form = ShoeAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ShortAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = ShortAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shorts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ShirtAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = ShirtAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shirts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class MikeyAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = MikeyAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='mikeys'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Short, ShortAdmin)
admin.site.register(Shirt, ShirtAdmin)
admin.site.register(Mikey, MikeyAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)