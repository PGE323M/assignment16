# Homework Assignment 16

![Assignment 16](https://github.com/PGE323M/assignment16-solution/workflows/.github/workflows/main.yml/badge.svg)


## Instructions

The [Simple 2D Problem in CMG](https://youtu.be/Tx1l-dQO5TA) was also the exact problem we wrote our own Python code for in [Assignment 15](https://github.com/PGE323M/assignment15/blob/master/assignment15.ipynb).   Recall the problem schematic

![image](images/grid.png)

Work through the [tutorial](https://youtu.be/Tx1l-dQO5TA) and import your results into CMG's Resultsapplication.  From there, export the pressures as shown in the tutorial (from the [3 3 3] gridblock).
Save the exported results to a *CSV file* `assignment16.csv`.  Copy this file into this repository, add, commit, and push to Github for submission.

**Note:**
There is one additional step not referenced in the video.  When editing the input file manually, after changing the grid from 1d to 2d and adjusting the permeabilities as shown in the video, you will also need to change the lines

```
DTOP
5*1000
```

to

```
DTOP
12*1000
```

because there are 12 grid blocks now.

## Testing

If you would like to check to see if your solution is correct, run the following command at the Terminal command line:

```bash
python test.py
```

a status message of `OK` indicates you have the correct solution.
