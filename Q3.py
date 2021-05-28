#Question no 3
#Given a string S, find length of the longest substring with all distinct characters. 

#Solution
def longestSubstrDitinctChars(string):
      
    already_seen = {}
    l = 0
    s = 0  
    for e in range(len(string)):
        if string[e] in already_seen:
            s = max(s, already_seen[string[e]] + 1)
        already_seen[string[e]] = e
        l = max(l, e-s + 1)
    return l

string = "rehmanalihussnain"
length = longestSubstrDitinctChars(string)
print("output", length)
