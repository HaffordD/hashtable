1:The bad linear probing method used a hashing function that had modulo 37
it had 112224052 collisions, 0 wasted buckets, and took 11.96 second by title
it had 112221371 collisions, 0 wasted buckets, and took 11.99 seconds by quote

2:The better linear probing method used a hashing function that had modulo 3917
it had 89041447 collisions, 0 wasted buckets, and took 9.66 seconds by title  (had 1.2 times better collision rates comapred to bad)
it had 71807526 collisions, 0 wasted buckets, and tool 7.86 seconds by quote  (had 1.5 times better collision rates compared to bad)

3:The bad Linked list method used a hashing function that had modulo 37
it had 14963 collisions, 14963 wasted buckets, and took 0.05 seconds by title (had 0.00013 times the collisions compared to bad linear probing)
it had 14963 collisions, 14963 wasted buckets, and took 0.05 seconds by quote (funny coincidence)  (had 0.00013 times the collisions compared to bad linear probing)

4:The better linked list method used a hashing function that had modulo 3917
it had 11787 collisions, 11787 wasted buckets, and took 0.05 seconds by title   (had 0.78 times better collision rates comapred to the bad version)
it had 12281 collisions, 12281 wasted buckets, and took 0.06 seconds by quote   (had 0.82 times better collision rates comapred to the bad version)

5:The worst posible hashing function was for a linked list method with a hashing function that only returned 1
it had 14999 collisions, 14999 wasted buckets, and took 0.03 seconds by title   (had 1.2 worse collision rates compared to the good linked list method)
it had 14999 collisions, 14999 wasted buckets, and took 0.03 seconds by quote   (had 1.2 worse collision rates compared to the good linked list method)

 Discuss which methods were most effective and why
Of the methods, the linked lists were the most effective in terms of time and collisions, with the lowest time counts and the lowest number of collisions.
The linear probing was the most effective in terms of wasted buckets, with no buckets being wasted.