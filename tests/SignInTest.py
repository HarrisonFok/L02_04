import sys, inspect, os, csv
import unittest

 # script directory

sys.path.append("../src")

import SignIn, Professor, Student

class TestSignIn(unittest.TestCase):

  def test_readUserFile(self):
    '''If everything's coded right, this should never encounter an empty Users.csv, nor Users with missing values, so testing for any number of Users should be the same and so there's only 1 test.'''
    
    # Generating Testing-only version of Users.csv.
    
    # Not using CSV Writer, as it doesn't write lines, just writes everything on one line.
    
    csv_file = open("TestUsers.csv", "w")
    csv_file.write("0,s,s,s,s,S\n")
    csv_file.write("1,p,p,p,p,P\n")
    csv_file.close()

    Users = [Student.Student('0',"s", "s", "s", "s"), Professor.Professor('1',"p", "p", "p", "p")]

    U = SignIn.readUserFile("TestUsers.csv")

    s = set()

    # Just check against the known values.

    for i in range(len(U)):
      s.add(U[i].getName() == Users[i].getName())
      s.add(U[i].getEmail() == Users[i].getEmail())
      s.add(U[i].getPassword() == Users[i].getPassword())
      s.add(U[i].getPersonnelNumber() == Users[i].getPersonnelNumber())
      s.add(U[i].getType() == Users[i].getType())
      s.add(U[i].getId() == Users[i].getId())
      
    self.assertTrue(len(s) == 1)

if __name__ == '__main__':
    unittest.main(exit=False)
