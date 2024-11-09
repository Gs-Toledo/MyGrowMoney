from unittest import *
from unittest.mock import *

from unittest.mock import patch, Mock
from services.get_all_transactions import get_all_transactions

class GetAllTransactionsTests(TestCase):
    @patch("services.get_all_transactions.Transaction.select")
    def test_get_all_transactions(self, mock_transaction_select):
        mock_query = Mock()
        mock_transactions = [Mock(), Mock()]

        mock_query.execute.return_value = mock_transactions
        mock_transaction_select.return_value = mock_query

        transactions = get_all_transactions()

        assert transactions == mock_transactions

if __name__ == "__main__":
    main()