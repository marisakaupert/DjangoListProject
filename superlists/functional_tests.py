from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    """Tests the basic functions of the to-do site:
       - tests user input
       - tests adding the input to a list
       - tests saving the site and revisting the list at another time
    """

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # the user goes to the homepage
        self.browser.get('http://localhost:8000')

        # the page title and header say to-do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # the user is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # the user types a task into a text-box
        inputbox.send_keys('Buy peacock feathers')

        # When the user hits enter, the page updates, and now the page lists
        # "1: " + the task they entered, as an item in the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1. Buy peacock feathers')        

        # There is another text box letting the user add another task.
        # the user enters another task
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # The page updates and shows both items on the lists
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make a fly')

        # The site has generated a unique rl so the user can go back and see their list.
        # There is some explanatory text along with it.

        # The user visits the url to see that the list has been saved.

        # The browser stops when everything has been tested

if __name__ == '__main__':
    unittest.main(warnings='ignore')
