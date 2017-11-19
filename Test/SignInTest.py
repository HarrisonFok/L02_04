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

## Remember how your function works:

#def readUserFile(filename):
    #csv_file = open("Users.csv", "r")

    #Users = []

    #lines = list(csv.reader(csv_file)) # Represents file as List of Lists, first list is of rows, deeper list is of row contents.

    #for l in lines:

        ## Could make the user and email pair now, instead of doing it when making the object...

        #if l[5] == "P":
            #Users.append(Professor(l[1], l[2], l[3], l[4]))
        #elif l[5] == "S":
            #Users.append(Student(l[1], l[2], l[3], l[4]))

    #csv_file.close()
    ## Should set it so it returns 0 if the file isn't there, then report that to the user.

    #return Users


## Remember how to test:

#class TestBoundedQueue(unittest.TestCase):

    ##def size(self):
        ##"""Return the number of elements in this BoundedQueue.
        ##"""

    ##def is_empty(self):
        ##"""Return Boolean on whether this BoundedQueue is empty.
        ##"""

    ##def enqueue(self, item):
        ##"""Add the given item to the end of this BoundedQueue, if capacity
        ##permits. Otherwise, do nothing. You'd have to check what happened with a dequeue.
        ##"""

    ##def dequeue(self):
        ##"""Remove and return the first item in this BoundedQueue.
        ##Raises IndexError if called on an empty BoundedQueue.
        ##"""

    #def setUp(self):

        ## Negative capacity queues aren't supposed to happen.

        #self.bqe0Full = BoundedQueue(0) # Empty queue, or at least it should be...
        #self.bqe1Full = BoundedQueue(1,[1]) # Queue with 1 item, or at least it should be...
        #self.bqe2Full = BoundedQueue(2,[1, 2]) # Queue with 3 items, or at least it should be...
        #self.bqe3Full = BoundedQueue(3,[1, 2, 3]) # Queue with 3 items, or at least it should be...

        #self.bqeEmpt1 = BoundedQueue(1) # Empty with Queue Cap 1, or at least it should be...
        #self.bqeEmpt2 = BoundedQueue(2) # Empty with Queue Cap 2, or at least it should be...
        #self.bqeEmpt3 = BoundedQueue(3) # Empty with Queue Cap 3, or at least it should be...

    ## Negative capacity queues aren't supposed to happen.

    #def test_Size0QCap0Full(self):

        ##Testing that the size of the contents are 0 in a Full / Empty 0-capacity queue.

        #self.assertEqual(self.bqe0Full.size(), 0)

    #def test_EmptyQCap0Full(self):

        ##Testing that it reports it's empty, for a Full / Empty 0-capacity queue.

        #self.assertTrue(self.bqe0Full.is_empty())

    #def test_CannotDequeueQCap0Full(self):

        ##Testing that dequeues fail in a Full / Empty 0-capacity queue.

        #with self.assertRaises(IndexError):
            #self.bqe0Full.dequeue()

    #def test_CanAttemptEnqueueQCap0Full(self):

        ##Testing that you can at least try to enqueue in a Full / Empty 0-capacity queue.

        #self.bqe0Full.enqueue("item")

