from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post
from .utils import get_random_code


@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())

    # if not instance.slug:
    #     instance.slug = slugify(
    #         instance.author.username + " " + instance.title
    #     )
    # this will throw an error when same user enter same title!!!!

# a = "henry forester"

# print(slugify(a)) ==> henry-forester