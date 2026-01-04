1. Start
2. Set previousScore = -1
3. Set trend = "Stable"
4. For each score in StudentScores do
5.     If previousScore != -1 then
6.         If score > previousScore then
7.             trend = "Improving"
8.         Else if score < previousScore then
9.             trend = "Declining"
10.        Else
11.            trend = "Stable"     // if–else modification
12.        End If
13.    End If
14.    previousScore = score
15. End For
16. Display trend
17. End
