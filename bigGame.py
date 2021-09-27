#
# Michael Salzarulo
#
# bigGame.py
#
# Mad lib game for user.
#

def main():

    print('Madlib Game ...')
    
    print('Enter the following words:')

    PNOUN1 = input("Plural Noun: ")
    FNAME = input("Person's First Name: ")
    NOUN1 = input("Noun: ")
    LNAME = input("Person's Last Name: ")
    PNOUN2 = input("Plural Noun: ")
    PLACE1 = input("Place: ")
    PNOUN3 = input("Plural Noun: ")
    PLACE2 = input("Place: ")
    PNOUN4 = input("Plural Noun: ")
    NOUN2 = input("Noun: ")
    ADJECTIVE1 = input("Adjective: ")
    ADJECTIVE2 = input("Adjective: ")
    VERB = input("Verb: ")
    ADJECTIVE3 = input("Adjective: ")

    print('The Big Game!!!')
    print('Hello there, sports', PNOUN1,
          '! This is', FNAME,', talking to you from the press', NOUN1,'in', LNAME,
          'Stadium, where 57,000 cheering', PNOUN2, 'Have gathered to watch (the)',
          PLACE1, PNOUN3, 'take on (the),', PLACE2, PNOUN4, '. Even though the', NOUN2,
          'is shining, its a/an', ADJECTIVE1, 'cool day with the temperature in the', ADJECTIVE2,
          '20s. Well be back for the opening', VERB,'-off after a few words from our', ADJECTIVE3,
          'sponsor.')

main()
