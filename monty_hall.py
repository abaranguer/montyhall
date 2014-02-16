from random import *

class MontyHall():
    rand = None
    door = []
    first_selection = 0
    door_goat = 0
    new_user_selection = 0
    has_changed = 0
    has_won = 0
    
    def __init__(self):
        self.door = ["Car", "Car", "Car", "Car"]
    
        self.rand = Random()
        D1 = self.rand.randint(1,4)
        D2 = self.rand.randint(1,4)
		
        while( D1 == D2):
            D2 = self.rand.randint(1,4)
			
        self.door[D1-1] = "Goat"
        self.door[D2-1] = "Goat"

        #print "---------------------------"
        #print self.door

        # first user selection
        self.first_selection = self.rand.randint(1,4)
        #print "User selects door %d" % self.first_selection 

        # monty halls shows a goat
        for i in range(1,5):
            if (self.door[i-1] == "Goat") and (i != self.first_selection):
                self.door_goat = i
                break;

        #print "Monty Hall shows goat on door %d" % self.door_goat

                
        # user selects new door
        self.new_user_selection = self.rand.randint(1,4)
        while(self.new_user_selection == self.door_goat):
            self.new_user_selection = self.rand.randint(1,4)

        # has changed?
        if (self.new_user_selection != self.first_selection):
            self.has_changed = 1
            #print "User has changed from door %d to door %d" % (self.first_selection, self.new_user_selection)
        #else:
            #print "User has not changed and remains on door %d" % self.first_selection


        # User wins?
        #print "In door %d got a %s " % (self.new_user_selection, self.door[self.new_user_selection-1]) 
        if (self.door[self.new_user_selection-1] == "Car"):
            self.has_won = 1
            #print "User wins!"
        #else:
            #print "User loses!"

    def get_has_won(self):
        return self.has_won

    def get_has_changed(self):
        return self.has_changed;

    def show_new_user_selection(self):
        print self.new_user_selection

    def show_goat_door(self):
        print self.door_goat

    def show_first_selection(self):
        print self.first_selection
		
    def show(self):
        print self.door
		
# ---- main ----
num_experiments = 100000

for j in range(0, 10):

    count_changes = 0.0
    count_no_change_won = 0.0
    count_change_won = 0.0

    for i in range(1,num_experiments + 1):
        montyHall = MontyHall()
        count_changes = count_changes + montyHall.get_has_changed()
        if montyHall.get_has_changed() == 1:
            count_change_won = count_change_won + montyHall.get_has_won()
        else:
            count_no_change_won = count_no_change_won + montyHall.get_has_won()

    print "---------------------------"
    print "Totals:"
    print "Num. experiments: %d" % num_experiments
    print "Num changes: %d" % count_changes
    print "Num no changes: %d" % (num_experiments - count_changes)
    print "Num changes won: %d" % count_change_won
    print "Num no changes won: %d" % count_no_change_won
    print "Num changes won/Num changes = %f" % (count_change_won / count_changes)
    print "Num no changes won/Num no changes = %f" % (count_no_change_won / (num_experiments - count_changes))

