Wine-Tasting-Puzzle
===================

This is a simple solution to the wine tasting puzzle.  In the wine tasting puzzle, there are X types of wine, and N people.  Each person has a set of preferred wine types.  The goal is to give as many bottles of wine out to the people, subject to the following constraints: <br />
	a) only one bottle of each type of wine may be given out <br />
	b) a person can only be given a bottle of wine of a type that is in the person's set of preferred wines <br />
	c) a person can only receive up to 3 bottles of wine <br />

The input data set is a tab-delimitted file with two columns.  For each row, the first column is a person's name, and the second column is a type of wine that is in the person's preferred wine set.

The output should be a tab-delimitted file.  The first line is the number of wines given out.  Subsequent lines contain two columns, where for each row, the first column has a person's name, and the second has a wine that this person received.

Example Datasets: <br />
https://s3.amazonaws.com/br-user/puzzles/person_wine_3.txt <br />
https://s3.amazonaws.com/br-user/puzzles/person_wine_4.txt.zip <br />
https://s3.amazonaws.com/br-user/puzzles/person_wine_5.txt.zip <br />