# Football Simulator
A football simulator coded in Python, just for fun! It is based on real data from the English leagues, and is based around the 05/06 season. It currently supports all 4 professionals tiers of the league and a cup competition, with built in functionality for all the main event in football (eg red cards, penalties, play-offs, penalty shoot outs etc). 

**It should be noted that this project is very much a work in progress and is therefore currently not formatted perfectly, optimised etc.**

## What does it do?
It is a functional football simulator that allows a season to evolve taking into account such things as the historic ability of a club, it's current 5-match form and an element of randomness (as football is based upon). Currently, only 1 season of the 4 major leagues in England can be simulated (along with a cup containing all the clubs), but the reglegation and promotion updater function is there (under construction, though near completion), so the simulation should easily be able to be extended to multiple seasons in the future. 

Upon running, a season will be started and simulate football matches until it will return at the end of the with table(s) detailing what happened (which can also be seen in the databases in more detail). That's it! 

## Install
The code is written in Pyton 2.7, and uses SQLite3 heavily to work its database system, as such an SQL database viewer such as "DB viewer for SQLite" is reccomended to view/edit the databases. Other than this, there should not be any other prerequistes to use this code. Currently, the database files are given as non-relative paths, which will need to be changed in order for the code to work for you. In addition, you will need those files specifically as they contain the data for grounds, crowds etc. All the season variables in those files are wiped at the beginning of a run.

## Change Log
N/A.

## License and Author Info
The project was created entirely from scratch by myself, Niall Mulkerns. FootballSim.py and its associated documents are available under the MIT License, see LICENSE.txt for more detials.
My email: nm13747@my.bristol.ac.uk