######### Capacity 1 Full Queue Testing starts here.

    #def test_Size1QCap1Full(self):

        ##Testing that the size of the contents are 1 in an initially Full 1-capacity queue.

        #self.assertEqual(self.bqe1Full.size(), 1)

    #def test_NotEmptyQCap1Full(self):

        ##Testing that the size of the contents are 1 in an initially Full 1-capacity queue.

        #self.assertFalse(self.bqe1Full.is_empty())

    #def test_CanAttemptEnqueueQCap1Full(self):

        ##Testing that you can at least try to enqueue in a Full / Empty 1-capacity queue.

        #self.bqe1Full.enqueue("item")

    #def test_CanDequeueQCap1Full(self):

        ##Testing that you can dequeue and you get the right object, in an initially Full 1-capacity queue.

        #self.assertEqual(self.bqe1Full.dequeue(), 1)

    ## Initial checks on size stop.

    ## Testing after 1 dequeue for Cap1Full.

    #def test_DequeuedQIsSize0Cap1Full(self):

        ##Testing that you can dequeue and the size becomes 0, in an initially Full 1-capacity queue..

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #self.assertEqual(bqe.size(), 0)

    #def test_DequeuedQIsEmptyCap1Full(self):

        ##Testing that you can dequeue and the queue is empty, in an initially Full 1-capacity queue..

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #self.assertTrue(bqe.is_empty())

    #def test_CannotDequeueTwiceQCap1Full(self):

        ##Testing that double dequeues fail, due to presumably an empty queue, in in an initially Full 1-capacity queue..

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #with self.assertRaises(IndexError):
            #bqe.dequeue()

    #def test_CanEnqueueWhenEmptyQCap1Full(self):

        ##Testing that a dequeued initially full 1-capacity queue, will be able to be enqueued.

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #bqe.enqueue("item")

    #def test_EnqueueWhenEmptyStoresProperlyQCap1Full(self):

        ##Testing that a dequeued initially full 1-capacity queue, will be able to be enqueued, and a second dequeue returns the correct item.

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #bqe.enqueue("item")
        #self.assertEqual(bqe.dequeue(), "item")

    #def test_EnqueueWhenEmptyIsSize1QCap1Full(self):

        ##Testing that you can dequeue and then enqueue, and you will have a size-1 queue, in an initially Full 1-capacity queue.

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #bqe.enqueue("item")
        #self.assertEqual(bqe.size(), 1)

    #def test_EnqueueWhenEmptyIsNotEmptyQCap1Full(self):

        ##Testing that a dequeued initially full 1-capacity queue, will report that it is empty.

        #bqe = self.bqe1Full
        #bqe.dequeue()
        #bqe.enqueue("item")
        #self.assertFalse(bqe.is_empty())

######### Full Capacity 2 Queue Starts Here.

    #def test_Size2QCap2Full(self):

        ##Testing that the size of the contents are 1 in a 1-capacity queue with those initialized size of contents.

        #bqe = self.bqe2Full
        #self.assertEqual(bqe.size(), 2)

    #def test_NotEmptyQCap2Full(self):

        ##Testing that the size of the contents are 1 in an initially Full 1-capacity queue.

        #bqe = self.bqe2Full
        #self.assertFalse(bqe.is_empty())

    #def test_CanAttemptEnqueueQCap2Full(self):

        ##Testing that you can at least try to enqueue in a Full / Empty 2-capacity queue.

        #bqe = self.bqe2Full
        #bqe.enqueue("item")

    ## Initial Size Checks for Cap2Full End Here

    ## Checks on Dequeue Once for same, start.

    #def test_CanDequeueOnceQCap2Full(self):

        ##Testing that you can dequeue once and you get the right object, in an initially Full 2-capacity queue.

        #bqe = self.bqe2Full
        #self.assertEqual(bqe.dequeue(), 1)

    #def test_DequeuedOnceQIsSize1Cap2Full(self):

        ##Testing that if you dequeue and you get a size of 1, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #self.assertEqual(bqe.size(), 1)

    #### Testing if enqueues work after 1 dequeue.

    #def test_DeQOnceEnQOnceQCap2Full(self):

        ##Testing that if you dequeue and enqueue with something, you get a size of 2, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.enqueue("test")

    #def test_DequeuedOnceEnQOnceNotEmptyQCap2Full(self):

        ##Testing that if you dequeue it's still not empty, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.enqueue("test")
        #self.assertFalse(bqe.is_empty())

    #def test_DeQOnceEnQOnceQIsSize2Cap2Full(self):

        ##Testing that if you dequeue and enqueue with something, you get a size of 2, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.enqueue("test")
        #self.assertEqual(bqe.size(), 2)

    #def test_DeQOnceEnQOnceDeQSecondCorrectCap2Full(self):

        ##Testing that if you dequeue and enqueue with something, you get a size of 2, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.enqueue("test")
        #self.assertEqual(bqe.dequeue(), 2)

    #def test_DequeuedOnceNotEmptyQCap2Full(self):

        ##Testing that if you dequeue it's still not empty, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #self.assertFalse(bqe.is_empty())

    #### Testing after dequeue twice.

    #def test_CanDequeueTwiceQCap2Full(self):

        ##Testing that you can dequeue once and you get the right object, in an initially Full 2-capacity queue.

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), 2)

    #def test_DequeuedTwiceQIsSize0Cap2Full(self):

        ##Testing that if you dequeue twice and you get a size of 0, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.dequeue()
        #self.assertEqual(bqe.size(), 0)

    #def test_DequeuedTwiceEmptyQCap2Full(self):

        ##Testing that if you dequeue twice, it's empty, in an initially Full 2-capacity queue..

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.dequeue()
        #self.assertTrue(bqe.is_empty())

    #def test_DequeuedTwiceEnqueueTwiceSameContentsEmptyQCap2Full(self):

        ##Testing that if you dequeue twice, you can enqueue twice, in an initially Full 2-capacity queue, and it'll be size 2. ... Not gonna test for all combos of de + re-queues... Soo tedious...

        #bqe = self.bqe2Full
        #bqe.dequeue()
        #bqe.dequeue()
        #bqe.enqueue("test")
        #bqe.enqueue("test")
        #self.assertEqual(bqe.size(), 2)

