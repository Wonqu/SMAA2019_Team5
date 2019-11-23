import uuid

from extract_sentences import extract_sentences


if __name__ == '__main__':
    with open('./data/hpl_clean.txt', 'r', encoding='UTF-8') as hpl:
        sentences = [
            sentence
            for line in hpl.readlines()
            for sentence in extract_sentences(line)
        ]

    with open('./data/out/hpl.csv', 'w', encoding='UTF-8') as hpl:
        newline = '\n'
        hpl.write(f'"id","text","author"{newline}')
        for s in sentences:
            hpl.write(f'"{uuid.uuid4()}","{s}","HPL"{newline}')
