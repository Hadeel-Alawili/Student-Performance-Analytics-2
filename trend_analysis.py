1. Start
2. Set previousScore = -1
3. Set trend = "Stable"
4. For each score in StudentScores do
5.     If previousScore != -1 then
6.         If score > previousScore then
7.             trend = "Improving"
8.         Else
9.             trend = "Declining"
10.        End If
11.    End If
12.    previousScore = score
13. End For
14. Display trend
15. End
