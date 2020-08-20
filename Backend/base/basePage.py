from .basicActions import Actions


class BasePage(Actions):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver

    def text_matches(self, actual_text, expected_text):
        if actual_text.lower() == expected_text.lower():
            return True
        else:
            return False

    def text_contains(self, actual_text, expected_text):
        print('{} and {}'.format(actual_text, expected_text))
        if expected_text.lower() in actual_text.lower():

            return True
        else:
            return False

    def validate_page_title(self, title_to_validate, exact_match='yes'):
        """
        Validates the page title.
        params:
            title_to_validate
            exact_match: yes/no (Default yes)
                if yes: Return True only when actual title matches with the expected
                if no: Return True when actual title contains expected title
        """
        actual_title = self.get_title()
        print(actual_title)
        if exact_match == 'yes':
            return self.text_matches(actual_title, title_to_validate)
        else:
            return self.text_contains(actual_title, title_to_validate)
