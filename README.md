In this program, it is similar to Pets_OOP, in regards, to containing a parent class, 
instead of a constructor class, only because the User Class, as a parent class, is just
a simple class. Thus it would not need a function __init__ to construct arguments, that 
can be passed onto the inherited class. The reason for that, is that it is a judgment 
call and that the class confirms, if a player is signed in. The program is a simple game 
user input module, to test the way a game can function but, in Python programming mode.

From the parent class User, with the intent to create a program for game player input
as User, I created the Wizard and Archer class as an inherited class structure, passing 
on the User class as their argument. Initially, these inherited class, did need the __init__
function, to define additional attributes to the inherited class arguments. Thus each had 
the common factor of name attribute, with the difference being, that Wizard had the power
attribute and the Archer had a weaponlike attribute called arrows. 

The output for each are based on a concept known as Polymorphism. The idea that each class, 
in this case, inherited class would have same attributes such as name, but would behave
differently. They also have power, but Wizard has power and Archer arrows. What makes them 
polymorphic is that they are contained in an def attack(self) function. Both have this functon, 
but they behave differently. The ouptput for Wizard, Merlin is "attacking with a power of 60".
The output for GreenArrow is "attacking with arrows - 1000 arrows left". The outputs are defined
in terms of instantiating them.

The instantiation of the inherited class was initally from the variable format, as ussual and 
printing the output by using a for loop. The for loop was a technique I realized that made sense
from a solution from a Udemy course. However, this solution makes sense, as this is a simple game
output model response, with a wizard attacking an archer and an archer retaliating in return. 

An interesting error occured, when I was initally calling the class objects:
RecursionError: maximum recursion depth exceeded. This error was indicative of a mistake that I made 
when attack two attack methods. One from the parent class, to demosntrate, that polymorphically, I can
call parent function and child function, together. This error kept displayin. I chekced StackOverflow,
however, I realized where I made the mistake was that, as I added the attack function from the parent 
class, I ran User as the argument, instead of self and that I ran the respective inherited class in dot
notation to the attack() method, resulting in the error. Once I realized that, I ran the approriate
solution, by using the parent class User.attack(self) on both inherited class. When performing that 
correction, I was able to then get the appropriate outputs:

    do nothing
    attackin with power of 60
    do nothing
    attacking with arrows - 1000 arrows left.