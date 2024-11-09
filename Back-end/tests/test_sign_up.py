import unittest
from unittest.mock import patch, MagicMock
from uuid import UUID
from services.sign_up import sign_up, SignUpServiceException
from data.users import User

class TestSignUp(unittest.TestCase):
    @patch('services.sign_up.User')
    def test_sign_up_email_already_registered(self, MockUser):
        MockUser.get_or_none.return_value = MagicMock()
        
        with self.assertRaises(SignUpServiceException) as context:
            sign_up(
                name = "ABC",
                email="abc@example.com",
                password="123"
            )
        
        self.assertEqual(str(context.exception), "Email is already registered")

        MockUser.get_or_none.assert_called_once_with(email = "abc@example.com")

    @patch('services.sign_up.uuid4')
    @patch('services.sign_up.User')
    def test_sign_up_success(self, MockUser, MockUUID):
        MockUser.get_or_none.return_value = None
        
        MockUUID.return_value = UUID("734637c8-515d-4769-95f5-ee2d9acc6ff2")
        
        sign_up(
            name = "ABC",
            email = "abc@example.com",
            password = "123"
        )
        
        MockUser.create.assert_called_once_with(
            id = UUID("734637c8-515d-4769-95f5-ee2d9acc6ff2"),
            name = "ABC",
            email = "abc@example.com",
            password = "123"
        )

if __name__ == "__main__":
    unittest.main()