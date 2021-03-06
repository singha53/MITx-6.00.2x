#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:12:37 2019

@author: asingh
"""

# =============================================================================
# Exercise 1-1
# 6/6 points (graded)
# For the following explanations of different types of programmatic models, fill in the blank with the appropriate model the definition describes.
# 
# A ______ model is one whose behavior is entirely predictable. Every set of variable states is uniquely determined by parameters in the model and by sets of previous states of these variables. Therefore, these models perform the same way for a given set of initial conditions, and it is possible to predict precisely what will happen.
# 
#  correct  deterministic
# A ________ model is one in which randomness is present, and variable states are not described by unique values, but rather by probability distributions. The behavior of this model cannot be entirely predicted.
# 
#  correct  stochasticv
# A _______ model does not account for the element of time. In this type of model, a simulation will give us a snapshot at a single point in time.
# 
#  correct  static
# A _______ model does account for the element of time. This type of model often contains state variables that change over time.
# 
#  correct  dynamic
# A _______ model does not take into account the function of time. The state variables change only at a countable number of points in time, abruptly from one state to another.
# 
#  correct  discrete
# A ______ model does take into account the function of time, typically by modelling a function f(t) and the changes reflected over time intervals. The state variables change in an unbroken way through an infinite number of states.
# 
#  correct  continuous
# =============================================================================

# =============================================================================
# Exercise 2
# 0.0/5.0 points (graded)
# This problem asks you to write a short function that uses the the random module. Click on the above link to be taken to the Python docs on the random module, where you can see all sorts of cool functions the module provides.
# 
# The random module has many useful functions - play around with them in your interpreter to see how much you can do! To test this code yourself, put the line import random at the top of your code file, to import all of the functions in the random module. To call random module methods, preface them with random., as in this sample interpreter session:
# 
# >>> import random
# >>> random.randint(1, 5)
# 4
# >>> random.choice(['apple', 'banana', 'cat'])
# 'cat'
# How would you randomly generate an even number x, 0 <= x < 100? Fill out the definition for the function genEven(). Please generate a uniform distribution over the even numbers between 0 and 100 (not including 100).
# 
# =============================================================================
import random

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return 10
    
# =============================================================================
# Exercise 3-1
# 0.0/5.0 points (graded)
# Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.
# 
# =============================================================================
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return random.randrange(8, 21, 2)
       
# =============================================================================
# Exercise 4
# 3/3 points (graded)
# Are the following two distributions equivalent?
# 
# import random
# def dist1():
#     return random.random() * 2 - 1
# 
# def dist2():
#     if random.random() > 0.5:
#         return random.random()
#     else:
#         return random.random() - 1 
# 
# Yes correct
# No
# Explanation:
# 
# The random.random() distribution is uniform, so both dist1 and dist2 are a uniform distribution over [-1.0, 1.0).
# 
# Are the following two distributions equivalent?
# 
# import random
# def dist3():
#     return int(random.random() * 10)
# 
# def dist4():
#     return random.randrange(0, 10)
# 
# Yes correct
# No
# Explanation:
# 
# The random.random() distribution is uniform, and so is the random.randrange() distribution, so both dist3 and dist4 are a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# 
# Are the following two distributions equivalent?
# 
# import random
# def dist5():
#     return int(random.random() * 10)
# 
# def dist6():
#     return random.randint(0, 10)
# 
# Yes
# No correct
# Explanation:
# 
# The random.random() distribution is uniform, and so is the random.randint() distribution. However unlike random.randrange(start, end), random.randint(start, end) returns a distribution that is inclusive of both the given start and end points.
# 
# Thus dist5 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], but dist6 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# 
# You can code a simple simulation to see what a distribution looks like using dictionaries:
# 
# d1 = {}
# for i in range(10000):
#     x = random.randrange(10) 
#     d1[x] = d1.get(x, 0) + 1
# d2 = {}
# for i in range(10000):
#     x = int(random.random()*10)
#     d2[x] = d2.get(x, 0) + 1
# d3 = {}
# for i in range(10000):
#     x = random.randint(0, 10)
#     d3[x] = d3.get(x, 0) + 1
# Examine the values of the three dictionaries to see what sort of distribution results!
# 
# Question to ponder: Should all the values of the dictionaries be equal? That is, should d1[x] == d1[y] for all values of x and y, where x != y and both x and y are values in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?    
#     
# =============================================================================
    
# =============================================================================
# Exercise 5
# 10/10 points (graded)
# In this problem, we're going to calculate some probabilities of dice rolls. Imagine you have two fair four-sided dice (if you've never seen one, here's a picture. The result, a number between 1 and 4, is displayed at the top of the die on each of the 3 visible sides). 'Fair' here means that there is equal probability of rolling any of the four numbers.
# 
# You can answer the following questions in one of two ways - you can calculate the probability directly, or, if you're having trouble, you can simply write out the entire sample space for the problem. A sample space is defined as a listing of all possible outcomes of a problem, and it can be written in many ways - a tree or a grid are popular options. For example, here is a diagram of the sample space for 3 coin tosses.
# 
# Some vocabulary before we begin: an event is a subset of the sample space, or, a collection of possible outcomes. A probability function assigns an event, A, a probability P(A) that represents the likelihood of event A occuring.
# 
# As an example, let's say we flip a coin. Define the event H as the event that the coin comes up heads. We can assign the probability P(H) = 1/2; the likelihood that event H occurs.
# 
# The following problems will ask for the probability that a given event occurs.
# 
# What is the size of the sample space for one roll of a four sided die?
# 
# 4
#   correct  4
# What is the size of the sample space for two rolls of a four sided die?
# 
# 16
#   correct  16
# Assume we roll 2 four sided dice. What is P({sum of the rolls is even})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/2
#   correct  1/2
# Assume we roll 2 four sided dice. What is P({rolling a 2 followed by a 3})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/16
#   correct  1/16
# Assume we roll 2 four sided dice. What is P({rolling a 2 and a 3, in any order})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/8
#   correct  1/8
# Assume we roll 2 four sided dice. What is P({sum of the rolls is odd})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/2
#   correct  1/2
# Assume we roll 2 four sided dice. What is P({first roll equal to second roll})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/4
#   correct  1/4
# Assume we roll 2 four sided dice. What is P({first roll larger than second roll})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 3/8
#   correct  3/8
# Assume we roll 2 four sided dice. What is P({at least one roll is equal to 4})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 7/16
#   correct  7/16
# Assume we roll 2 four sided dice. What is P({neither roll is equal to 4})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 9/16
#   correct  9/16
# Explanation:
# 
# Here is a visual representation of the sample space for 2 rolls of a four sided die. The left represents the 16 outcomes as a 2D grid; the right represents the outcomes as a tree, where each tree path represents one possible outcome.
# 
# 
# Each of the 16 outcomes in the sample space has equal probability (1/16) of occuring. So, for all of the above questions, you could simply use the visual representations to count up your answers. However, for large sample spaces this isn't feasible and it is instead better to be able to calculate the answers directly. So let's take a look at how to do that.
# 
# What is the size of the sample space for one roll of a four sided die? 4
# 
# What is the size of the sample space for two rolls of a four sided die? 4**2 = 16
# 
# P({sum of the rolls is even}) = 8/16 = 1/2
# 
# P({rolling a 2 followed by a 3}) = P({2, 3}) = 1/16
# 
# P({rolling a 2 and a 3}) = P({2, 3}) + P({3, 2}) = 1/16 + 1/16 = 2/16 = 1/8
# 
# P({sum of the rolls is odd}) = 8/16 = 1/2
# 
# P({first roll equal to second roll}) = P({both 1}) + P({both 2}) + P({both 3}) + P({both 4}) = 1/16 + 1/16 + 1/16 + 1/16 = 4/16 = 1/4. Another way of thinking about this is that it doesn't matter what the first roll is, just that the second roll matches it. So, the probability of that event is (4/4) * (1/4) = 1/4: 4/4 for the first roll (we don't care what it is), times 1/4 chance that the second roll matches the first roll.
# 
# P({first roll larger than second}) = P({4, <1, 2, 3>}) + P({3, <1, 2>}) + P({2, 1}) = 3/16 + 2/16 + 1/16 = 6/16 = 3/8
# 
# P({at least one roll equal to 4}) = P({4, <1, 2, 3>}) + P({<1, 2, 3>, 4}) + P({4, 4}) = 3/16 + 3/16 + 1/16= 7/16
# 
# P({nether roll is equal to 4}) = 1 - P({at least one roll equal to 4}) = 1 - 7/16 = 9/16
# 
# =============================================================================

# =============================================================================
# Exercise 6
# 12/13 points (graded)
# In this problem, we're going to calculate some various probabilities.
# 
# What is the size of the sample space for two rolls of a ten sided die?
# 
# 100
#   correct  100
# What is the size of the sample space for three rolls of an eight sided die?
# 
# 512
#   correct  512
# What is the size of the sample space for drawing one card from a deck of 52 cards?
# 
# 52
#   correct  52
# What is the size of the sample space for drawing one card from each of two decks of 52 cards? That is, drawing one card from one deck of cards, then a second card from a second deck of cards.
# 
# 2704
#   correct  2704
# Assume we roll 2 ten sided dice. What is P({rolling a 2 followed by a 3})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/100
#   correct  1/100
# Assume we roll 2 ten sided dice. What is P({first roll larger than second roll})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 9/20
#   correct  9/20
# Assume we roll 3 eight sided dice. What is P({all three rolls are equal})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/52
#   incorrect  1/64
# A standard deck of cards contains 52 cards, 13 each of four suits - diamonds, clubs, hearts, and spades. Each suit contains one of 13 cards: A (ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J (jack), Q (queen), K (king). Given one deck of 52 playing cards, you flip one over. Assuming a fair deck,what is P({ace of hearts})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/52
#   correct  1/52
# Given one deck of 52 playing cards, you flip one over. Assuming a fair deck, what is P({drawing a card with suit spades})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/4
#   correct  1/4
# Given one deck of 52 playing cards, you flip one over. Assuming a fair deck, what is P({ace of any suit})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/13
#   correct  1/13
# Given one deck of 52 playing cards, you flip one over. Assuming a fair deck, what is P({any card except an ace})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 12/13
#   correct  12/13
# Given one deck of 52 playing cards, you draw two random cards. (The cards are drawn at the same time, so the selection is considered without replacement) Assuming a fair deck, what is P({both cards are aces})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/221
#   correct  1/221
# Given two decks of 52 playing cards, you flip one over from each deck. Assuming fair decks, what is P({the two cards are the same suit})? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/4
#   correct  1/4
# Explanation:
# 
# What is the size of the sample space for two rolls of a ten sided die? 10**2 = 100
# What is the size of the sample space for three rolls of an eight sided die? 8**3 = 512
# What is the size of the sample space drawing from a deck of 52 cards? 52
# What is the size of the sample space drawing from two decks of 52 cards? 52**2 = 2704
# P({rolling a 2 followed by a 3}) = P({2, 3}) = 1/100
# P({first roll larger than second roll}) = P({10, <1, 2, 3, 4, 5, 6, 7, 8, 9>}) + P({9, <1, 2, 3, 4, 5, 6, 7, 8>}) + ... + P({2, 1}) = 9/100 + 8/100 + 7/100 + 6/100 + 5/100 + 4/100 + 3/100 + 2/100 + 1/100 = 45/100 = 9/20
# P({all three rolls are equal}) = P({all 1}) + P({all 2}) + ... + P({all 8}) = 1/512 + 1/512 + 1/512 + 1/512 + 1/512 + 1/512 + 1/512 + 1/512 = 8/512 = 1/64. Another way to think of it: it doesn't matter what the first roll is, but the second and third rolls must match the first roll. So the probability can be expressed as (8/8) * (1/8) * (1/8) = 1/64.
# P({ace of hearts}) = P({one card}) = 1/52
# P({drawing a card with suite spades}) = 13/52 = 1/4
# P({ace of any suit}) = P({ace of hearts}) + P({ace of clubs}) + P({ace of spaces}) P({ace of diamonds}) = 1/52 + 1/52 + 1/52 + 1/52 = 4/52 = 1/13
# P({any card except an ace}) = 1 - P({ace of any suit}) = 1 - 1/13 = 12/13
# P({both cards are aces}) = 4/52 * 3/51 = 12/2652 = 1/221. The probability of an ace is 4/52. On the second draw, if an ace was drawn the first time, there are only 3 aces left and only 51 cards remaining. Thus the probability that the second card is also an ace is 3/51.
# P({two cards are the same suit}) = This is an interesting problem. There are a few ways of calculating this, but a very simple way is to note that it doesn't matter what suit the first card is; what matters is that the second card's suit matches the suit of the first card. If the first card is a spade, there is a 13/52 = 1/4 chance the second card will also be a spade. Following this logic, you'll find that there's always a 1/4 chance the second card's suit will match the first card's suit, thus P({two cards are the same suit}) = 1/4.
# =============================================================================
