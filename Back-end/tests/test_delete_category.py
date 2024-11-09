from unittest import *
from unittest.mock import *

from services.delete_category import delete_category

class DeleteCategoryTests(TestCase):
    @patch("services.delete_category.Category.get_by_id")
    def test_delete_category_success(
        self,
        mock_category_get_by_id
    ):
        mock_category = Mock()
        mock_category_get_by_id.return_value = mock_category

        delete_category("category-1")

        mock_category.delete_instance.assert_called_once()

    @patch("services.delete_category.Category.get_by_id")
    def test_delete_category_not_found(
        self,
        mock_category_get_by_id
    ):
        mock_category = None
        mock_category_get_by_id.return_value = mock_category

        delete_category("category-1")

if __name__ == "__main__":
    main()