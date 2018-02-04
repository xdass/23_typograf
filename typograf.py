import re

actions = [
    (r'[ \t]+', ' '),  # remove extra space and tabs
    (r'\n+', '\n'),  # remove extra linebreak
    (r'[\"\'](.+)[\"\']', r'«\1»'),  # replace ' or " to « »
    (r'(\d+)‐(\d+)', r'\1&ndash;\2'),  # replacement of hyphens with dashes in phone numbers
    (r'(\d+)\s+(\w+)', r'\1&nbsp;\2'),  # connect numbers with words by non-breaking space
    (r'(\w+)—([то|либо|нибудь]+)', r'\1-\2'),  # replacing dashes on hyphens
    (r'(это)\s([а-яА-Я]+)', r'\1&nbsp;— \2'),  # replacing hyphens on dashes
    (r'([^-]\b[а-яА-Я]{1,2}\b)\s+(\w+)', r'\1&nbsp;\2')  # connect conjunctions and any words by non-breaking space
]


def beautify_text(text):
    for expr, replace in actions:
        text = re.sub(expr, replace, text, flags=re.I)
    return text
