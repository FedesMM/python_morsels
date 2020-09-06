import re
import sys


def semantic_wrap_v_1(text):
    text = text.replace('. ', '.\n')
    print(text)
    return text


def semantic_wrap(text):
    print(text)
    print("----------")
    # text = text.replace(r"([\.\!\?]) *", '\nAAAAAAAAAAAA')#r"\g1"+'\n')
    text = re.sub(r"([\.\!\?]) +", r"\g<1>\n", text)
    print(text)
    return text


def semantic_wrap(text):
    #print(old_text)
    #print("----------")
    text = re.sub(r"([\.\!\?]\"*) +", r"\g<1>\n", text)
    #print(new_text)
    return text


# if os.path.isfile(text_or_file):
if len(sys.argv) > 1:
    file_input_name = sys.argv[1]
    file_input = open(file_input_name, "r")
    old_text = file_input.read()
    file_input.close()
    new_text = semantic_wrap(old_text)
    print(new_text,end='')



