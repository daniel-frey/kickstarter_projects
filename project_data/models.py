from django.db import models


class Kickstarter(models.Model):
    """Representation of kickstarter data from Kaggle
    """
    id_data = models.IntegerField()
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.CharField(max_length=1024)
    goal = models.FloatField()
    launched = models.CharField(max_length=1024)
    pledged = models.FloatField()
    state = models.CharField(max_length=1024)
    backers = models.IntegerField()
    country = models.CharField(max_length=1024)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

    def __str__(self):
        """String representation of the kickstarter class
        """
        return f'Name:  ({self.name})'

    def __repr__(self):
        """Repr of the kickstarter class
        """
        return f'Name:  ({self.name})'
