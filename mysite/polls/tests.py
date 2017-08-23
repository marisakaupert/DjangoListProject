# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently() returns False with questions whose pub_date is in
            the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day
        """

        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day
        """

        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


    def create_questions(question_text, days):
        """
        Create a question with the given 'question_text' and publish the
        given number of 'days' offset to now (negative for questions published
        in the past, positive for questions that have yet to be published)
        """

        
