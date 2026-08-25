"""
7868190130M7522

The first ten characters consist of the phone number of passengers.
- 7868190130

The next character denotes the gender of the person.
- M

The following two characters are used to indicate the age of the person.
- 75

The last two characters determine the seat allotted to that person.
- 22
"""

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for i in details:
            if int(i[11:13]) > 60:
                count+=1
        return count