# MtgChainer
Finds the longest chain of magic cards where the last name of card n is the first of card n+1


First off, huge shoutouts to reddit user u/LuridTeaParty for inspiring me to do this.

Second shoutouts to https://mtgjson.com/ for being the source for all magic card names. At time of writing, this list uses the names from the new Eldrained set.

## To Run
Just download all the files, and put them in the same folder. Then you can run the main.py and it will begin finding the longest list.


## Brief Description
### alphabetize.py.
What this does is it breaks down every card into the first and last word. Sorts them alphabetically, and then assigns each of them a number.

### cdm.py
This then turns the list of all cards into a huge graph. Then it iterates through every node, first looking for dead ends and condensing them down so that they won't be tested. Finally, it begins just running the depth first search. The output of this is illegible because it's still integers

### decypher.py
This just turns the numbers into words and double checks that all are valid cards.

### jsonreader.py
A quick addition that turned the data from mtgjson into a list of card names I could use.
