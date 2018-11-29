# https://leetcode.com/problems/regular-expression-matching/
p = 'mis*is*ip*.'
a = '.*'
c = 'c*a*b'
d = 'a*a'

def map_pattern(pattern):
    p_len = len(pattern)
    star = False
    next_is_star = False
    a = {} # Initalize end index to point to Null
    for index in range(p_len-1,-1, -1 ):
        if pattern[index] != '*':
            if not a:
                a[index] = (None,) if not star else (index, None)
            else:
                if next_is_star:
                    val = a[index + 1] if not star else a[index + 2]
                else:
                    val = (index + 1,) if not star else (index + 2,)

                if star:
                    val = (index,) + val
                    star = False # reset star
                    next_is_star = True
                else:
                    next_is_star = False
                a[index] = val
        else:
            star = True
    return a

def is_match(s, pattern):
    mapping = map_pattern(pattern)
    current_p_index = 0
    if s[0] != pattern[0] and pattern[0] != '.':
        return False
    print("Map: ", mapping)
    # check = s[1]
    # print([pattern[i] for i in mapping[current_p_index]])
    can_end = False
    for char in s[1:]:
        try:
            # print([pattern[char] for char in mapping[current_p_index]
                #   if char is not None])
            if None in mapping[current_p_index] or None in mapping[max(mapping[current_p_index])]:
                can_end = True
            match = [pattern[char] for char in mapping[current_p_index]
                     if char is not None]
            # print(f'match: {match}, char: {char}')
            match_index = match.index(char)
            current_p_index = mapping[current_p_index][match_index]
            # print(current_p_index)
        except ValueError:
            if '.' in match:
                current_p_index = mapping[current_p_index][match.index('.')]
            else:
                return False
    if None not in mapping[current_p_index] and None not in mapping[max(mapping[current_p_index])]:
        # print("here")
        return False
    return True


# print(map_pattern(p))
# print(is_match("aaa", "a*a"))

def match(s, p):
    if not p: return not s
    matches = bool(s) and p[0] in [s[0], '.']
    return matches and match(s[1:], p[1:])

# print(match('abc', '..c'))
memo = {}
def match_kleene(st, pattern):
    # import pdb; pdb.set_trace()
    if (st, pattern) in memo:
        return memo[(st, pattern)]
    if not pattern: return not st
    matches = bool(st) and pattern[0] in [st[0], '.']

    if len(pattern) > 1 and pattern[1] == '*':
        # print(f'here, matches: {matches}')
        memo[(st, pattern)] = (matches and match_kleene(st[1:], pattern)) or (match_kleene(st, pattern[2:]))
    memo[(st, pattern)] = matches and match_kleene(st[1:], pattern[1:])
    return memo[(st, pattern)]

print(match_kleene("abc", "aa*bc"))