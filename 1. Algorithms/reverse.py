
def reverse(n):
    n = str(n)
    ans = ""
    for i in range(len(n)-1, -1, -1):
        ans += n[i]
    return ans


num = 756
re_num = reverse(num)
print(re_num)
