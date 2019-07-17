#solution one
# class Solution(object):
#     def replaceSpace(self, s):
#         return s.replace(" ", '20%')

#solution two
# import re
# pattern = re.compile(' ')
# pattern.sub('20%', ' a b ')

#solution three
class Solution(object):
    def replaceSpace(self, s):
        string = list(s)
        result = []
        for i in string:
            if i == ' ':
                result.append('2')
                result.append('0')
                result.append('%')
            else:
                result.append(i)
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    result = solution.replaceSpace(' a b ')
    print(result)
