import pathlib
import unittest

from gradescope_utils.autograder_utils.decorators import weight, leaderboard

from text_recognizer.datasets import EmnistDataset
from text_recognizer.character_predictor import CharacterPredictor
from text_recognizer.models.emnist_mlp import EmnistMlp


SUPPORT_DIRNAME = pathlib.Path(__file__).parents[0].resolve() / 'tests' / 'support'


class TestCharacterPredictor(unittest.TestCase):
    @weight(10)
    def test_filename(self):
      predictor = CharacterPredictor()

      for filename in SUPPORT_DIRNAME.glob('*.png'):
        pred, conf = predictor.predict(str(filename))
        print(pred, conf, filename.stem)
        self.assertEqual(pred, filename.stem)
        self.assertGreater(conf, 0.4)


class TestEvaluateCharacterPredictor(unittest.TestCase):
    @leaderboard("accuracy")
    def test_evaluate_accuracy(self, set_leaderboard_value=None):
        dataset = EmnistDataset()
        dataset.load_or_generate_data()
        model = EmnistMlp()
        metric = model.evaluate(dataset.x_test, dataset.y_test)
        set_leaderboard_value(metric)