######### Full Capacity 3 Queue Starts Here.


    #def test_Size3QCap3Full(self):

        ##Testing that the size of the contents are 1 in a 1-capacity queue with those initialized size of contents.

        #bqe = self.bqe3Full
        #self.assertEqual(bqe.size(), 3)

    #def test_NotEmptyQCap3Full(self):

        ##Testing that the size of the contents are 1 in an initially Full 1-capacity queue.

        #bqe = self.bqe3Full
        #self.assertFalse(bqe.is_empty())

    #def test_CanAttemptEnqueueQCap3Full(self):

        ##Testing that you can at least try to enqueue in a Full / Empty 3-capacity queue.

        #bqe = self.bqe3Full
        #bqe.enqueue("item")

    ## Initial Size Checks for Cap3Full End Here

    ## Checks on Dequeue Once for same, start.

    #def test_CanDequeueOnceQCap3Full(self):

        ##Testing that you can dequeue once and you get the right object, in an initially Full 3-capacity queue.

        #bqe = self.bqe3Full
        #self.assertEqual(bqe.dequeue(), 1)

    #def test_DequeuedOnceQIsSize2Cap3Full(self):

        ##Testing that if you dequeue and you get a size of 2, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #self.assertEqual(bqe.size(), 2)

    #### Testing if enqueues work after 1 dequeue.

    #def test_DeQOnceEnQOnceQCap3Full(self):

        ##Testing that if you dequeue and enqueue with something, you get a size of 3, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.enqueue("test")

    #def test_DequeuedOnceEnQOnceNotEmptyQCap3Full(self):

        ##Testing that if you dequeue it's still not empty, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.enqueue("test")
        #self.assertFalse(bqe.is_empty())

    #def test_DeQOnceEnQOnceQIsSize3Cap3Full(self):

        ##Testing that if you dequeue and enqueue with something, you get a size of 3, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.enqueue("test")
        #self.assertEqual(bqe.size(), 3)

    #def test_DeQOnceEnQOnceDeQSecondCorrectCap3Full(self):

        ##Testing that if you dequeue and enqueue with something, you get a size of 3, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.enqueue("test")
        #self.assertEqual(bqe.dequeue(), 2)

    #def test_DequeuedOnceNotEmptyQCap3Full(self):

        ##Testing that if you dequeue it's still not empty, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #self.assertFalse(bqe.is_empty())

    #### Testing after dequeue twice.

    #def test_CanDequeueTwiceQCap3Full(self):

        ##Testing that you can dequeue once and you get the right object, in an initially Full 3-capacity queue.

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), 2)

    #def test_DequeuedTwiceQIsSize1Cap3Full(self):

        ##Testing that if you dequeue twice and you get a size of 1, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.dequeue()
        #self.assertEqual(bqe.size(), 1)

    #def test_DequeuedTwiceEmptyQCap3Full(self):

        ##Testing that if you dequeue twice, it's not empty, in an initially Full 3-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.dequeue()
        #self.assertFalse(bqe.is_empty())

    #def test_DequeuedTwiceEnqueueTwiceSameContentsEmptyQCap2Full(self):

        ##Testing that if you dequeue twice, you can enqueue twice, in an initially Full 3-capacity queue, and it'll be size 3. ... Not gonna test for all combos of de + re-queues... Soo tedious...

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.dequeue()
        #bqe.enqueue("test")
        #bqe.enqueue("test")
        #self.assertEqual(bqe.size(), 3)

    #def test_CanDequeueThriceQCap3Full(self):

        ##Testing that you can dequeue thrice and you get the right object, in an initially Full 3-capacity queue.

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), 3)

    #def test_CannotDequeueQuadQCap3Full(self):

        ##Testing that quadruple dequeues fail, due to presumably an empty queue, in in an initially Full 2-capacity queue..

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.dequeue()
        #bqe.dequeue()
        #with self.assertRaises(IndexError):
            #bqe.dequeue()

    #def test_CanDequeueTwiceQCap3Full(self):

        ##Testing that you can dequeue twice and you get the right object, in an initially Full 3-capacity queue.

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), 2)

    #def test_CanEnqueueWhenSize1QCap3Full(self):

        ##Testing that a twice dequeued initially full 3-capacity queue, will be able to be enqueued with 1 item.

        #bqe = self.bqe3Full
        #bqe.dequeue()
        #bqe.dequeue()
        #bqe.enqueue("item")

    #def test_EnqueueWhenEmptyMakesSize1QCap3Full(self):

        ##Testing that a emptied 3-capacity queue with those initialized size of contents, will report having a size of 1.

        #bqe = self.bqe3Full
        #for i in range(0,bqe.size()):
            #bqe.dequeue()
        #bqe.enqueue("item")
        #self.assertEqual(bqe.size(), 1)

