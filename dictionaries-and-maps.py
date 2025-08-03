def solve():
    n = int(input())
    phone_book = {}
    for _ in range(n):
        name, phone_num = input().split()
        phone_book[name] = phone_num
    
    while True: 
        try:
            query = input()
            if query in phone_book:
                print(f"{query}={phone_book[query]}")
            else:
                print("Not found")
        except EOFError:
            break
solve()
