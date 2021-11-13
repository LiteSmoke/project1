from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question

class QuestionModelTest(TestCase):

    def test_published_days_ago_with_future_date(self):

        fut_time = timezone.now() + datetime.timedelta(days = 30)
        q = Question(pub_date=fut_time)
        self.assertIs(q.published_days_ago(3), False)
