t = int(input())
while t > 0:
    n = int(input())
    s = input()
    
    server = 'A'
    alice_score = 0
    bob_score = 0
    
    for ch in s:
        if ch == server:
            if server == 'A':
                alice_score += 1
            else:
                bob_score += 1
        else:
            server = ch  # The player who won the point becomes the new server
            
    print(f"{alice_score} {bob_score}")
    t -= 1
