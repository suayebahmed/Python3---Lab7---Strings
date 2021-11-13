# computes and returns the average word length in the string s
def avg_word_length(s):
    word_list = s.split()
    list_len = len(word_list)
    total_char = 0
    for word in word_list:
        total_char += len(word)
    avg_word = total_char / list_len
    return avg_word


# ignore ending chr that are not letters and return avg length
def avg_word_length_better(s):
    word_list = s.split()
    list_len = len(word_list)
    new_list = []
    for x in word_list:
        n = 1
        for i in range(len(x) - 1, -1, -1):
            if not x[i].isalpha():
                n += 1
            else:
                break
        x = x[:len(x) - n + 1]
        new_list.append(x)
    print(new_list)
    total_char = 0
    for word in new_list:
        total_char += len(word)
    avg_word_better = total_char / list_len
    return avg_word_better


# Taking input from the user for input s
user_input = input("Enter a string (X to exit): ")
# input X or x to exit; otherwise, show average word length and better version

while user_input != 'X' or user_input != 'x':
    if user_input == 'X' or user_input == 'x':
        print('Thanks, come back soon!')
        break
    else:
        print("Average word length:", avg_word_length(user_input))
        print("Average word length (better):", avg_word_length_better(user_input))
        user_input = input("Enter a string (X to exit): ")
        continue

