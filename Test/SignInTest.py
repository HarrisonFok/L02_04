import SignIn
import unittest

## You just gotta your read. WriteUserFile has been obsoleted by the ProfileIndex-s' functions. I forgot that.

class TestSignIn(unittest.TestCase):

  def TestreadUserFile():

  # How am I gonna test this without doing what the function is already doing?
  # ... Well, it's only noteworthy if it fails, so this is just a test that it hasn't changed...

    csv_file = open("TestUsers.csv", "a")
    writer = csv.writer(csv_file)
    writer.writerow([0] + ["s"]*4 + ["S"])
    writer.writerow([1] + ["p"]*4 + ["P"])
    csv_file.close()

    csv_file = open("TestUsers.csv", "r")
    Users = []
    lines = list(csv.reader(csv_file))
    for l in lines:
      if l[5] == "P":
        Users.append(Professor(l[1], l[2], l[3], l[4]))
      elif l[5] == "S":
        Users.append(Student(l[1], l[2], l[3], l[4]))
    csv_file.close()

    assertEqual(Users, readUserFile("TestUsers.csv"))

if __name__ == '__main__':
    unittest.main(exit=False)
