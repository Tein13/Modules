# 1
'''def all_divisors(number):
    divisors = []


    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)'''


# 2
'''def three_args(*, var1=None, var2=None, var3=None):
    args = []
    
    
    if var1 is not None:
        args.append(f"var1 = {var1}")
    if var2 is not None:
        args.append(f"var2 = {var2}")
    if var3 is not None:
        args.append(f"var3 = {var3}")
    
    
    if args:
        print("Переданы аргументы:", ", ".join(args))'''


# 3
'''def palindromme(user_str):
    if user_str == user_str[::-1]:
        res = 'Число Палиндромное'
    else:
        res = 'Число не Палиндромное'
    return res'''


# 4
'''def most_common_string(text):
    words = text.lower().split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_frequent_word = ''
    max_count = 0
    for word, count in word_counts.items():
        if count > max_count:
            most_frequent_word = word
            max_count = count

    return most_frequent_word


def longest_word(text):
    very_long_word = ''
    for word in text.split():
        if len(word) > len(very_long_word):
            very_long_word = word
    return very_long_word'''