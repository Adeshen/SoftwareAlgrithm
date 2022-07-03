

# 参考leetcode格式
# from asyncio.windows_events import NULL

def restoreIpAddresses( s):
    """
    :type s: str
    :rtype: List[str]
    """
    if(len(s)>12):   #四个点分位只能分出3*4=12
        return 0

   
    #核心思路是将三个点插入到一个字符串中，不能插在首位，只能插在中间
    
    #第一次尝试需要尝试三重循环，暴力法
    ans=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            for k in range(j+1,len(s)):
                ans.push(s[0:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:-1])
                print(s[i:j])
    
restoreIpAddresses("dsadaad")    