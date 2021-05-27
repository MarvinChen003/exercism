import re


def abbreviate(words):
    acronym = "".join([word.strip("_").capitalize()[0] for word in re.split(r'\s|-', words) if word != ""])
    return re.compile('[^a-zA-Z]').sub('', acronym)

