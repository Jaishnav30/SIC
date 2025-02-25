def check_order(boys, girls):
    order1 = []
    for i in range(len(boys)):
        order1.append(boys[i])
        order1.append(girls[i])
    
    order1_s = sorted(order1)
    
    order2 = []
    for i in range(len(boys)):
        order2.append(girls[i])
        order2.append(boys[i])
        
    order2_s = sorted(order2)
    
    if order1 == order1_s or order2 == order2_s:
        return "YES"
    return "NO"
    
test_cases = int(input())
    
result = []

for _ in range(test_cases):
    n = int(input())
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))
    val = check_order(b, g)
    result.append(val)
    
for i in result:
    print(i)
    