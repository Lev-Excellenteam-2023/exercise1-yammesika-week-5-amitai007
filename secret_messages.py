import re


def extract_secret_messages(filename):
    """ The course logo appears in the resources/logo.jpg file,
        and several secret messages are contained within it.
        The messages are strings of at least 5 letters,
        written in lowercase English letters only and ending with an exclamation mark"""
    regex_pattern = r'[a-z]{5}[a-z]*!'
    with open(filename, 'rb') as f:  # open file in read bits
        my_text = f.readline()  # read line from f(ile) and put in my_text
        while my_text:
            matches = re.findall(regex_pattern, my_text.decode(errors='ignore'))  # search the regex term
            for match in matches:
                yield match
            my_text = f.readline()


# endregion