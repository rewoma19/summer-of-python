"""
    Functions for creating, transforming, and adding prefixes to strings.
"""

def add_prefix_un(word):
    """
        Take the given word and add the "un" prefix.
        :param word: str - containing the root word.
        :return: str - of root word prepended with "un".
    """
    word_with_prefix = "un" + word.strip() # strip() string method removes any whitespace at the start and end of the string
    return word_with_prefix

def make_word_groups(vocab_words):
    """
        Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

        :param vocab_words: list - of a vocabulary words with prefix in first index.
        :return: str - of prefix followed by vocabulary words with prefix applied.

        This function takes a `vocab_words` list and returns a string with the prefix and the words with prefix applied, separated by ' :: '.

        For example: list('en', 'close', 'joy', 'lighten'), produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    prefixed_words = [prefix]

    for word in vocab_words[1:]:
        word = prefix + word
        prefixed_words.append(word)

    word_group = (" :: ").join(prefixed_words)
    return word_group

def remove_suffix_ness(word):
    """
        Remove the suffix from the word while keeping spelling in mind.

        :param word: str - of word to remove suffix from.
        :return: str - of word with suffix removed and spelling adjusted.

        For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    root_word = word[:-4]

    if root_word.endswith("i"):
        root_word = root_word.replace(root_word[-1], "y")

    return root_word

def adjective_to_verb(sentence, index):
    """
        Change the adjective within the sentence to a verb.

        :param sentence: str - that uses the word in sentence.
        :param index: int - index of the word to remove and transform.
        :return: str - word that changes the extracted adjective to a verb.

        For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words_list = sentence.split()
    verbified_word = None

    for word in words_list:
        words_list[-1] = words_list[-1].replace(".", "")
        if word == words_list[index]:
            verbified_word = word + "en"

    return verbified_word