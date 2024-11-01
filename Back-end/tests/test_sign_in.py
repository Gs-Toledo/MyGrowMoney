import unittest
from unittest.mock import patch, MagicMock
from services.sign_in import sign_in, SignInServiceException  # Update with your module name
from data.users import User

class TestSignIn(unittest.TestCase):
    @patch('services.sign_in.User')
    def test_sign_in_user_not_registered(self, MockUser):
        MockUser.get_or_none.return_value = None
        
        with self.assertRaises(SignInServiceException) as context:
            sign_in(
                email = "abc@example.com",
                password = "123"
            )
        
        self.assertEqual(str(context.exception), "Email is not registered")

    @patch('services.sign_in.User')
    def test_sign_in_incorrect_password(self, MockUser):
        mock_user = MagicMock()
        mock_user.check_password.return_value = False
        
        MockUser.get_or_none.return_value = mock_user
        
        with self.assertRaises(SignInServiceException) as context:
            sign_in(
                email = "abc@example.com",
                password="123"
            )
        
        self.assertEqual(str(context.exception), "Password does not match")

    @patch('services.sign_in.User')
    def test_sign_in_success(self, MockUser):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.check_password.return_value = True
        
        MockUser.get_or_none.return_value = mock_user
        
        output = sign_in(
            email = "abc@example.com",
            password="123"
        )
        
        self.assertEqual(output, mock_user.id)


if __name__ == "__main__":
    unittest.main()