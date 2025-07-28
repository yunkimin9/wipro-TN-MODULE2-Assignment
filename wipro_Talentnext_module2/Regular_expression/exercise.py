# Q1- Write a program to find and check if a string has only octal digits. given string is ['789','123','004']

#Q2- Extract the user ID, domain name, and suffix from the following zuck@facebook.com , sunder33@google.com , jeff42@amazon.com  

#Q3- Split the following irregular sentence into proper words:

#Q4- Clean up the following tweet so that it contains only the user’s message (remove URLs, hashtags, mentions, punctuations, RTs, and CCs):

#Q5-Extract all the text portions between the tags from this HTML

#Q6-  Given the following list of words, identify the words that start and end with the same character: civic , trust ,widows ,maximum ,museums,aa  

import re
import requests


def check_octal(strings):
    octal_pattern = re.compile(r'^[0-7]+$')
    return {s: bool(octal_pattern.match(s)) for s in strings}


def extract_email_parts(emails):
    pattern = re.compile(r'(\w+)@(\w+)\.(\w+)')
    return pattern.findall(emails)


def clean_sentence(sentence):
    return re.sub(r'[\s;,_]+', ' ', sentence)


def clean_tweet(tweet):
    return re.sub(r'RT\s@\w+:|@\w+|http\S+|#\w+|cc:|[!]', '', tweet).strip()


def extract_html_text(url):
    r = requests.get(url)
    html = r.text
    text_list = re.findall(r'>([^<>]+)<', html)
    return [txt.strip() for txt in text_list if txt.strip()]


def same_start_end(words):
    pattern = re.compile(r'^(.).*\1$')
    return [word for word in words if pattern.match(word)]


if __name__ == "__main__":
   
    print("Task 1:", check_octal(['789', '123', '004']))

    emails = """zuck@facebook.com
    sunder33@google.com
    jeff42@amazon.com"""
    print("Task 2:", extract_email_parts(emails))

    print("Task 3:", clean_sentence("A, very   very; irregular_sentence"))

    tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
    print("Task 4:", clean_tweet(tweet))

    url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
    print("Task 5:", extract_html_text(url))

    words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
    print("Task 6:", same_start_end(words))

