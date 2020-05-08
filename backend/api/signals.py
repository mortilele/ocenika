from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from api.models import ProfessorReview

from profanity_filter import ProfanityFilter

pf = ProfanityFilter(languages=['ru', 'en'])


@receiver(pre_save, sender=ProfessorReview)
def pre_save_order_status(sender, instance, **kwargs):

    print(pf.censor(instance.review))
    instance.review = pf.censor(instance.review)
