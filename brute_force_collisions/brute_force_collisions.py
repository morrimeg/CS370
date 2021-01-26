## Name: Megan Morrison
## Date: 10-13-2020
## Class: CS370
## Assignment: Programming Project 1, Problem 3.8
## Description: In this file are functions for breaking both
##              the weak collision resistance property as well as
##              the strong collision resistance property.

import hashlib
import string
import random

# below are a few sites I found helpful in explaining the difference between
# weak & strong collision resistance
# https://stackoverflow.com/questions/8523005/what-is-the-difference-between-weak-and-strong-resistance
# https://personal.utdallas.edu/~muratk/courses/crypto09s_files/hash.pdf

# I got the gist of the below code from here:
# https://pynative.com/python-generate-random-string/
def generate_random_string(str_length):
    """
    The generate_random_string function takes in the length of a string
    and then returns a random string of that length.
    """

    # Create what characters can be used in the string
    str_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random string
    rand_string = ''.join(random.choice(str_characters) for i in range(str_length))

    return rand_string



def generate_hash(string_1, string_2):
    """
        The function generate_hash takes in two strings
        and generates a hash value for each string. Both
        hash values are returned.
    """
    # Generate a hash for the known string, use SHA256
    generate_hash_1 = hashlib.sha256(string_1.encode())

    # Turn hash into a hex string
    hash_string_1 = generate_hash_1.hexdigest()

    # Generate a hash for the random string, use SHA256
    generate_hash_2 = hashlib.sha256(string_2.encode())

    # Turn hash into a hex string
    hash_string_2 = generate_hash_2.hexdigest()

    return hash_string_1, hash_string_2




def weak_collision_breaking():
    """
    The weak_collision_breaking function generates a known
    string and a random string. It then creates hashes
    based off of the two strings and sees if there is a
    match. It continues like this until there is a match.
    """
    # Weak Collision Resistance: Given an arbitrary x there exists no x' with x' != x so that h(x) = h(x')

    number_trials = 0 # variable to hold number of trials

    # Generate 1 random string of length 20 which is fixed for matching
    fixed_rand_str = generate_random_string(20)

    while True:
        # Generate a 2nd random strings of length 20
        non_fixed_rand_str = generate_random_string(20)

        # Make sure that the strings are not equal to each other
        if fixed_rand_str == non_fixed_rand_str:
            continue

        # Otherwise create hashes and see if the hash's match
        else:

            hash_string_1, hash_string_2 = generate_hash(fixed_rand_str, non_fixed_rand_str)

            # Keep adding to the number of trials
            number_trials += 1

            # If the 1st 24 bits of both has values are
            # the same, then break out of the while loop
            # as the hashes match
            if (hash_string_1[0:6] == hash_string_2[0:6]):
                break

    return number_trials



def strong_collision_breaking():
    """
    The function strong_collision_resistance generates two
    random strings. It then creates hashes
    based off of the two strings and sees if there is a
    match. It continues like this until there is a match.
    """
    # Strong Collision resistance: There exist no x and x' with x != x' so that h(x) = h(x')
    number_trials = 0 # variable to hold number of trials

    while True:
        # Generate 2 random strings of length 20
        rand_str_1 = generate_random_string(20)
        rand_str_2 = generate_random_string(20)

        # Make sure that the strings are not equal to each other
        if rand_str_1 == rand_str_2:
            continue

        # Otherwise create hashes and see if the hash's match
        else:

            rand_hash_string_1, rand_hash_string_2 = generate_hash(rand_str_1, rand_str_2)

            # Keep adding to the number of trials
            number_trials += 1

            # If the 1st 24 bits of both has values are
            # the same, then break out of the while loop
            # as the hashes match
            if (rand_hash_string_1[0:6] == rand_hash_string_2[0:6]):
                break

    return number_trials



def weak_collision_trials(max_number_of_trials):
    """
        The function weak_collision_trials takes in
        the number of trials to run in order to get an
        average for how many trials are needed to break
        weak collision resistance. It returns the
        average number of trials.
    """

    num_trials_weak_list = []  # list to hold number of trials

    # Iterate through the number of experiments
    for i in range(1, max_number_of_trials):
        # Call function to run weak collision
        num_trials_weak = weak_collision_breaking()

        # Append num_trials_weak to list to keep track
        num_trials_weak_list.append(num_trials_weak)

    # Take the average
    avg_num_trials_weak = sum(num_trials_weak_list) / len(num_trials_weak_list)

    return avg_num_trials_weak



def strong_collision_trials(max_number_of_trials):
    """
        The function strong_collision_trials takes in
        the number of trials to run in order to get an
        average for how many trials are needed to break
        strong collision resistance. It returns the
        average number of trials.
    """

    num_trials_strong_list = [] # list to hold number of trials

    # Iterate through the number of experiments for
    # strong collision
    for i in range(1, 20):
        # Call function to run strong collision
        num_trials_strong = strong_collision_breaking()

        # Append num_trials_weak to list to keep track
        num_trials_strong_list.append(num_trials_strong)

    # Take the average
    avg_num_trials_strong = sum(num_trials_strong_list) / len(num_trials_strong_list)

    return avg_num_trials_strong



def main():

    avg_weak_collision_trials = weak_collision_trials(20)
    avg_strong_collision_trials = strong_collision_trials(20)

    # Report the average for weak collision resistance
    print("Average number of trials to break weak-collision-resistant property = ", avg_weak_collision_trials)

    # Report the average for strong collision resistance
    print("Average number of trials to break strong-collision-resistant property = ", avg_strong_collision_trials)

main()