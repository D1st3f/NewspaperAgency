from django.test import TestCase
from newspaper.models import Redactor, Newspaper, Topic


class RedactorModelTest(TestCase):
    def test_redactor_model_str_method(self):
        redactor = Redactor(username='john_doe', first_name='John', last_name='Doe')
        self.assertEqual(str(redactor), 'john_doe (John Doe)')

    def test_redactor_model_year_of_experience(self):
        redactor = Redactor(username='john_doe', year_of_experience=5)
        self.assertEqual(redactor.year_of_experience, 5)


class TopicModelTest(TestCase):
    def test_topic_model_str_method(self):
        topic = Topic(name='Science')
        self.assertEqual(str(topic), 'Science')


class NewspaperModelTest(TestCase):
    def test_newspaper_model_str_method(self):
        newspaper = Newspaper(title='Daily News', content='Breaking news!')
        self.assertEqual(str(newspaper), 'Daily News')

    def test_newspaper_model_publishers(self):
        redactor1 = Redactor.objects.create(username='john_doe1', first_name='John', last_name='Doe1')
        redactor2 = Redactor.objects.create(username='john_doe2', first_name='John', last_name='Doe2')

        newspaper = Newspaper(title='Daily News', content='Breaking news!')
        newspaper.save()
        newspaper.publishers.add(redactor1, redactor2)
        newspaper.save()

        self.assertEqual(newspaper.get_publishers(), 'John Doe1, John Doe2')

    def test_newspaper_model_topics(self):
        topic1 = Topic.objects.create(name='Science')
        topic2 = Topic.objects.create(name='Technology')

        newspaper = Newspaper(title='Daily News', content='Breaking news!')
        newspaper.save()
        newspaper.topic.add(topic1, topic2)
        newspaper.save()

        self.assertEqual(newspaper.get_topics(), 'Science, Technology')

    def test_redactor_model_with_year_of_experience(self):
        redactor = Redactor(username='john_doe', year_of_experience=5)
        self.assertEqual(redactor.year_of_experience, 5)

    def test_topic_model_with_name(self):
        topic = Topic(name='Science')
        self.assertEqual(topic.name, 'Science')
