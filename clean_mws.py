import uuid

from extract_sentences import extract_sentences, extract_chapters

FRANKENSTEIN_CHAPTERS = {
    x.upper().strip() for x in
    """Letter 1
        Letter 2
        Letter 3
        Letter 4
        Chapter 1
        Chapter 2
        Chapter 3
        Chapter 4
        Chapter 5
        Chapter 6
        Chapter 7
        Chapter 8
        Chapter 9
        Chapter 10
        Chapter 11
        Chapter 12
        Chapter 13
        Chapter 14
        Chapter 15
        Chapter 16
        Chapter 17
        Chapter 18
        Chapter 19
        Chapter 20
        Chapter 21
        Chapter 22
        Chapter 23
        Chapter 24
    """.split('\n') if x.upper().strip()
}


if __name__ == '__main__':
    sentences = [
        sentence
        for poem in extract_chapters(FRANKENSTEIN_CHAPTERS, 'mws_clean.txt')
        for sentence in extract_sentences(poem)
    ]

    with open('./data/out/mws.csv', 'w', encoding='UTF-8') as mws:
        newline = '\n'
        mws.write(f'"id","text","author"{newline}')
        for s in sentences:
            mws.write(f'"{uuid.uuid4()}","{s}","MWS"{newline}')
