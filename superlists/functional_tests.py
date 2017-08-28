from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    """Tests the basic functions of the to-do site:
       - tests user input
       - tests adding the input to a list
       - tests saving the site and revisting the list at another time
    """
    def setup(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # the user goes to the homepage
        self.browser.get('http://localhost:8000')

        # the page title and header say to-do
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # the user is invited to enter a to-do item straight away

        # the user types a task into a text-box

        # When the user hits enter, the page updates, and now the page lists
        # "1: " + the task they entered, as an item in the list

        # There is another text box letting the user add another task.
        # the user enters another task

        # The page updates and shows both items on the lists

        # The site has generated a nique rl so the user can go back and see their list.
        # There is some explanatory text along with it.

        # The user visits the url to see that the list has been saved.

        # The browser stops when everything has been tested

if __name__ == '__main__':
    unittest.main(warnings='ignore')
