# clavdivs

We are given a simple string: ```MOIv/q.Z>\`n/mZH+m,opm,ZO.ZN/gpo\iox%``` with the hint `AVE CLAVDIVS!`.
To be quite honest, this challenge flew right over my head the first time. I initially tried just using
[cyberchef](https://gchq.github.io/CyberChef) but that lead nowhere (mostly thanks to me not playing with the settings enough).
So for a few days this challenge was unsolved for me, I got so desperate that I can't solve the easiest challenge in the CTF that I even asked for hints... yeah.

Turns out that I overcomplicated stuff (*as usual*), I tried to see if there was some XOR encryption going on, but no, it turned out to be a simple caesar cypher. After using an online tool (or we use [cyberchef with *the correct settings*](https://gchq.github.io/CyberChef/#recipe=ROT47(5)&input=TU9Jdi9xLlo%2BXGBuL21aSCttLG9wbSxaTy5aTi9ncG9caW94JQ), `ROT47` with amount set to `5`), we get the flag: `RTN{4v3_Caes4r_M0r1tur1_T3_S4lutant}`.
