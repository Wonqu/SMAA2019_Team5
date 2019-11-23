import re
import regex


def extract_sentences(paragraph, min_word_length=3, min_words=8):
    """
    :param paragraph: string where each sentence is separated by '. '
    :param min_word_length: minimum number of letters for a sequence of chars to be considered a word
    :param min_words: minimum number of words in a sentence to be considered valuable for ML purposes
    :return: list of valid sentences for training models
    """
    paragraph = paragraph.replace('\n', ' ')
    clean_pattern = '[^0-9a-zA-Z \-;.]+'
    paragraph = re.sub(clean_pattern, "", paragraph)
    # split pattern catches 3 main types of sentences to be considered for split:
    # - sentences that end with capitalized word of length 4 or more (to exclude abbreviations such as "Dec.", "No."
    # - sentences that end with non-capitalized word of length 2 or more, to include endigns such as "at.", "of."
    # - sentences that end with pattern that describes place and time of letter in Mary Shelley's Frankenstein
    #   such as "St. Petersburgh, Dec. 11th, 17—."
    split_pattern = '(([A-Z][a-z]{3,})|( [a-z]{2,})|([0-9]{1,2}(st|nd|rd|th) [0-9]{1,2}))\K[:.]+ ?'
    # split paragraph by dots and add them again
    sentences = [f'{sentence}.' for sentence in regex.split(split_pattern, paragraph)]

    # last sentence will have additional dot because it won't be split, so remove that dot
    sentences[-1] = sentences[-1][:-1]
    sentences = [
        sentence.strip()
        for sentence in sentences if len(
            # count only alpha-numeric characters
            [
                word
                for word in sentence.split(' ')
                if len(word) >= min_word_length
            ]
        ) >= min_words
    ]

    return sentences


def extract_chapters(titles, filename):
    chapters = []
    with open(f'./data/{filename}', 'r', encoding='UTF-8') as f:
        line = f.readline()
        current_chapter = []
        while line:
            if line.strip().upper() in titles:
                if current_chapter:
                    chapters.append(' '.join(current_chapter))
                    current_chapter = []
            else:
                current_chapter.append(line.strip())
            line = f.readline()

    return chapters
