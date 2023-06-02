# Paper Airplane launcher

This was a relatively complex project that aimed to launch a paper air plane with a geared robotic arm.
## Planing

There was a thorough and set out plan which included drawings and a schedule.  this plan was used as a basis for all the work for the project and the drawings were fundamental to the creation of the onshape model. These drawings were made in Ms paint as a quick reference tool for when the CAD work needed to be completed. It was also used to explain our project to Mister H and to make a proof of concept that would help validate the initial idea.


### Here are some initial drawings

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a22f814b-a53b-4a0b-9ef8-88d4e8045bfc" width="500">


<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/d1ba5a72-2022-4801-b321-48f045ee277f" width="500">

These were the initial drawings made in MS Paint they were used as reference points for onshape and Design and were overall simple summaries of the project. I do this for every project so I know what needs doing and what has been completed by referencing the image.

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a8e4fefe-ad51-498b-afbc-188c744aa3a2" width="500">

This this the drawing for the paper airplane holder which was worked by pushing a servo with a pad into an upright push pad which would clamp it down.

### Schedule

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/aa6812a5-25f6-440f-980c-f279e4d6cd4a" width="500">

There were many different issues with this project that didn't allow it to be completed this will be reviewed in the reflection.

# Cad

The cad was relatively difficult creating 1 part that could hold 3 gears and the top of the box together. The Complicated and compact part would hurt the construction process later. 

### Gears

<img src="https://user-images.githubusercontent.com/112961442/234099095-6adc4385-2095-47c9-b666-65f3ca1e5cb2.png" width="500">

The gears were by far the most complicated part of the design process. It included two nut traps 3 interchanging gears a 1 arm mount. It was also heavily integrated meaning almost all of the moving parts interacted with one part. Later on, I would find out this was a mistake as a reprint or repair would require total disassembly. In onshape, I had the most difficulty creating the nut traps as I used a nut in the assembly context as a reference. When I finished this nut trap I constrained the part with a revolute mate, but when I updated the context the reference nut had rotated running my nut trap. I fixed this by un contexting the nut and fixing the relative sketch variables.

<img src="https://user-images.githubusercontent.com/112961442/234100001-78696cd9-1386-4406-b197-9892231fd08b.png" width="500">

The nut trap was needed to connect the parallel gear and make sure that they were spinning in unison not fighting against each other.


<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/49b8b6ee-03f6-41b2-b1c9-904506accbc1" width="500">

Overall I should have scrapped most of the design but because I had become too invested in this design I had not scrapped it.

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/9e04b531-347c-454f-b820-8ce5c71b38bf" width="500">

This is a battery pack holder that I made for my last project and now use as standard across all my projects. This is to speed up the design process and to make construction easier. I have also standardized my control panel and Arduino placement

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/dcb49d4c-6127-485a-a17d-aeec585e7870" width="500">

These are both of the gear lock shafts that were used to hold the gears in place. These had a lot of iterations and required lots of tweaking. The end caps where redone as well as the separating rings for a smoother fit. These also had a complete redesign that will be discussed in the construction portion.

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/c9f1956c-1655-4802-812d-6ecd1b9c3af6" width="500">

This image represents a small change in my design process, the change is that I now import all bolts and nuts to make sure everything fits properly and is easily accessible for construction. This is especially useful when trying to make sure that bolts are long enough to reach certain nuts or to make sure they aren't interfering with any other part.

# Construction

### Bill of materials

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/e4a19292-6f03-4b7e-aa82-578af97303e3" width="500">

### Arm construction

<img src="https://github.com/Jweder06/circuitpython-/assets/112961442/2ab5d763-eacb-4372-9f40-fa21383f205f" width="500">

The arm required a few redesigns and was one of the main issues within the project It changed from being held together by a makeshift tea slot into a miniature bracket that held the arm pieces onto the gear shaft. This was done because although it probably required a full redesign I was out of time and just needed something that worked. It did end up working better than expected and holds the arm in securely.

### Soldering

