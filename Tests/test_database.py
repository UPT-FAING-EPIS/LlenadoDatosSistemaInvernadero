import unittest
from unittest.mock import patch, Mock
import mysql.connector

from Database.database import Database

class TestDatabase(unittest.TestCase):
    
    @patch('mysql.connector.connect')
    def setUp(self, mock_connect):
        self.mock_db = Mock()
        mock_connect.return_value = self.mock_db

        self.db = Database('host', 'user', 'password', 'database', 'port')
        self.assertEqual(self.db.connection, self.mock_db)

    @patch('mysql.connector.connect')
    def test_insert_temperature(self, mock_connect):
        mock_connect.return_value = self.mock_db
        mock_cursor = Mock()
        self.mock_db.cursor.return_value = mock_cursor

        self.db.insert_temperature('12:00', 25.0)

        mock_cursor.execute.assert_called_once_with("INSERT INTO temperatura (hora, temperatura) VALUES (%s, %s)", ('12:00', 25.0))
        self.mock_db.commit.assert_called_once()

    @patch('mysql.connector.connect')
    def test_get_temperature(self, mock_connect):
        mock_connect.return_value = self.mock_db
        mock_cursor = Mock()
        self.mock_db.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (25.0,)

        result = self.db.get_temperature('12:00')

        mock_cursor.execute.assert_called_once_with("SELECT temperatura FROM temperatura WHERE hora = %s", ('12:00',))
        self.assertEqual(result, 25.0)

        mock_cursor.fetchone.return_value = None
        result = self.db.get_temperature('12:00')

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
