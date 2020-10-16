#!/usr/bin python3
from collections import OrderedDict
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 78.5
        self.SAFE_DISTANCE = 300
        self.CLOSE_DISTANCE = 150
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # check to see if it's safe before dancing
        if not self.safe_to_dance():
            return False # SHUT IT DOWN
            # THIS IS ThE GROVE 
        for d in range(2):
        # LOOPED IT SO MY DANCE CAN REACH THE REQUIRED TIME LIMIT
            self.dance1()
            self.dance2()
            self.dance3()
            self.dance4()
            self.move2()
            self.quinn_shuffle()
            self.roundround()
            self.sprinkler()
        self.wheelie()
        
       
 
 


    
   #for x in range(3):
            #self.shake()
            # call other dance moves

    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        # check for all fail/early-termiation conditions
        for x in range(4):
            if self.read_distance() < 300:
                print("NOT SAFE TO GROVE!")
                return False
            else:
                self.turn_by_deg(90)
        # after the checks have been done. We deduce it's safe
        print("01101111 01101011")
        return True



    #   FIRST DANCE (1/4)

    def dance1(self):
        """ This is the 1st part to a 4 move combo. This dance makes the robot drive in an L-shape to mock a slide"""
        # Very complex, but this is how I go the L to work.
        time.sleep(.2)
        self.fwd()
        # Going forward for a second
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        self.right()
        # Turning right for a second
        time.sleep(1)
        self.fwd()
        time.sleep(1)
        self.stop()
        time.sleep(.3)
        self.back()
        time.sleep(1)
        self.turn_by_deg(-90)
        # turning left for a second
        time.sleep(.1)
        self.back()
        # returning to start
        time.sleep(1)
        self.stop()
    
    # SECOND DANCE (2/4)

    def dance2(self):
        """ Second dance, Same move as dance1, just the other way"""
        # In order to make it go the other way I change its turning direction
        time.sleep(.2)
        self.fwd()
        # going forward for a second
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        self.left()
        # turning left for a second
        time.sleep(1)
        self.fwd()
        time.sleep(1)
        self.stop()
        time.sleep(.3)
        self.back()
        time.sleep(1)
        self.turn_by_deg(90)
        # turning right for a second
        time.sleep(.1)
        self.back()
        # returning to start position
        time.sleep(1)
        self.stop()

    # THRID DANCE (3/4)

    def dance3(self):
        """ Thrid dance Combo 3 of 4 same move as dance1, just backwords"""
        # This move is untested and I pray it works, created by changing the directions the robot heads in. Oppisite to dance1
        time.sleep(.2)
        # ^ Is here since the code wouldn't run without it
        self.back()
        # going backwards for a second
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        self.turn_by_deg(90)
        # turning right for a second
        time.sleep(1)
        self.fwd()
        time.sleep(1)
        self.stop()
        time.sleep(.3)
        self.back()
        time.sleep(1)
        self.turn_by_deg(-90)
        # turning left for a second
        time.sleep(.1)
        # returning to starting position
        self.back()
        time.sleep(1)
        self.stop()


    # FORTH DANCE (4/4)

    def dance4(self):
        """ Forth dance, The last combo move, same as dance2, just backwards instead of forwards"""
        # This is the last move of the four step-slide combo
        time.sleep(.2)
        self.back()
        # going backwards for a second
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        self.turn_by_deg(-90)
        # turning left for a second
        time.sleep(1)
        self.fwd()
        time.sleep(1)
        self.stop()
        time.sleep(.3)
        self.back()
        time.sleep(1)
        self.turn_by_deg(90)
        # turning to go back to start for a second
        time.sleep(.1)
        self.back()
        # returning to starting position
        time.sleep(1)
        self.stop()


    #FIFTH DANCE

    def move2(self):
        """Fitfh dance, it is a simple cha-cha slide, so fwds and back"""
        # May pop a wheelie due to change of battery placement

        for r in range(3):
            time.sleep(.1)
            self.fwd()
            time.sleep(.5)
            self.stop()
            time.sleep(.3)
            self.back()
            time.sleep(.5)
            self.stop()
            time.sleep(.3)
        
        self.stop()

    # SIXTH DANCE

    def quinn_shuffle(self):
        """ This dance was added to extend the dance, does a cool snake like slithering move"""
         # Code taken from Quinn via discord, thanks Quinn.
        for x in range(12):
            self.right(primary=-60, counter=0)
            time.sleep(.1)
            self.left(primary=-60, counter=0)
            time.sleep(.1)
        self.stop() 

        # SEVENTH DANCE

    def roundround(self):
        """ This dance is odd, just a spin with some head movements. He is trying his hardest ok"""
        # A last minute add in, but I think it will be cool
        for angle in range(4):
            self.turn_by_deg(90)
            self.servo(1000)
            self.servo(2000)
        self.servo(1500)
        self.stop()
        

    # EIGHT DANCE

    def sprinkler(self):
        """ As classic and simple as it gets. Make the head/neck of the robot move so it mocks the famous sprinkler move"""
        # Code taken from Mr.A on the Gilmour Discord
        for angle in range(1100, 2000, 50):
            self.servo(angle)
            time.sleep(.1)
            self.servo(angle-100)
            time.sleep(.1)
        self.servo(1100)
        for angles in range(1100, 2000, 50):
            self.servo(angles)
            time.sleep(.1)
            self.servo(angles-100)
            time.sleep(.1)
        self.servo(1500)
        self.stop()

    # NINTH DANCE

    def wheelie(self):
        """this is a wheelie move, it pops a quick backwards wheelie, is very rad """
        #taken from Friedman, thanks mate.
        for x in range(4):
            self.fwd(right=100, left=100)
            # causes the robot to tip making a wheelie
            time.sleep(.5)
            self.servo(1000)
            time.sleep(.1)
            self.servo(2000)
            time.sleep(.1)
            self.fwd(right=-100, left=-100)
            time.sleep(.1)
            self.servo(-1000)
            self.stop()
        self.stop()



    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 50):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()
        # sort the scan data for easier analysis
        self.scan_data = OrderedDict(sorted(self.scan_data.items()))


    def right_or_left(self):
        """ Should I turn right or left? Returns l or r depending on the scanned data"""
        self.scan()
        
        right_sum = 0
        right_avg = 0
        left_sum = 0
        left_avg = 0

        for angle in self.scan_data:
            # avg up the dist on the right side
            if angle < self.MIDPOINT:
                right_sum += self.scan_data[angle]
                right_avg += 1
            else:
                left_sum += self.scan_data[angle]
                left_avg += 1

        # calc avgs
        left_avg = left_sum / left_avg
        right_avg = right_sum / right_avg
        if left_avg > right_avg:
            return 'l'
        else:
            return 'r'

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        for s in range(4):
        # scan
            self.scan()
        # FIGURE OUT HOW MANY obejcts THERE WERE
            see_an_object = False
            count = 0

            for angle in self.scan_data:
                dist = self.scan_data[angle]
                if dist < self.SAFE_DISTANCE and not see_an_object:
                    see_an_object = True
                    count += 1
                    print("I see something")
                elif dist > self.SAFE_DISTANCE and see_an_object:
                    see_an_object = False
                    print("The object is no more")
                print("ANGLE %d | DIST: %d" % (angle,dist))
            self.turn_by_deg(90)
            print("\nI saw %d objects" % count)
    



        pass


    def quick_check(self):
        """ Moves the servo to three angles and preforms a distance check. """
        # loop three times and move the servo
        for ang in range(self.MIDPOINT - 100, self.MIDPOINT + 101, 100):
            self.servo(ang)
            time.sleep(.1)
            if self.read_distance() < self.SAFE_DISTANCE:
                return False
        # if the three part check didn't freak out
        return True


    def turn_until_clear(self):
        """ Rotate right until no obstacle is seen. """
        print("----turning until clear----")
        # make sure we are looking straight
        self.servo(self.MIDPOINT)
        # so long as we see something close, keep turning left
        while self.read_distance() < self.SAFE_DISTANCE:
            self.right(primary=40, counter=-40)
            time.sleep(.05)



        # stop motion before we end the method
        self.stop()

    


    def nav(self):
        """ Auto-pilot program """
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        exit_ang = self.get_heading()
        # because I've written down the exit angle, at any time I can use
        # self.turn_to_deg(exit_ang)
        turn_count = 0

        
        while True:
        # Basic/starting Code taught and created by Mr.A
        # I want to make a code that allows my robot to back out of any situation
        # so I started looking through other peoples code
        # work smarter not harder
        # I took some inspiration from a few people, thanks other people for having the same idea as me
            if not self.quick_check(): 
                turn_count += 1
                self.stop()
                # self.turn_until_clear()
                # turn count code taken from Parker Strauss and slightly modified by yours truly
                if turn_count > 3:
                    self.turn_by_deg(135)
                    self.turn_count = 0
                elif 'l' in self.right_or_left():
                    self.turn_by_deg(-45)
                else: 
                    self.turn_by_deg(45)
            else:
                self.fwd()





        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
