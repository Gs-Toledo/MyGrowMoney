from unittest import *
from unittest.mock import *

from services.create_category import create_category

class CreateTransactionTests(TestCase):
    @patch("services.create_category.Category.create")
    def test_create_category_success(
        self,
        mock_category_create
    ):
        mock_category = Mock()
        mock_category.id = "category-1"

        mock_category_create.return_value = mock_category

        category_id = create_category(
            name = "Health",
            limit = 200.0,
        )

        assert category_id == "category-1"

if __name__ == "__main__":
    main()