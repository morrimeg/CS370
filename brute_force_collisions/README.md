## Brute Force Collisions

Hash functions have two properties: weak collision and strong collision. This project was aimed at seeing how many trials on average it takes to find a collision with a hash function.  

### Weak Collision  

The property that must be satisified for weak collision to happen is: 

Given an arbitrary x there exists no x' with x' != x so that h(x) = h(x')


### Strong Collision

The property that must be satisified in order for strong collision to happen is:

There exist no x and x' with x != x' so that h(x) = h(x')



In this project, random strings were generated which satisfied both collision properties. An algorithm was run to determine how long it took to brute force break both the strong and weak collisoin properties of hash functions.  


**Running the Code:**

- To run the Python script, use the following command in the command line:  

    python3 brute_force_collisions.py
