from itertools import permutations

def solve_cryptarithmetic():

    letters = 'SENDMOREMONEY'
    
    unique_letters = set(letters)
    
    if len(unique_letters) != 8:
        print("The number of unique letters is incorrect.")
        return

    for perm in permutations(range(10), 8):

        letter_to_digit = dict(zip(unique_letters, perm))

        send = int(''.join(str(letter_to_digit[char]) for char in 'SEND'))
        more = int(''.join(str(letter_to_digit[char]) for char in 'MORE'))
        money = int(''.join(str(letter_to_digit[char]) for char in 'MONEY'))

        if send + more == money:
            print("Solution found:")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            return

    print("No solution found.")

solve_cryptarithmetic()
