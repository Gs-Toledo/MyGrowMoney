from unittest import *
from unittest.mock import *

from services.delete_transaction import delete_transaction

class DeleteTransactionTests(TestCase):
    @patch("services.delete_transaction.Transaction.get_by_id")
    def test_delete_transaction_success(
        self,
        mock_transaction_get_by_id
    ):
        mock_transaction = Mock()
        mock_transaction_get_by_id.return_value = mock_transaction

        delete_transaction("transaction-1")

        mock_transaction.delete_instance.assert_called_once()

    @patch("services.delete_transaction.Transaction.get_by_id")
    def test_delete_transaction_not_found(
        self,
        mock_transaction_get_by_id
    ):
        mock_transaction = None
        mock_transaction_get_by_id.return_value = mock_transaction

        delete_transaction("transaction-1")

if __name__ == "__main__":
    main()