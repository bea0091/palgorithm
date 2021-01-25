# Save the alarm informtaion
class Node:
    def __init__(self, title, time, timer, music):
        self.next = None
        self.prev = None
        self.title = title
        self.time = time
        self.timer = timer
        self.music = music

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.iterator = None
        self.length = 0

    def add_first(self, title, time, timer, music):
        new_node = Node(title, time, timer, music)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.length += 1

    def add_last(self, title, time, timer, music):
        new_node = Node(title, time, timer, music)
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

    def add_iterator(self, title, time, timer, music):
        if self.iterator is None:
            raise Exception("Iterator is null!")
        elif self.iterator == self.last:
            self.add_last(title, time, music)
        else:
            new_node = Node(title, time, music)
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

    def get_first_time(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.first.time

    def get_last_time(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.time

    def get_first_timer(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.first.timer

    def get_last_timer(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.timer

    def get_first_music(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.first.music

    def get_last_music(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.music

    def is_empty(self):
        return self.get_length() == 0

    def get_iterator_title(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get title.")
        return self.iterator.title

    def get_iterator_time(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get time.")
        return self.iterator.time

    def get_iterator_timer(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get timer.")
        return self.iterator.timer

    def get_iterator_music(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get link.")
        return self.iterator.music

    def off_end(self):
        return self.iterator is None

    def get_length(self):
        return self.length

    def print_numbered_list(self):
        temp = self.first
        num = 1
        while temp is not None:
            lists = "{}. name: " + temp.title + "\ntime: " + temp.time + "\nlink: " + temp.music
            print(lists.format(num).strip("\n"))
            temp = temp.next
            num += 1