<img src="https://github.com/Jweder06/circuitpython-/assets/112961442/6ea91122-912c-4ff2-898e-a660f6a82223" width="500">
I hand-soldered all of the control panel components on the robot arm with resistors built into the LEDs for easier wiring and each component having color-coded wires.

### Integrated parts

<img src="https://github.com/Jweder06/circuitpython-/assets/112961442/8ff74daf-3286-4b34-b404-d6fdb89d55ad" width="500">

The integrated parts had a lot of issues the primary one being that to replace a part required almost total disassembly. There were a few benefits though, one being that because the holder was printed as one part no fit problems emerged with minute construction errors offsetting 

### End Caps

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/a5dcc0ca-2796-4d5c-b90e-ed8d3076a9c3" width="500">

Originally the end caps didn't have a bolt hole and just a stopper, after printing I realized I couldn't have stoppers so I cut off the stoppers and drilled a bolt hole. Which ended up being u unnecessary because I needed a redesign anyway.
### Final fit and finish

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/d09d7532-8e86-4464-9987-26ad0dd4dae9" width="500">

The final fit was very good all the gears meshed together properly and all the walls fit perfectly. That is probably the only benefit of the integrated part system because each part is only constrained and affected by one part that is printed to perfect dimensions not constructed which can have some flaws. The wiring organization and planning were also good each wire had a place to go and pre-planned exit and entrance holes that led to the prototyping shield or the control panel.

### Re-soldering the battery pack

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/28420353-beb7-475f-9839-a58cc8a9d88d" width="500">

I had to resolder the 5 volt wire on the 9 volt battery pack because the previous soldering job had ripped off and caused me a lot of confusion as I couldn't figure out why my power was missing.

### Wiring diagram

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/2a74da22-1ff5-4ffb-8fd5-e194c2efdd39" width="500">

This is a wiring diagram of what the wiring of the final circuit looks like.

# Code
```python
#type: ignore
from time import sleep
import time
import math
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import servo
buttonstate = "not pressed"
Servo1 = servo.Servo(pwmio.PWMOut(board.D1 , duty_cycle=2 ** 15, frequency=50))     #Servosetup
Servo2 = servo.Servo(pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50))
button = DigitalInOut(board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP
Bvalue = False
Presscount = 1
led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT
while True:
    if button.value == 0 and buttonstate == "not pressed":
        buttonstate = "pressed"     #Debounce
        Bvalue = True
        Presscount = Presscount + 1                  
    if button.value == 1:
        Bvalue = False
        buttonstate = "not pressed"     #Debounce
    if Bvalue == True and Presscount == 0:
        Servo2.angle = 0        #servos reset
        Servo1.angle = 180
        Presscount = 1
        led.value = True       #Power LED on  
    if Bvalue == True and Presscount == 1:
        led.value = False       #Power LED off    
        Presscount = 0
        Servo2.angle = 40
        Servo1.angle = 220      #servos move
```
The code was eaisy to make as it was very similar to the centrifuge code so I was able to copy some of the logic over.

## Final Product

Insert image here

The final product was almost functional The code and wiring were complete and so was the construction. The final issue was that the torque required was too high making it impossible to get the project to work. 

## Reflection

This project had many different issues from the beginning I lacked the motivation and excitement I usually have for projects stifling my creative coding abilities that usually make great designs. I followed my usual design process but made a critical flaw in the beginning that cost me a lot of time later in the process redesigning and rebuilding flawed parts of the gearbox. This led me to fall behind and caused me to miss deadlines that further made it more difficult to catch up. In the future, my planning process will have to be more robust and I should also be able to identify a part that is no longer worth trying to fix and instead do a full redesign. I experienced this last year as well with my motor holder for my cyber truck after three attempts at fixing it  I scrapped it and made a part that worked the first time. I should have applied this lesson to this project as well. Finally, the most prominent issue was the lack of help from my partner who did not help with any of the documentation, CAD, Construction, code, or planning. I will take some blame for this because, after a few weeks of almost no help, I gave up trying to get him to do some work and just did it myself. 
