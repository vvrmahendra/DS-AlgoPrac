"""To convert integer to english"""

def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "Zero" 
    def helper(a):
        ans = []
        if a//100:
            ans = ans+[dict_[a//100]]+["Hundred"]
            a = a%100
        # print(ans)
        if a <= 20 and a:
            ans = ans+[dict_[a]]
            a = 0
        if a:

            if a//10:
                ans = ans+[dict_[(a//10)*10]]
                a = a%10

            if a:
                ans = ans+[dict_[a]]

        return ans

    dict_ = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five',
            6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
            11:'Eleven', 12:'Twelve', 13:'Thirteen', 14: 'Fourteen', 15:'Fifteen',
            16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty',
            30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
            80:'Eighty', 90:'Ninety'}

    ans = []
    a = num
    if a//1000000000:
        temp = a//1000000000
        ans.extend(helper(temp))
        ans.append("Billion")
        a = a%1000000000

    if a//1000000:
        temp = a//1000000
        ans.extend(helper(temp))
        ans.append("Million")
        a = a%1000000

    if a//1000:
        temp = a//1000
        ans.extend(helper(temp))
        ans.append("Thousand")
        a = a%1000

    ans.extend(helper(a))

    return " ".join(ans)