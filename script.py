import re


def lowercase_letters(string):
    """
    Write a regular expression to match a string that contains only lowercase letters.
    """
    return re.findall(r'\b[a-z]+\b', string)



def contains_digit(string):
    """
    Write a regular expression to match a string that contains at least one digit.
    """
    return re.findall(r'\d', string)

def word_length(string):
    """
    Write a regular expression to match a string that contains a word with exactly five letters.
    """
    return re.findall(r'\b\w{5}\b', string)

def url_regex(string):
    """
    Write a regular expression to match a valid URL.
    """
    return re.findall(r'^((http|https)://)(?:[\w.-]{2,255}(?:\.\w{2,6}){1,2})', string)
    #Got to be honest I have always hated this kind of check Its very light weight but passes

def mixed_case_letters(string):
    """
    Write a regular expression to match a string that contains a word with both uppercase and lowercase letters.
    """
    return re.findall(r'(.*[a-z])(.*[A-Z])', string)

def phone_number_regex(string):
    """
    Write a regular expression to match a phone number in a specific format, such as (123)456-7890.
    """
    return re.findall(r'\((\d{3})\)(\d{3})\-(\d{4})', string)


def consecutive_consonants(string):
    """
    Write a regular expression to match a string that contains a word with three or more consecutive consonants.
    """
    return re.findall(r'[^aeiou]{3,}', string)

def hello_world(string):
    """
    Write a regular expression to match a string that starts with "hello" and ends with "world".
    """
    return re.findall(r'^hello.*world$', string)

def consecutive_vowels(string):
    """
    Write a regular expression to match a string that contains three consecutive vowels.
    """
    return re.findall(r'[aeiou]{3,}', string)

def word_start_end_ae_noz(string):
    """
    Write a regular expression to match a string that contains a word that starts with "a" and ends with "e" and may have any number of characters in between, excluding "z".
    """
    return re.findall(r'^a.*[^z].*e$', string)

def email_regex(string):
    """
    Write a regular expression to match an email address.
    """
    return re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', string) #Not sure this would stand up these days as I have had it around for years


def vowel_start_length(string):
    """
    Write a regular expression to match a string that contains a word with a length of 7 or more characters and starts with a vowel.
    """
    return re.findall(r'', string)

def consecutive_repeating_characters(string):
    """
    Write a regular expression to match a string that contains a word with two or more consecutive repeating characters.
    """
    return re.findall(r'', string)


def repeated_word(string):
    """
    Write a regular expression to match a string that contains a word that is repeated consecutively at least twice.
    """
    return re.findall(r'', string)

def word_start_end_az_and_one_digit(string):
    """
    Write a regular expression to match a string that contains a word starting
    with "a" and ending with "z", with at least one digit in between.
    """
    return re.findall(r'^a.*(\d).*z$', string)