from unittest import *
from unittest.mock import *

from services.exception import NotFoundServiceException
from services.create_transaction import create_transaction

class CreateTransactionTests(TestCase):
    @patch("services.create_transaction.Transaction.create")
    @patch("services.create_transaction.Category.get_or_none")
    @patch("services.create_transaction.User.get_or_none")
    def test_create_transaction_success(
        self,
        mock_user_get_or_none,
        mock_category_get_or_none,
        mock_transaction_create
    ):
        mock_user = Mock()
        mock_category = Mock()

        mock_transaction = Mock()
        mock_transaction.id = "transaction-1"
        
        mock_user_get_or_none.return_value = mock_user
        mock_category_get_or_none.return_value = mock_category
        mock_transaction_create.return_value = mock_transaction

        transaction_id = create_transaction(
            user_id = "user-1",
            category_id = "category-1",
            value = 100.0,
            date = "2024-01-01",
        )

        assert transaction_id == "transaction-1"

    @patch("services.create_transaction.Category.get_or_none")
    @patch("services.create_transaction.User.get_or_none")
    def test_create_transaction_user_not_found(
        self,
        mock_user_get_or_none,
        mock_category_get_or_none,
    ):
        mock_user = None
        mock_category = Mock()

        mock_user_get_or_none.return_value = mock_user
        mock_category_get_or_none.return_value = mock_category

        with TestCase.assertRaises(TestCase, NotFoundServiceException) as context:
            create_transaction(
                user_id = "user-1",
                category_id = "category-1",
                value = 100.0,
                date = "2024-01-01",
            )
            
        assert str(context.exception) == "User was not found"

    @patch("services.create_transaction.Category.get_or_none")
    @patch("services.create_transaction.User.get_or_none")
    def test_create_transaction_category_not_found(
        self,
        mock_user_get_or_none,
        mock_category_get_or_none,
    ):
        mock_user = Mock()
        mock_category = None

        mock_user_get_or_none.return_value = mock_user
        mock_category_get_or_none.return_value = mock_category

        with TestCase.assertRaises(TestCase, NotFoundServiceException) as context:
            create_transaction(
                user_id = "user-1",
                category_id = "category-1",
                value = 100.0,
                date = "2024-01-01",
            )
            
        assert str(context.exception) == "Category was not found"

if __name__ == "__main__":
    main()