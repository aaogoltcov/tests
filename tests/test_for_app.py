import unittest
from unittest.mock import patch
import app


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        self.error_docs = [{"type": "insurance", "number": "10006"}]
        self.get_all_docs = {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}
        self.get_doc_owner = 'Геннадий Покемонов'
        self.shelf_length = len(self.dirs)
        # print(self.shelf_length)
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_get_all_docs(self):
        with patch('app.update_date', return_value=(self.dirs, self.error_docs)):
            response = app.get_all_doc_owners_names()
            self.assertEqual(response, self.get_all_docs)

    def test_get_doc_owner(self):
        with patch('app.input', return_value="11-2"):
            # print(app.get_doc_owner_name())
            self.assertEqual(app.get_doc_owner_name(), self.get_doc_owner)
            self.assertTrue(app.get_doc_owner_name())

    def test_new_shelf(self):
        with patch('app.input', return_value="9999"):
            app.add_new_shelf()
            self.assertGreater(len(self.dirs), self.shelf_length)