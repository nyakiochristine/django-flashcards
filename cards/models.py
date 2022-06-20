from django.db import models
import random


class Card_Set(models.Model):
    '''
    Card_Set model functions as the deck that a card belongs to
    A deck has a topic and description
    '''
    topic = models.CharField(max_length = 50, null = False, blank = False)       # Topic of the Deck
    description = models.CharField(max_length = 300, null = False, blank = True) # Description of topic
    created_by = models.CharField(max_length= 300, null = False, blank = True)
    is_active = models.BooleanField(default = True)  
    
def __str__(self):
        return self.topic


def get_card_count(self):
        '''
        Returns the card count in each deck as an integer
        '''
        return self.card_set.count()
get_card_count.short_description = 'Card Count' 


class Card(models.Model):
    '''
    Card model for the cards in the deck
    Parent- Card_Set model
    Each card has word, definition, and sentence
    '''
    parent_card_set = models.ForeignKey(Card_Set, on_delete = models.CASCADE)

    word = models.CharField(max_length = 50, null = False, blank = False)         # Vocabulary word
    definition = models.TextField(max_length = 500, null = False, blank = False)  # Word's definition
    sentences = models.TextField(max_length = 500, null = False, blank = True)    # Word used in sentence


    def __str__(self):
        return self.word


    def is_there_previous_card(self):
        '''
        Returns True  if card  is not the frist card in the deck
        '''
        first_card_in_set = self.parent_card_set.card_set.first()
        if self == first_card_in_set:
            return False
        else:
            return True


    def get_previous_card(self):
        '''
        Returns the previous card in the deck
        '''
        first_card_in_set = self.parent_card_set.card_set.first()

        if self == first_card_in_set:
            return self.parent_card_set.card_set.last()
        else:
            return self.parent_card_set.card_set.filter(id__lt = self.id).last()


    def is_there_a_next_card(self):
        '''
        Returns True if is not last in the deck
        '''
        last_card_in_set = self.parent_card_set.card_set.last()
        if self == last_card_in_set:
            return False
        else:
            return True


    def get_next_card(self):
        '''
        Returns the next card on the deck
        '''
        last_card_in_set = self.parent_card_set.card_set.last()
        if self == last_card_in_set:
            return self.parent_card_set.card_set.first()
        else:
            return self.parent_card_set.card_set.filter(id__gt = self.id).first()  