######### OMG. Just use a variable to hold the size of the queue and adjust accordingly, instead?

######### Empty Queues start here.

######### Empty Queue 1 starts here.

    #def test_DequeueFullQSize1Empty(self):

        ##Testing that an empty Capacity 1 queue can't be dequeued.

        #bqe = self.bqeEmpt1
        #with self.assertRaises(IndexError):
            #bqe.dequeue()

    #def test_EnqueueFullQSize1Empty(self):

        ##Testing that an empty Capacity 1 queue can be enqueued.

        #bqe = self.bqeEmpt1
        #bqe.enqueue("item")

    #def test_EnThenDeQueueReturnsEnqueueQSize1Empty(self):

        ##Testing that en, then de, queues work.

        #bqe = self.bqeEmpt1
        #bqe.enqueue("item")
        #self.assertEqual(bqe.dequeue(), "item")

######### Empty Queue 2 starts here.

    #def test_DequeueFullQCap2Empty(self):

        ##Testing that an empty Capacity 2 queue can't be dequeued.

        #bqe = self.bqeEmpt2
        #with self.assertRaises(IndexError):
            #bqe.dequeue()

    #def test_EnqueueFullQSize2Empty(self):

        ##Testing that an empty Capacity 2 queue can be enqueued.

        #bqe = self.bqeEmpt2
        #bqe.enqueue("item")
        #bqe.enqueue("item2")

    #def test_EnThenDeQueueReturnsProperOrder1EnqueueQSize2Empty(self):

        #bqe = self.bqeEmpt2
        #bqe.enqueue("item")
        #bqe.enqueue("item2")
        #self.assertEqual(bqe.dequeue(), "item")

    #def test_EnThenDeQueueReturnsProperOrder2EnqueueQSize2Empty(self):

        #bqe = self.bqeEmpt2
        #bqe.enqueue("item")
        #bqe.enqueue("item2")
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), "item2")

######### Empty Queue 3 starts here.

    #def test_DequeueFullQCap3Empty(self):

        ##Testing that an empty Capacity 3 queue can't be dequeued.

        #bqe = self.bqeEmpt3
        #with self.assertRaises(IndexError):
            #bqe.dequeue()

    #def test_EnqueueFullQSize3Empty(self):

        ##Testing that an empty Capacity 3 queue can be enqueued.

        #bqe = self.bqeEmpt3
        #bqe.enqueue("item")
        #bqe.enqueue("item2")
        #bqe.enqueue("item3")

    #def test_EnThenDeQueueReturnsProperOrder1EnqueueQSize3Empty(self):

        #bqe = self.bqeEmpt3
        #bqe.enqueue("item")
        #self.assertEqual(bqe.dequeue(), "item")

    #def test_EnThenDeQueueReturnsProperOrder2EnqueueQSize3Empty(self):

        #bqe = self.bqeEmpt3
        #bqe.enqueue("item")
        #bqe.enqueue("item2")
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), "item2")

    #def test_EnThenDeQueueReturnsProperOrder3EnqueueQSize3Empty(self):

        #bqe = self.bqeEmpt3
        #bqe.enqueue("item")
        #bqe.enqueue("item2")
        #bqe.enqueue("item3")
        #bqe.dequeue()
        #bqe.dequeue()
        #self.assertEqual(bqe.dequeue(), "item3")

if __name__ == '__main__':
    unittest.main(exit=False)
