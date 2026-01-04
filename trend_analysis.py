1. Start
2. Set previousScore = -1
3. Set trend = "Stable"
4. Set count = 0
5. For each score in StudentScores do
6.     count = count + 1        // loop modification
7.     If previousScore != -1 then
8.         If score > previousScore then
9.             trend = "Improving"
10.        Else
11.            trend = "Declining"
12.        End If
13.    End If
14.    previousScore = score
15. End For
16. Display trend
17. End

