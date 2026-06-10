'''Given a string of text, return a dict with:
- word_count: total number of words
- unique_words: number of unique words
- most_common: the word that appears most often
               lowercase, ignore punctuation
- longest_word: the longest word in the text
               if tie return alphabetically first

Input:
text = "the cat sat on the mat the cat sat"

Expected:
{
    "word_count": 9,
    "unique_words": 5,
    "most_common": "the",
    "longest_word": "mat"
}

Edge cases:
- empty string → return {}
- single word → most_common = that word'''


text = "the cat sat on the mat the cats sat"


def word_count(text):

    unique_word = set()

    word_counts ={}


    if not text:
        return {}

    words = text.split()
    unique_word = set(words)  

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    most_common = max(word_counts, key=lambda x: word_counts[x])
    longest = max(sorted(words), key=lambda x: len(x))



    return {

    "word_count": len(words),
    "unique_words": len(unique_word),
    "most_common": most_common,
    "longest_word": longest

    }  






result = word_count(text)   
print(result) 
