class Solutoin(object):
    def permuteString(self, string):
        if len(string) <= 1:
            return [string]
        temp = list(string)
        result = []
        for i, s in enumerate(temp):
            n = temp[:i] + temp[i+1:]
            for j in self.permuteString(n):
                result_string = s
                for k in j:
                    result_string += k
                result.append(result_string)
        return result

s= Solutoin()
print(s.permuteString('xian'))

        