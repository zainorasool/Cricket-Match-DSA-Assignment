## Zaino Rasool
###                                        Cricket Match Database
##                                              Cricketers
class List_Node():
    def __init__(self,name):
        self.name = name
        self.next_reference = None


#Linked List to contain cricketer's names:
class Cricketer():

    def __init__(self):
        self.head = None

    def Add_Cricketer(self, name):        #deals with first insertion and insertion at the end
        if self.head is None:
            new_list_node = List_Node(name)   #first node object is created
            new_list_node.next_reference = self.head    #header's value becomes next value i.e. None
            self.head = new_list_node              #header start pointing to this new node
        else:                           #adds a new node to the end of the list, regardless of how many nodes
            last = self.head               # temp variable "last" holds header's value

            while last.next_reference:     #temp var runs from header towards end of the list
                last = last.next_reference

            new_list_node = List_Node(name)     #New node created
            last.next_reference = new_list_node   #last pointer's next reference becomes this new current node
            new_list_node.next_reference = None    #next is made none until new insertion

    def print_all_list(self):
        current_node = self.head
        while(current_node):
            print(current_node.name)
            current_node = current_node.next_reference

    def Delete_Cricketer(self, name):
        current_node = self.head
        previous_node = None

        if current_node is None:
            print("The list is empty.")
            return

        if current_node.name == name:       #node to be deleted is the head
            self.head = current_node.next_reference  # Move head to the next node
            current_node = None  # Free the old head
            return


        while current_node is not None:   # searching for the node to be deleted
            if current_node.name == name:
                break
            previous_node = current_node     #keeping track of the previous node to not lose that obviously
            current_node = current_node.next_reference


        if current_node is None:            #this case display if the node isnt found
            print(f"Cricketer named '{name}' not found in the list.")
            return

        # the node is unlinked from the list and the rest of the DCirkceter list isnt disturbed
        previous_node.next_reference = current_node.next_reference
        current_node = None  # Free the memory of the node


# cric1 = Cricketer()
# cric1.Add_Cricketer("Shaheen")
# cric1.Add_Cricketer("Babar")
# cric1.Add_Cricketer("Lala")
# cric1.Delete_Cricketer("Shaheen")
# cric1.print_all_list()
#

class Tree_Node():
    def __init__(self, match_id, First_Team, Second_Team, Match_date, Match_winner, Match_Location):
        self.match_id = match_id
        self.First_Team = Cricketer()
        self.Second_Team = Cricketer()
        self.Match_date = Match_date
        self.Match_winner = Match_winner
        self.Match_Location = Match_Location
        self.left = None
        self.right = None
        self.height = 1

class BST():
    def __init__(self):
        self.root_node = None

    def height_calculation(self, node):   #calculating height of the tree
        if node is None:
            return 0
        else:
            return node.height

    def balance_factor(self, node):      # using left-right formala for the calculation
        if node is None:
            return 0
        else:
            return self.height_calculation(node.left) - self.height_calculation(node.right)

    def right_rotation(self, y):
        x = y.left
        temp_subtree = x.right
        x.right = y
        y.left = temp_subtree
        y.height = 1 + max(self.height_calculation(y.left), self.height_calculation(y.right))
        x.height = 1 + max(self.height_calculation(x.left), self.height_calculation(x.right))
        return x

    def left_rotation(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height_calculation(x.left), self.height_calculation(x.right))
        y.height = 1 + max(self.height_calculation(y.left), self.height_calculation(y.right))
        return y

    def insersion_of_node(self, node, match_node):
        if node is None:
            return match_node
        if match_node.match_id < node.match_id:
            node.left = self.insersion_of_node(node.left, match_node)
        elif match_node.match_id > node.match_id:
            node.right = self.insersion_of_node(node.right, match_node)
        else:
            return node  # Duplicate match IDs are not allowed

        node.height = 1 + max(self.height_calculation(node.left), self.height_calculation(node.right))
        balance = self.balance_factor(node)

        # LL Rotation
        if balance > 1 and match_node.match_id < node.left.match_id:
            return self.right_rotation(node)
        # RR Rotation
        if balance < -1 and match_node.match_id > node.right.match_id:
            return self.left_rotation(node)
        # LR Rotation
        if balance > 1 and match_node.match_id > node.left.match_id:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        # RL Rotation
        if balance < -1 and match_node.match_id < node.right.match_id:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node

    def enter_new_match(self, match_id, First_Team, Second_Team, Match_date, Match_winner, Match_Location):
        match_node = Tree_Node(match_id, First_Team, Second_Team, Match_date, Match_winner, Match_Location)
        self.root_node = self.insersion_of_node(self.root_node, match_node)

    def search(self, node, match_id):
        if node is None or node.match_id == match_id:
            return node
        if match_id < node.match_id:
            return self.search(node.left, match_id)
        return self.search(node.right, match_id)

    def find_match(self, match_id):
        return self.search(self.root_node, match_id)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node)
            self.inorder_traversal(node.right, result)

    def print_inorder(self):
        result = []
        self.inorder_traversal(self.root_node, result)
        for match in result:
            print(f"Match ID: {match.match_id}, Date: {match.date}, Winner: {match.winner}, Location: {match.location}")

    def add_cricketer_to_match(self, match_id, team, cricketer_name):
        match = self.find_match(match_id)
        if match:
            if team == 1:
                match.team1.add_cricketer(cricketer_name)
            elif team == 2:
                match.team2.add_cricketer(cricketer_name)

    def delete_cricketer_from_match(self, match_id, team, cricketer_name):
        match = self.find_match(match_id)
        if match:
            if team == 1:
                self.delete_cricketer_from_list(match.First_Team, cricketer_name)
            elif team == 2:
                self.delete_cricketer_from_list(match.Second_Team, cricketer_name)
            else:
                print(f"Invalid team number {team}. Choose either 1 or 2.")
        else:
            print(f"Match with ID {match_id} not found.")

    def delete_cricketer_from_list(self, team, cricketer_name):
        current_node = team.head
        previous_node = None

        if current_node is None:
            print("The team has no cricketers.")
            return

        if current_node.name == cricketer_name:
            team.head = current_node.next_reference
            current_node = None
            return

        while current_node is not None:
            if current_node.name == cricketer_name:
                break
            previous_node = current_node
            current_node = current_node.next_reference

        if current_node is None:
            print(f"Cricketer named '{cricketer_name}' not found in the team.")
            return

        previous_node.next_reference = current_node.next_reference
        current_node = None

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_match(self, root, match_id):
        # Step 1: Perform standard BST delete
        if root is None:
            return root

        if match_id < root.match_id:
            root.left = self.delete_match(root.left, match_id)
        elif match_id > root.match_id:
            root.right = self.delete_match(root.right, match_id)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._min_value_node(root.right)
            root.match_id = temp.match_id
            root.First_Team = temp.First_Team
            root.Second_Team = temp.Second_Team
            root.Match_date = temp.Match_date
            root.Match_winner = temp.Match_winner
            root.Match_Location = temp.Match_Location
            root.right = self.delete_match(root.right, temp.match_id)

        if root is None:
            return root

        # Step 2: Update the height of the current node
        root.height = 1 + max(self.height_calculation(root.left), self.height_calculation(root.right))

        # Step 3: Get the balance factor and balance the tree
        balance = self.balance_factor(root)

        # Left Left Case
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotation(root)

        # Left Right Case
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        # Right Right Case
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotation(root)

        # Right Left Case
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root

    def remove_match(self, match_id):
        self.root_node = self.delete_match(self.root_node, match_id)






