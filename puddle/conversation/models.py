from django.db import models
from django.contrib.auth.models import User

from item.models import Item
#model for conversation between client and seller

class Conversation(models.Model):
    item=models.ForeignKey(Item,related_name='conversations',on_delete=models.CASCADE)
    members=models.ManyToManyField(User,related_name='conversations')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    #make order and arrangment of items by dateit modified 
    class Meta:
        ordering=('-modified_at',)


class ConversationMessage(models.Model):
    conversation=models.ForeignKey(Conversation,related_name='messages',on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='created_messages', on_delete=models.CASCADE)