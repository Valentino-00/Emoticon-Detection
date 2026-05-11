import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I feel disgusted")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am afraid of this")
        self.assertEqual(result['dominant_emotion'], 'joy')


if __name__ == '__main__':
    unittest.main()