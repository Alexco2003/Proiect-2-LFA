# Proiect 2 LFA -> Regular Grammar
Regular Grammar

Implemented a Python algorithm that gets as input a Regular Grammar and a list of words and determines if the words are accepted or not. 

The Regular Grammar input file needs to have the following layout :

all the production rules

Example of input file (Regular Grammar):

S->aA | bB | lambda \
A->aS \
B->bC \
C->bD | b \
D->dB

Example of input file (the list of words that we want to check):


aa \
aaa \
bbb \
bb \
aabbb

Example of outputs :

Enter the Regular Grammar file name : grammar.txt \
Enter the file name that contains the words to check: words.txt \
The word '' is accepted by the grammar. \
The word 'aa' is accepted by the grammar. \
The word 'aaa' is not accepted by the grammar. \
The word 'bbb' is accepted by the grammar. \
The word 'bb' is not accepted by the grammar. \
The word 'aabbb' is accepted by the grammar. \


The algorithm was tested with the following examples to determine its correctness. All tests were successful.

![Screenshot_19](https://user-images.githubusercontent.com/105515716/230786352-cea1f7aa-0203-49ea-af84-3957201e514c.jpg)
