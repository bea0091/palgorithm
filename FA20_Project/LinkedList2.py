# Save the music information
class Node:
    def __init__(self, title, duration, link):
        self.next = None
        self.prev = None
        self.title = title
        self.duration = duration
        self.link = link

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.iterator = None
        self.length = 0

    def add_first(self, title, duration, link):
        new_node = Node(title, duration, link)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.length += 1

    def add_last(self, title, duration, link):
        new_node = Node(title, duration, link)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        self.length += 1

    def remove_first(self):
        if self.first is None:
            raise Exception("The list is empty!")
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            if self.iterator == self.first:
                self.iterator = None
            self.first = self.first.next
            self.first.prev = None
        self.length -= 1

    def remove_last(self):
        if self.first is None:
            raise Exception("The list is empty!")
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            if self.iterator == self.last:
                self.iterator = None
            self.last = self.last.prev
            self.last.next = None
        self.length -= 1

    def place_iterator(self):
        self.iterator = self.first

    def remove_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is already null!")
        elif self.iterator == self.first:
            self.remove_first()
        elif self.iterator == self.last:
            self.remove_last()
        else:
            self.iterator.prev.next = self.iterator.next
            self.iterator.next.prev = self.iterator.prev
            self.iterator = None
            self.length -= 1

    def add_iterator(self, track, duration, link):
        if self.iterator is None:
            raise Exception("Iterator is null!")
        elif self.iterator == self.last:
            self.add_last(track, duration, link)
        else:
            new_node = Node(track, duration, link)
            self.iterator.next.prev = new_node
            new_node.next = self.iterator.next
            self.iterator.next = new_node
            new_node.prev = self.iterator
        self.length += 1

    def advance_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is null")
        self.iterator = self.iterator.next

    def reverse_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is null")
        self.iterator = self.iterator.prev

    def get_first_title(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.first.title

    def get_last_title(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.title

    def get_first_duration(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.first.duration

    def get_last_duration(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.duration

    def get_first_link(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.first.link

    def get_last_link(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.link

    def is_empty(self):
        return self.get_length() == 0

    def get_iterator_title(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get title.")
        return self.iterator.title

    def get_iterator_duration(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get timer.")
        return self.iterator.duration

    def get_iterator_link(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get link.")
        return self.iterator.link

    def off_end(self):
        return self.iterator is None

    def get_length(self):
        return self.length

    def __str__(self):
        return self.title

    def print_numbered_list(self):
        temp = self.first
        num = 1
        while temp is not None:
            lists = "{}. title: " + temp.title + "\nduration: " + temp.duration + '\nurl: "' + temp.link
            print(lists.format(num).strip("\n") + '"\n')
            temp = temp.next
            num += 1

    def sortedDuration(self, a, b):
        result = None

        # Base cases
        if a == None:
            return b
        if b == None:
            return a

            # pick either a or b and recur..
        if a.duration <= b.duration:
            result = a
            result.next = self.sortedDuration(a.next, b)
        else:
            result = b
            result.next = self.sortedDuration(a, b.next)
        return result

    def mergeDuration(self, h):
        # Base case if head is None
        if h == None or h.next == None:
            return h

            # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.mergeDuration(h)

        # Apply mergeSort on right list
        right = self.mergeDuration(nexttomiddle)

        # Merge the left and right lists
        sortedlist = self.sortedDuration(left, right)
        return sortedlist

        # Utility function to get the middle
        # of the linked list


    def sortedTitle(self, a, b):
        result = None

        # Base cases
        if a == None:
            return b
        if b == None:
            return a

            # pick either a or b and recur..
        if a.title <= b.title:
            result = a
            result.next = self.sortedTitle(a.next, b)
        else:
            result = b
            result.next = self.sortedTitle(a, b.next)
        return result

    def mergeTitle(self, h):
        # Base case if head is None
        if h == None or h.next == None:
            return h

            # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.mergeTitle(h)

        # Apply mergeSort on right list
        right = self.mergeTitle(nexttomiddle)

        # Merge the left and right lists
        sortedlist = self.sortedTitle(left, right)
        return sortedlist

        # Utility function to get the middle
        # of the linked list

    def getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow
