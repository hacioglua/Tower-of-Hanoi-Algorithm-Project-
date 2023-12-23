# Tower of Hanoi Algorithm Project

This python program simulates the Tower of Hanoi algorithm using both recursive and iterative approaches. The graphical user interface is implemented with using Tkinter GUI library

## Tower of Hanoi Background

The Tower of Hanoi problem is a timeless challenge in computer science and mathematics, rooted in an ancient legend about a Hindu temple with three diamond pegs and 64 gold disks. This classic problem involves moving a stack of disks from one peg to another while adhering to specific rules: only one disk can be moved at a time, and a larger disk cannot be placed on top of a smaller one. The stack must be transferred from the source peg to the destination peg, using an auxiliary peg if necessary. Despite its seemingly simple rules, the Tower of Hanoi conceals a complexity that makes it an intriguing puzzle, requiring a deep understanding of recursive algorithms and intricate problem-solving strategies[this paragraph is taken directly from the report.]. 

## Instructions
    1. Run the program by executing the main.py file.

    2. Enter the number of disks in the entry window.

    3. Click the "Enter a disk value" button to start the simulation.

## GUI Components

* Entry Field: Enter the number of disks.
* Image Display: Tower of Hanoi image is displayed.
* Error Label: Displays error messages for invalid inputs if users will enter.
* Exit Button: Closes the input window and also program will close.
* Main Window: Displays the Tower of Hanoi simulation.
  * Restart Button: Restarts the simulation.
  * Exit Button: Closes the main program(GUI Part - Second).
  * Simulate Recursive Button: Simulates the Tower of Hanoi problem using a recursive approach.
  * Simulate Iterative Button: Simulates the Tower of Hanoi problem using an iterative approach.

## Algorithms

### Recursive Algorithm
The  algorithm is implemented using the classic Tower of Hanoi recursive solution. 

### Iterative Algorithm
The  algorithm uses a stack to keep track of the state of the towers. 

* NOTE: If you want to use iterative approach, all updates the GUI for each move until the entire disk_number is solved. In this step, program uses a stack to keep all steps. If you choose recursive algorithm simulation, this algorithm shows each move step by step.

## Runtime Calculation

* The programme calculates and displays all steps according to total numbers of disks and the programme displays runtime on console for both algorithm apporcahes.

#### Example outputs:

![](/screenshots_for_runtime/runtime-3.png)
![](/screenshots_for_runtime/runtime-4.png)
![](/screenshots_for_runtime/runtime-5.png)
![](/screenshots_for_runtime/runtime-6.png)
![](/screenshots_for_runtime/runtime-7.png)

### Example GUI for implemented with 3 disks.

![](/screenshots_for_disk3/disk3-round0.png)
![](/screenshots_for_disk3/disk3-round1.png)
![](/screenshots_for_disk3/disk3-round2.png)
![](/screenshots_for_disk3/disk3-round3.png)
![](/screenshots_for_disk3/disk3-round4.png)
![](/screenshots_for_disk3/disk3-round5.png)
![](/screenshots_for_disk3/disk3-round6.png)
![](/screenshots_for_disk3/disk3-round7.png)

## Important Notes

 * Please make sure to have the Tkinter library installed. 
 * Please be careful when you start to running code, you must enter the path of our mainImage in your computer before the starting running.

    
    The 15th line is the line to edit for this purpose.
    eg.
	    image = "path_of_mainImage"
* In this line, path_of_mainImage must be your local computer path.

Enjoy exploring the Tower of Hanoi simulation!
