def calculate_love_score(name1, name2):
    '''This function does the love calculation'''
    name_combined = name1 + name2
    true_letters =['T','R','U','E']
    love_letters =['L','O','V','E']

    #name_combined_length = len(name_combined)
    score1 = 0
    for letter in name_combined.upper():
        if letter in true_letters:
            score1 += 1
    score2 = 0
    for letter in name_combined.upper():
        if letter in love_letters:
            score2 += 1
    lovescore = str(score1)+str(score2)
    print(f"Your love score is {lovescore}")

def main():
    '''Take input - this is the main function'''
    name1 = input("Enter your name: ").strip().upper()
    name2 = input("Enter your lover's name: ").strip().upper()
    calculate_love_score(name1, name2)

if __name__ == "__main__":
    main()