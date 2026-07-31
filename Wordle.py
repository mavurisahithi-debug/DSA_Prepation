# Read the number of test cases
T = int(input())

for _ in range(T):
    S = input().strip()  # Hidden word
    T_word = input().strip()  # Guess word
    
    M = []
    for i in range(5):
        if S[i] == T_word[i]:
            M.append('G')
        else:
            M.append('B')
            
    print("".join(M))
