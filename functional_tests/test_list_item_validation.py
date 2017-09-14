from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    """ Test users input
    """

    def test_cannot_add_empty_list_items(self):
        # the user goes to a haome page and tries to submit
        # an empty list item. They hit ENTER on the
        # empty input box

        # The home page refreshes, and there is an error
        # message saying that list items cannot
        # be blank

        # They try again with some text forr the item,
        # it works

        # The user decides to submit a
        # second blank list item

        # They recieve a similar warning on the list page

        # And they can correct it by filling some text in
        self.fail('write me!')



