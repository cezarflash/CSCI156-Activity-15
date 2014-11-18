__author__ = 'Ayla'

import copy

#Part 1 Aliasing a Class

#Create a class named foo that has a class variable notagoodidea that is initialized to "what am I now?".
#Instantiate your class, and change the value of the instance variable notagoodidea to "who knows".
#Alias your class from part 2. Set the value of notagoodidea for the alias to "who's on first?".
#Print the value of the class and instance variables notagoodidea.

#Part 2 Copy a Class

#Make a copy of the first instance of foo that you created in
# 2. Change the value of the instance variable notagoodidea to "I'm lost".
#Print out all of the instance variables, the id for the instance variables, and the id for the instances as well as the
#class variable. What does this tell you about mutability?

class Foo:
    notagoodidea="what am I now?"

object1=Foo()
object1.notagoodidea = "who knows"
object2 = object1
object2.notagoodidea = "who's on first"
print(Foo.notagoodidea)
print(object1.notagoodidea)
print(object2.notagoodidea)

object3= copy.copy(object1)
object3.notagoodidea="I'm lost"
print(object3.notagoodidea)
print(id(Foo.notagoodidea))
print(id(object1.notagoodidea))
print(id(object2.notagoodidea))
print(id(object3.notagoodidea))






#alias
#x=2
#y=x








#import put at top

#class Foo:
    #pass
    #x='what am I now?'
#object1=Foo()
#object2=Foo()
#object1.x=1
#object2.x=2