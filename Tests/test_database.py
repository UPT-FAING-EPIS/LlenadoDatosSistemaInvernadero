import unittest
from unittest.mock import patch, Mock
from Database.database import Database  # Asegúrate de importar correctamente tu módulo/clase Database

class TestDatabase(unittest.TestCase):
    
    @patch('mysql.connector.connect')
    def setUp(self, mock_connect):
        self.mock_db = Mock()
        mock_connect.return_value = self.mock_db

        self.db = Database('host', 'user', 'password', 'database')
        self.assertEqual(self.db.connection, self.mock_db)

    @patch('mysql.connector.connect')
    def test_insert_temperature(self, mock_connect):
        mock_connect.return_value = self.mock_db
        mock_cursor = Mock()
        self.mock_db.cursor.return_value = mock_cursor

        self.db.insert_temperature('12:00', 25.0)

        mock_cursor.execute.assert_called_once_with("INSERT INTO temperatura (hora, temperatura) VALUES (%s, %s)", ('12:00', 25.0))
        self.mock_db.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
