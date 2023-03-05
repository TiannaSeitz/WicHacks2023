**Welcome to TELL**
Created by: Tianna Seitz, Sunny Goodman, Lily Fiore, and Leanna Frasch

**What is TELL?**
Perhaps you are familiar with the concept of the Angel shot. Perhaps you are not. The uncertainty in your answer is a probelm, and the uncertainty in your date's answer is ALSO a problem. If you are spending your evening out on the town and someone is making you uncomfortable, it is not always practical or discrete to order an Angle shot (which is a codeword asking the bartender for one of three things: escord me to my car, call me a cab, or call the police.) 

We created TELL as a communication system to discretely ask for help from participating establishments. It is simply a bracelet with two buttons. All you have to do is: press button 1 to have the waitstaff walk you to our car, press button 2 to have the waitstaff call a cab or uber, press button 3 to have the waitstaff call the police. After pressing the button, the server will get a notification on their restaurant management system at the hostess station, or behind the bar and will be able to assist you.

**How we built it**
We built tell with a couple different techniques:
Hardware: the bracelet prototype was created with an Arduino and Raspberry Pi with C++ and Python respectively. Though we did not have the resources to mount the buttons on a bracelet, the functionality is there.
Functional Front End: The front end used in our hardware demo was created in Python with TKinter and PIL. When the buttons are pressed, it pulls up a sample profile of the user for the waitstaff with the appropriate call for help.
Front End Prototype: The front end prototype was built using Figma. It is storyboarded and can be viewed on a phone as if were a real app without the hardware functionality!

**What we learned**
We learned a lot. Our Front End team had never worked with Figma before and our Functional Front End team had to relearn TKinter and how to do integrate it with hardware.

We certainly had challenges. The inital attempt at hardware tried using an IR sensor to demonstrate remote capabilities, but the transmitter we used was broken. TKinter had trouble sharing variable between files. We solved this by creating three GUI windows and different oens are called depending on the help signal recieved from the Arduino.

**Next Steps:**
Our next steps are to clean up to code and implement better GUI techniques to make it more professional and start prototyping on an actual bracelet!
