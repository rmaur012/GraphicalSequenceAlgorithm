# GraphicalSequenceAlgorithm

This script implements the graphical sequence algorithm to detect whether a sequence of integers that signify the degrees of vertices in a graph could be graphical. Graphical means that one may be able to draw the graph that the sequence represents by connecting vertices such that you get the same degrees as in the sequence.

Example: Sequence = <2,2,2>
This sequence is graphical, so the graph could be made like so:

(1)---(3)
 |     |
(2)----|

To Run The Script:

1. Type "python GraphicalSequenceAlgorithm.py" once you have the file in the local directory.
2. Enter the number of vertices that will be part of the sequence.
3. Enter a degree one by one. Although the algorithm asks for the degrees to be sorted, this is also done in the code so the user may enter the degrees in any order. Once you have entered the degree that corresponds to the last vertex, the algorithm will run and produce a judgement on whether or not the sequence is graphical.

The code was done in Python to gain experience in the language and as a small challenge to implement the algorithm from graph theory.
