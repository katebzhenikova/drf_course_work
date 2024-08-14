from django.contrib import admin

from habits.models import Habit, HabitPeriodicity
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "is_active", "is_staff", "tg_nick")
    search_fields = ("email", "phone", "tg_nick")
    list_filter = ("is_active", "is_staff", "groups", "tg_nick")
    ordering = ("email", "tg_nick")
    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "avatar")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {"fields": ("last_login", "date_joined", "tg_nick", "tg_chat_id")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "phone", "password1", "password2"),
            },
        ),
    )


class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "user",
        "place",
        "is_pleasant",
        "related_habit",
        "reward",
        "get_periodicity",
        "start_at",
        "estimated_time",
        "is_public",
    )
    filter_horizontal = ("periodicity",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если объект еще не создан
            super().save_model(request, obj, form, change)
            if (
                "related_habit" in form.cleaned_data
                and form.cleaned_data["related_habit"]
            ):
                related_habit = form.cleaned_data["related_habit"]
                related_habit.related_habit = obj
                related_habit.save()
        else:
            super().save_model(request, obj, form, change)


admin.site.register(Habit, HabitAdmin)
admin.site.register(HabitPeriodicity)
