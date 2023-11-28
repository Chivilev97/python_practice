import unittest
import fix


class FixTestCase(unittest.TestCase):
    def test_passthrough(self):
        timeseries = [{'value': 0, 'timestamp': 100},
                      {'value': 8.4, 'timestamp': 110},
                      {'value': 0.999, 'timestamp': 120}]

        result = fix.fix(timeseries, 100, 130, 10)
        self.assertEqual(timeseries, result)

    def test_apply_from_to(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 8.4, 'timestamp': 110},
            {'value': 32.5, 'timestamp': 120},
            {'value': 0.999, 'timestamp': 130}
        ]
        expected = [
            {'value': 8.4, 'timestamp': 110},
            {'value': 32.5, 'timestamp': 120}
        ]
        result = fix.fix(timeseries, 110, 130, 10)
        self.assertEqual(expected, result)

    def test_apply_from_to_none_empty(self):
        timeseries = [

        ]
        expected = [
            {'value': None, 'timestamp': 90},
            {'value': None, 'timestamp': 100},
            {'value': None, 'timestamp': 110},
            {'value': None, 'timestamp': 120},
            {'value': None, 'timestamp': 130}
        ]
        result = fix.fix(timeseries, 90, 140, 10)
        self.assertEqual(expected, result)

    def test_apply_from_to_none(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 41.3, 'timestamp': 110}
        ]
        expected = [
            {'value': None, 'timestamp': 90},
            {'value': 0.5, 'timestamp': 100},
            {'value': 41.3, 'timestamp': 110},
            {'value': None, 'timestamp': 120},
            {'value': None, 'timestamp': 130}
        ]
        result = fix.fix(timeseries, 90, 140, 10)
        self.assertEqual(expected, result)

    def test_apply_irregular_from_to_none(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 41.3, 'timestamp': 110}
        ]
        expected = [
            {'value': None, 'timestamp': 90},
            {'value': 0.5, 'timestamp': 100},
            {'value': 41.3, 'timestamp': 110},
            {'value': None, 'timestamp': 120},
            {'value': None, 'timestamp': 130}
        ]
        result = fix.fix(timeseries, 89, 131, 10)
        self.assertEqual(expected, result)

    def test_adjust_irregular_timestamps(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 8.4, 'timestamp': 110},
            {'value': 32.5, 'timestamp': 118},
            {'value': 0.999, 'timestamp': 130},
            {'value': 41.3, 'timestamp': 139},
            {'value': 41.9, 'timestamp': 141}
        ]
        expected = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 8.4, 'timestamp': 110},
            {'value': 32.5, 'timestamp': 120},
            {'value': 0.999, 'timestamp': 130},
            {'value': 41.3, 'timestamp': 140},
            {'value': 41.9, 'timestamp': 150}
        ]
        result = fix.fix(timeseries, 100, 160, 10)
        self.assertEqual(expected, result)

    def test_insert_none(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 32.5, 'timestamp': 120},
            {'value': 0.999, 'timestamp': 130},
            {'value': 41.3, 'timestamp': 150}
        ]
        expected = [
            {'value': 0.5, 'timestamp': 100},
            {'value': None, 'timestamp': 110},
            {'value': 32.5, 'timestamp': 120},
            {'value': 0.999, 'timestamp': 130},
            {'value': None, 'timestamp': 140},
            {'value': 41.3, 'timestamp': 150}
        ]
        result = fix.fix(timeseries, 100, 160, 10)
        self.assertEqual(expected, result)

    def test_filter_duplicates(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 0.7, 'timestamp': 100},
            {'value': 32.5, 'timestamp': 110},
            {'value': 0.9, 'timestamp': 120},
            {'value': 0.8, 'timestamp': 125},
            {'value': 41.3, 'timestamp': 130},
            {'value': 41.3, 'timestamp': 140},
            {'value': 41.2, 'timestamp': 141},
            {'value': 41.3, 'timestamp': 142},
            {'value': 41.4, 'timestamp': 149}
        ]
        expected = [
            {'value': 0.5, 'timestamp': 100},
            {'value': 32.5, 'timestamp': 110},
            {'value': 0.9, 'timestamp': 120},
            {'value': 0.8, 'timestamp': 130},
            {'value': 41.3, 'timestamp': 140},
            {'value': 41.2, 'timestamp': 150}
        ]
        result = fix.fix(timeseries, 100, 160, 10)
        self.assertEqual(expected, result)

    def test_irregular_from_to_irregular_timestamps(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 105},
            {'value': 1, 'timestamp': 120},
            {'value': 1.5, 'timestamp': 130},
            {'value': 2, 'timestamp': 135},
            {'value': 3, 'timestamp': 139}
        ]
        expected = [
            {'value': 0.5, 'timestamp': 110},
            {'value': 1, 'timestamp': 120},
            {'value': 1.5, 'timestamp': 130}
        ]
        result = fix.fix(timeseries, 108, 138, 10)
        self.assertEqual(expected, result)

    def test_all_at_once(self):
        timeseries = [
            {'value': 0.5, 'timestamp': 105},
            {'value': 41.3, 'timestamp': 111},
            {'value': 0, 'timestamp': 130},
            {'value': 1, 'timestamp': 150},
            {'value': 2, 'timestamp': 151},
            {'value': 3, 'timestamp': 152},
            {'value': 4, 'timestamp': 159},
            {'value': 4, 'timestamp': 160},
            {'value': 5, 'timestamp': 160},
            {'value': 4, 'timestamp': 174},
            {'value': 5, 'timestamp': 175},
            {'value': 6, 'timestamp': 185}
        ]
        expected = [
            {'value': None, 'timestamp': 90},
            {'value': None, 'timestamp': 100},
            {'value': 0.5, 'timestamp': 110},
            {'value': 41.3, 'timestamp': 120},
            {'value': 0, 'timestamp': 130},
            {'value': None, 'timestamp': 140},
            {'value': 1, 'timestamp': 150},
            {'value': 2, 'timestamp': 160},
            {'value': None, 'timestamp': 170},
            {'value': 4, 'timestamp': 180}
        ]
        result = fix.fix(timeseries, 81, 186, 10)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
