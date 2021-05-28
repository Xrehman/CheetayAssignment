#Question no 4
#There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] 
#is start time of meeting i and F[i] is finish time of meeting i.
#What is the maximum number of meetings that can be accommodated in the meeting room when only one 
#meeting can be held in the meeting room at a particular time? Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

#Solution

class Maxmeet:
    def __init__(self, start, end, pos):

        self.start = start
        self.end = end
        self.pos = pos
def maxMeetings(s,f,n):
    
    pair = []
    for i in range(n):
        pair.append(Maxmeet(s[i], f[i], i))


    ans = []
    c = 1
    
    # Sorting of meetings
    pair.sort(key = lambda x: x.end)

    # First meeting always executed
    ans.append(pair[0].pos)


    prev_end = pair[0].end
    
    # Checkings of meetings
    for i in range(1, n):
        if pair[i].start > prev_end:
            ans.append(pair[i].pos)
            prev_end = pair[i].end
            c = c + 1

    print("output:",c)
   

    
    
s = [1,3,0,5,8,5 ]
f = [2,4,6,7,9,9 ]

n = len(s)

maxMeetings(s,f,n)
