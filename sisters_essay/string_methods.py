def capitalize_title(title):
    """
        Convert the first letter of each word in the title to uppercase if needed.

        :param title: str - title string that needs title casing.
        :return: str - title string in title case (first letters capitalized).
    """

    capitalized_title = title.title()
    return capitalized_title

def check_sentence_ending(sentence):
    """
        Check the ending of the sentence to verify that a period is present.

        :param sentence: str - a sentence to check.
        :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    ends_with_period = sentence.endswith(".")
    return ends_with_period

def clean_up_spacing(sentence):
    """
        Verify that there is not any whitespace at the start and end of the sentence.

        :param sentence: str - a sentence to clean of leading and trailing space characters.
        :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    cleaned_up_sentence = sentence.strip()
    return cleaned_up_sentence