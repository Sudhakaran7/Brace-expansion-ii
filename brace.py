class Solution2(object):
    def expand(self, S):  # nested is fine
        """
        :type S: str
        :rtype: List[str]
        """
        def form_words(options):
            words = []
            total = 1
            for opt in options:
                total *= len(opt)
            for i in range(total):
                tmp = []
                for opt in reversed(options):
                    i, c = divmod(i, len(opt))
                    tmp.append(opt[c])
                tmp.reverse()
                words.append("".join(tmp))
            words.sort()
            return words

        def generate_option(expr, i):
            option_set = set()
            while i[0] != len(expr) and expr[i[0]] != "}":
                i[0] += 1  # { or ,
                for option in generate_words(expr, i):
                    option_set.add(option)
            i[0] += 1  # }
            option = list(option_set)
            option.sort()
            return option

        def generate_words(expr, i):
            options = []
            while i[0] != len(expr) and expr[i[0]] not in ",}":
                tmp = []
                if expr[i[0]] not in "{,}":
                    tmp.append(expr[i[0]])
                    i[0] += 1  # a-z
                elif expr[i[0]] == "{":
                    tmp = generate_option(expr, i)
                options.append(tmp)
            return form_words(options)

        return generate_words(S, [0])

val=Solution2()
s=input()
print(*val.expand(s))
