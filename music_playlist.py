class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # 1. Add song at beginning
    def add_beginning(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        print(song, "added at the beginning.")

    # 2. Add song at end
    def add_end(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
            print(song, "added at the end.")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print(song, "added at the end.")

    # 3. Insert song at specified position
    def insert_position(self, song, pos):
        if pos < 1:
            print("Invalid position.")
            return

        if pos == 1:
            self.add_beginning(song)
            return

        new_node = Node(song)
        temp = self.head
        count = 1

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position.")
            return

        new_node.next = temp.next
        temp.next = new_node
        print(song, "inserted at position", pos)

    # 4. Remove first song
    def remove_first(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print(self.head.data, "removed.")
        self.head = self.head.next

    # 5. Remove last song
    def remove_last(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        if self.head.next is None:
            print(self.head.data, "removed.")
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        print(temp.next.data, "removed.")
        temp.next = None

    # 6. Remove song at specified position
    def remove_position(self, pos):
        if self.head is None:
            print("Playlist is empty.")
            return

        if pos < 1:
            print("Invalid position.")
            return

        if pos == 1:
            self.remove_first()
            return

        temp = self.head
        count = 1

        while temp.next is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            print("Invalid position.")
            return

        print(temp.next.data, "removed from position", pos)
        temp.next = temp.next.next

    # 7. Search for a song
    def search(self, song):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == song:
                print(song, "found at position", pos)
                return

            temp = temp.next
            pos += 1

        print(song, "not found in the playlist.")

    # 8. Count total songs
    def count_songs(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Total number of songs:", count)

    # 9. Display playlist
    def display(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 10. Reverse playlist
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        print("Playlist reversed.")


# Main program
playlist = Playlist()

while True:
    print("\n===== MUSIC PLAYLIST MANAGER =====")
    print("1. Add song at beginning")
    print("2. Add song at end")
    print("3. Insert song at position")
    print("4. Remove first song")
    print("5. Remove last song")
    print("6. Remove song at position")
    print("7. Search for a song")
    print("8. Display total number of songs")
    print("9. Display complete playlist")
    print("10. Reverse playlist")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            song = input("Enter song name: ")
            playlist.add_beginning(song)

        case 2:
            song = input("Enter song name: ")
            playlist.add_end(song)

        case 3:
            song = input("Enter song name: ")
            pos = int(input("Enter position: "))
            playlist.insert_position(song, pos)

        case 4:
            playlist.remove_first()

        case 5:
            playlist.remove_last()

        case 6:
            pos = int(input("Enter position: "))
            playlist.remove_position(pos)

        case 7:
            song = input("Enter song name to search: ")
            playlist.search(song)

        case 8:
            playlist.count_songs()

        case 9:
            playlist.display()

        case 10:
            playlist.reverse()

        case 11:
            print("Exiting Music Playlist Manager...")
            break

        case _:
            print("Invalid choice. Please try again.")
