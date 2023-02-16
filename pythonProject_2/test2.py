letters = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
letter_list = letters.split(", ")
score = "11, 5, 9, 19, 6, 21, 8, 22, 18, 16, 4, 12, 10, 24, 25, 13, 17, 7, 26, 23, 2, 20, 14, 3, 15, 1"
score_list = score.split(", ")

new_list = {}
is_game_end = False
while not is_game_end:
    for a in range(len(letter_list)):
        new_word = letter_list[a-1]
        new_num = score_list[a-1]
        new_list[new_word] = int(new_num)

    testing_word = input("Enter the word: ")
    test_list = []
    output = ""

    for letter in testing_word:
        test_list.append(letter.upper())

    for letter in test_list:
        output += str(new_list[letter])

    print(output)