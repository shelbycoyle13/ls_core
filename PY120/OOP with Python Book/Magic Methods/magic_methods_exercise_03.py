#3. Challenge: Create the classes needed to make the following code work as shown:

# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = {
#     mike_jones,
#     susan_dore,
#     kim_waters,
# }

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()

#Output
# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes

# Don't worry about ties or whether votes should be singular.

class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        self.votes += other
        return self #self is always returns with augmented assignment customization
    
class Election:

    def __init__(self, group):
        self.group = group

    def results(self):
        max_votes = 0 #This refers to the top quantity of votes a single person has
        vote_count = 0 #This is the TOTAL vote count for the election
        winner = None #We don't know who the winner is yet, so we set it to None

        for candidate in candidates:
            vote_count += candidate.votes #This is calculating the total amount of election votes
            if candidate.votes > max_votes: #If a candidate has the greatest amount of votes
                max_votes = candidate.votes #The new max is equal to their amount of votes
                winner = candidate.name

        for candidate in candidates:
            name = candidate.name #Here we do initialize name so we can use this in the f-string. This isn't total necessary, it's done for conveniece and readability.
            votes = candidate.votes #Initializing votes so we can use in the f-string. Also done for readability.
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count) #max_votes refers to a single person's largest quantity of votes
        print()
        print(f"{winner} won: {percent}% of the votes")

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Output
# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes