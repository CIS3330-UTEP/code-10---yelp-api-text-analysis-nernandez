import nltk

reviews = open("tacos_reviews.txt")

for review in reviews:
    tokens = nltk.word_tokenize(review)
    print(tokens)

    pos_tags = nltk.pos_tag(tokens)
    
    for token in pos_tags:
        if token[1] == 'JJ' or token[1] == 'NN':
            print(token)
