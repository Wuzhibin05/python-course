#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/3/16

# Practice Questions
# Q: 1. What is []?
print("这是一个空的列表，类似一个空的字符串，里面没有存任何值")
# Q: 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume
# spam contains [2, 4, 6, 8, 10].)
# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

# Q: 3. What does spam[int('3' * 2) / 11] evaluate to?
# Q: 4. What does spam[-1] evaluate to?
# Q: 5. What does spam[:2] evaluate to?
# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
# Q: 6. What does bacon.index('cat') evaluate to?
# Q: 7. What does bacon.append(99) make the list value in bacon look like?
# Q: 8. What does bacon.remove('cat') make the list value in bacon look like?
# Q: 9. What are the operators for list concatenation and list replication?
# Q: 10. What is the difference between the append() and insert() list methods?
# Q: 11. What are two ways to remove values from a list?
# Q: 12. Name a few ways that list values are similar to string values.
# Q: 13. What is the difference between lists and tuples?
# Q: 14. How do you type the tuple value that has just the integer value 42 in it?
# Q: 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
# Q: 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# Q: 17. What is the difference between copy.copy() and copy.deepcopy()?

# Practice Projects
# For practice, write programs to do the following tasks.
# Comma Code
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the
# items separated by a comma and a space, with and inserted before the last item. For
# example, passing the previous spam list to the function would return 'apples, bananas,
# tofu, and cats'. But your function should be able to work with any list value passed to
# it.

spam = ['apples', 'bananas', 'tofu', 'cats']
def transform(*args):
    for i in range(len(args)):
        ListStr = ', '.join(args[i])
    return  ListStr
ret=transform(spam)
print(ret,type(ret))


# Character Picture Grid
# Say you have a list of lists where each value in the inner lists is a one-character string, like
# this:
# grid = [['.', '.', '.', '.', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['.', 'O', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.']]
# You can think of grid[x][y] as being the character at the x- and y-coordinates of a
# “picture” drawn with text characters. The (0, 0) origin will be in the upper-left corner,
# the x-coordinates increase going right, and w the y-coordinates increase going down.
# Copy the previous grid value, and write code that uses it to print the image.
# ..OO.OO…OOOOOOO.
# .OOOOOOO…OOOOO…..OOO…
# ....O….
# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0],
# then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print
# a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2]
# [1], and so on. The last thing your program will print is grid[8][5].
# Also, remember to pass the end keyword argument to print() if you don’t want a newline
# printed automatically after each print() call.

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

row=0
count = 0
while True:
    if len(grid)>count:
        for i in range(len(grid)):
            if len(grid[i])>row:
                print(grid[i][row],end='')
        print('\n')
        row +=1
        count +=1
    else:
        break



