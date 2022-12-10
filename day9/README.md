# Day 9 - rope_bridge

2022-12-09 07:42:55

This one looks fun.

2022-12-09 19:29:03

Got the first part done. This is one where it's not obvious how to update the existing code to account for the second part.

I used classes with a long list of possible actions by the head of the rope, and then what the tail should do in response.

Might be able to just make a multi-knoted rope class to inherit and include a new method to handle x knots, where each pair of knots is essentially a mini-rope.