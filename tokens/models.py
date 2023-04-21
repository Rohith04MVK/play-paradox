from django.db import models


class TokenAccount(models.Model):
    card_id = models.CharField(max_length=10, unique=True)
    play_tokens = models.IntegerField(default=0)
    gift_tokens = models.IntegerField(default=0)
