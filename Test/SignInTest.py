import sys, inspect, os, csv
import unittest

 # script directory
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))[:-5] + "/src")

sys.path.append("../src")

sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))[:-5] + "/src")

import SignIn, Professor, Student

## You just gotta your read. WriteUserFile has been obsoleted by the ProfileIndex-s' functions. I forgot that.

class TestSignIn(unittest.TestCase):

  def test_readUserFile(self):

  # How am I gonna test this without doing what the function is already doing?
  # ... Well, it's only noteworthy if it fails, so this is just a test that it hasn't changed...

    csv_file = open("TestUsers.csv", "a")
    writer = csv.writer(csv_file)
    writer.writerow([0] + ["s"]*4 + ["S"])
    writer.writerow([1] + ["p"]*4 + ["P"])
    csv_file.close()

    Users = [Student.Student("p", "p", "p", "p"), Professor.Professor("s", "s", "s", "s")]

    self.assertEqual(Users, SignIn.readUserFile("TestUsers.csv"))

if __name__ == '__main__':
    unittest.main(exit=False)
