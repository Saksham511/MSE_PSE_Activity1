#importing class from different files

from cat import Cat
from dog import Dog

#create instance of classes
dog1= Dog("Sisimanu","chocolate roll","pug")        
cat1= Cat("kiyo","Fish","Turkish cat")

#see how the object of subclass overide the function of its superclass
dog1.speak()
cat1.speak()