from unittest import *
from unittest.mock import *

from services.get_category import get_category

class GetCategoryTests(TestCase):
    @patch("services.get_category.Category.get_by_id")
    def test_get_category_success(
        self,
        mock_category_get_by_id
    ):
        mock_category = Mock()
        mock_category_get_by_id.return_value = mock_category

        category = get_category("category-1")

        assert category == mock_category

if __name__ == "__main__":
    main()