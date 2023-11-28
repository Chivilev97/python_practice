import unittest
import validation_input


class TestIsValidationInputs(unittest.TestCase):

    def test_all_invalid(self):
        self.assertEqual({'name': False, 'last_name': False, 'zip_code': False, 'employee_id': False},
                         validation_input.validate_input(name='', last_name='', zip_code='', employee_id=''))

    def test_some_invalid(self):
        self.assertEqual({'name': True, 'last_name': False, 'zip_code': False, 'employee_id': False},
                         validation_input.validate_input(name='fff', last_name='', zip_code='', employee_id=''))
        self.assertEqual({'name': False, 'last_name': True, 'zip_code': False, 'employee_id': False},
                         validation_input.validate_input(name='', last_name='ааа', zip_code='', employee_id=''))
        self.assertEqual({'name': False, 'last_name': False, 'zip_code': True, 'employee_id': False},
                         validation_input.validate_input(name='', last_name='', zip_code='12345', employee_id=''))
        self.assertEqual({'name': False, 'last_name': False, 'zip_code': False, 'employee_id': True},
                         validation_input.validate_input(name='', last_name='', zip_code='', employee_id='AA-1234'))

    def test_name(self):
        result = validation_input.validate_input(name='f', last_name='', zip_code='', employee_id='')
        self.assertFalse(result['name'])

    def test_last_name(self):
        result = validation_input.validate_input(name='', last_name='f', zip_code='', employee_id='')
        self.assertFalse(result['last_name'])

    def test_zip_code(self):
        result = validation_input.validate_input(name='', last_name='', zip_code='a', employee_id='')
        self.assertFalse(result['zip_code'])

    def test_employee_id(self):
        result = validation_input.validate_input(name='', last_name='', zip_code='', employee_id='f')
        self.assertFalse(result['employee_id'])
        result = validation_input.validate_input(name='', last_name='', zip_code='', employee_id='AA-12345')
        self.assertFalse(result['employee_id'])
        result = validation_input.validate_input(name='', last_name='', zip_code='', employee_id='AA-123')
        self.assertFalse(result['employee_id'])
        result = validation_input.validate_input(name='', last_name='', zip_code='', employee_id='aa-1234')
        self.assertFalse(result['employee_id'])
        result = validation_input.validate_input(name='', last_name='', zip_code='', employee_id='Aa-1234')
        self.assertFalse(result['employee_id'])


if __name__ == '__main__':
    unittest.main()
