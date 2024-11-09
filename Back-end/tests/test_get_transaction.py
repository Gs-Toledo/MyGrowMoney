from unittest import *
from unittest.mock import *

from services.get_transaction import get_transaction

class GetTransactionTests(TestCase):
    @patch("services.get_transaction.Transaction.get_by_id")
    def test_get_transaction_success(
        self,
        mock_transaction_get_by_id
    ):
        mock_transaction = Mock()
        mock_transaction_get_by_id.return_value = mock_transaction

        transaction = get_transaction("transaction-1")

        assert transaction == mock_transaction

if __name__ == "__main__":
    main()