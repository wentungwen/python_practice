## Bonus exercise 4: Love letter(?)
sample_sentence = "Like every human beings I have many likes & dislikes. " \
                  "When I talk about my likes I like to talk about my favourite color, " \
                  "TV shows, movies, actor-actresses, food, books, pets, sports & music." \
                  "My favourite color is red. If given a choice I always choose " \
                  "red color because I find it pretty & glowing. I have many dislikes too. " \
                  "When I talk about my dislikes I like to talk about the color " \
                  "I hate the most, TV shows that makes me sick, " \
                  "movies that I hate, pets that I hate, foods that I avoid to eat etc. " \
                  "Generally I like all the colors except brown because I find it very dull, dark & nasty."

is_sentence_input = False
like = 0
hate = 0
words = ""

while not is_sentence_input:
    sentence = input(f"Use the sample sentence (type 1) or enter a sentence (type 2): ")
    if sentence == "1":
        words = sample_sentence
        print(f"The sample sentence is: {words}")
        is_sentence_input = True
    elif sentence == "2":
        words = input("Okay, please enter: ")
        is_sentence_input = True
    else:
        print("enter again:")

    words_list = words.lower().split()

for word in words_list:
    if word == "like" or word == "love":
        like += 1
    elif word == "hate" or word == "dislikes" or word == "dislike":
        hate += 1

if like == hate:
    print(f"\nHe feel neutral to you.")
elif like > hate:
    print(f"\nHe likes you.")
else:
    print(f"\nHe hates you.")

print(f"Like: {like}, Hate: {hate}")

