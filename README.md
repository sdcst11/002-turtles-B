## SDSS Computing Studies Python Assignment
### Basic Code in Python with Turtle Graphics

Objectives:
* Describing Errors
* To create repeatable code
* To make use of variables to create copies in different locations

You may have found the constant figuring out left and right turns and moving forward quite challenging to visualize from the perspective of the turtle.  Often this can cause real problems if you turn the wrong way.

This results in an error from your planned code and presents an example of kinds of errors in programming:

### Sytax Error
You probably found that sometimes the program would stop working and "crash" with an error.  This could occur if you enter some of the following commands:
```
s = turtle.getScreen()  instead of s = turtle.getscreen()
t.forward(30            instead of t.forward(30)
t.forward()             instead of t.forward(20)
```
A syntax error is an error that is caused because the interpreter is expecting a specific format or specific amounts of data, but gets incorrect commands or missing data.
* Every bracket needs a closing bracket.
* Commands are case sensitive
* If a command is expecting some required data, it must get it or the program crashes.

### Semantic Errors
Sometimes your program would run, just fine, but your perfect picture of a shape was all messed up because lines were going in wrong directions. Technically, this is not an error, because the program is working just fine, following all of the instructions you gave it.  However, it is not behaving as you intended.  This is called a semantic error, and the only solution is to figure out what steps in your planning were incorrect, and make a better version.

We will see that the Visual Studio Code Debugger will be able to help us identify syntax errors, but only rigorous testing can help us find Semantic Errors.

## The goto(x,y) command
Instead of using forward and left/right, we can use absolute positions on a grid, much like using a cartesian coordinate system to draw lines between 2 points.  Open the file goto.py for an example.  You can copy the code into your own program to see how it works.

## Creating reusable code part 1
Create an image using reusable code using the goto(x,y) command.
Refer to your worksheet for helping you come up with the coordinates you need to find the relative positions of your coordinates.

## Creating reusable code part 2
Create another version of your same file using left/forward/right to make your shapes.  You will need to move your turtle to a new location prior to each shape.