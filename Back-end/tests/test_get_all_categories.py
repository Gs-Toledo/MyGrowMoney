from unittest import *
from unittest.mock import *

from unittest.mock import patch, Mock
from services.get_all_categories import get_all_categories

class GetAllCategoriesTests(TestCase):
    @patch("services.get_all_categories.Category.select")
    def test_get_all_categories(self, mock_category_select):
        mock_query = Mock()
        mock_categories = [Mock(), Mock()]

        mock_query.execute.return_value = mock_categories
        mock_category_select.return_value = mock_query

        categories = get_all_categories()

        assert categories == mock_categories

if __name__ == "__main__":
    main()