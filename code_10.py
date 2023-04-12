import nltk
from nltk.corpus import stopwords

reviews = open("tacos_reviews.txt")
stop_words = set(stopwords.words('english'))

for review in reviews:
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    new_text = []
    for tag in pos_tags:
        if tag[0] not in stop_words:
            print(tag[0])
            new_text.append(tag[0])

    for token in pos_tags:
        if token[1] == 'JJ' or token[1] == 'JJS':
            print(token[0])

print("\nOriginal")
print(review)
print("\nNew")
print("".join(new_text))
