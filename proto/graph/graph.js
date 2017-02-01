/*
Basic dependency graph structure for visualization prototype.
Playing around with ways to represent satisfiability with pure JSON.
This will be useful for sending the backend model to the client for
rendering.

Authors: kurtvan, aratno
*/

/*
4: ((1 AND 2) OR 3)
*/
let nodes = {
    1 : [],
    2 : [],
    3 : [],
    4 : [[1, 2], 3],
    5 : [4],
    6 : [5, 3],
    9 : [[1, 2], 3, [5, 6]]
}

/*
nodes[9]    => join OR = [1, 2] OR 3 OR [5, 6]
            => apply AND = AND(1, 2) OR 3 OR AND(5, 6)
*/

/*
nodes[4]    => join OR = [1, 2] OR 3
            => apply AND = AND(1, 2) OR AND(3)
*/

/*
ASCII Graph~:

   1    2    3
    \  /   / |
     o    /  |
      \  /   |
       4     |
       \     |
        5   /
         \ /
         6
*/
