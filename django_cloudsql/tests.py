import unittest
from mock import patch, Mock
from mock_django.query import QuerySetMock
from django_cloudsql.storage import Storage
from models import Score

class StorageTestCase(unittest.TestCase):
  @patch('django_cloudsql.storage.Score')
  def test(self, score_class_mock):
    save_mock = Mock(return_value=None)
    score_class_mock.return_value.save = save_mock

    storage = Storage()
    storage.populate()
    self.assertEqual(save_mock.call_count, 1)

    score = Score()
    score.score = 1234
    score_class_mock.objects.all.return_value.order_by.return_value = QuerySetMock(score_class_mock, score)
    score = storage.get_score()
    self.assertEqual(score, 1234)

if __name__ == "__main__":
  unittest.main()
