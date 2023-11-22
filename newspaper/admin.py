from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import CheckboxSelectMultiple
from django import forms

from newspaper.models import Redactor, Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("year_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("year_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                        "year_of_experience",
                    )
                },
            ),
        )
    )


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = '__all__'
        widgets = {
            'topic': CheckboxSelectMultiple,
            'publishers': CheckboxSelectMultiple,
        }


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("topic",)
    form = NewspaperForm


admin.site.register(Topic)
