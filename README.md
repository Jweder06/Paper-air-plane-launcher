# Paper Airplane launcher

This was a relatively complex project that aimed to launch a paper air plane with a geared robotic arm.
## Planing

There was a thorough and set out plan which included drawings and a schedule.  this plan was used as a basis for all the work for the project and the drawings were fundamental to the creation of the onshape model. These drawings were made in Ms paint as a quick reference tool for when the CAD work needed to be completed. It was also used to explain our project to Mister H and to make a proof of concept that would help validate the initial idea.


### Here are some initial drawings

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a22f814b-a53b-4a0b-9ef8-88d4e8045bfc)

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/d1ba5a72-2022-4801-b321-48f045ee277f)

These were the initial drawings made in MS Paint they were used as reference points for onshape and Design and were overall simple summaries of the project. I do this for every project so I know what needs doing and what has been completed by referencing the image.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a8e4fefe-ad51-498b-afbc-188c744aa3a2)

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a8e4fefe-ad51-498b-afbc-188c744aa3a2" alt="Jakob Weder" width="500">
This this the drawing for the paper airplane holder which was worked by pushing a servo with a pad into an upright push pad which would clamp it down.

### Schedule

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/aa6812a5-25f6-440f-980c-f279e4d6cd4a)

There were many different issues with this project that didn't allow it to be completed this will be reviewed in the reflection.

## Cad

The cad was relatively difficult creating 1 part that could hold 3 gears and the top of the box together. The Complicated and compact part would hurt the construction process later. 

### Gears

![image](https://user-images.githubusercontent.com/112961442/234099095-6adc4385-2095-47c9-b666-65f3ca1e5cb2.png)

The gears were by far the most complicated part of the design process. It included two nut traps 3 interchanging gears a 1 arm mount. It was also heavily integrated meaning almost all of the moving parts interacted with one part. Later on, I would find out this was a mistake as a reprint or repair would require total disassembly. In onshape, I had the most difficulty creating the nut traps as I used a nut in the assembly context as a reference. When I finished this nut trap I constrained the part with a revolute mate, but when I updated the context the reference nut had rotated running my nut trap. I fixed this by un contexting the nut and fixing the relative sketch variables.

![image](https://user-images.githubusercontent.com/112961442/234100001-78696cd9-1386-4406-b197-9892231fd08b.png)

The nut trap was needed to connect the parallel gear and make sure that they were spinning in unison not fighting against each other.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/49b8b6ee-03f6-41b2-b1c9-904506accbc1)

Overall I should have scrapped most of the design but because I had become too invested in this design I had not scrapped it.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/9e04b531-347c-454f-b820-8ce5c71b38bf)

This is a battery pack holder that I made for my last project and now use as standard across all my projects. This is to speed up the design process and to make construction easier. I have also standardized my control panel and Arduino placement

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/dcb49d4c-6127-485a-a17d-aeec585e7870)

These are both of the gear lock shafts that were used to hold the gears in place. These had a lot of iterations and required lots of tweaking. The end caps where redone as well as the separating rings for a smoother fit. These also had a complete redesign that will be discussed in the construction portion.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/c9f1956c-1655-4802-812d-6ecd1b9c3af6)

This image represents a small change in my design process, the change is that I now import all bolts and nuts to make sure everything fits properly and is easily accessible for construction. This is especially useful when trying to make sure that bolts are long enough to reach certain nuts or to make sure they aren't interfering with any other part.

## Construction

### Arm construction

![IMG_0597 1](https://github.com/Jweder06/circuitpython-/assets/112961442/2ab5d763-eacb-4372-9f40-fa21383f205f)

The arm required a few redesigns and was one of the main issues within the project It changed from being held together by a makeshift tea slot into a miniature bracket that held the arm pieces onto the gear shaft. This was done because although it probably required a full redesign I was out of time and just needed something that worked. It did end up working better than expected and holds the arm in securely.
### Soldering

![IMG_0515 1](https://github.com/Jweder06/circuitpython-/assets/112961442/6ea91122-912c-4ff2-898e-a660f6a82223)

I hand-soldered all of the control panel components on the robot arm with resistors built into the LEDs for easier wiring and each component having color-coded wires.

### Integrated parts

![IMG_0500](https://github.com/Jweder06/circuitpython-/assets/112961442/8ff74daf-3286-4b34-b404-d6fdb89d55ad)

The integrated parts had a lot of issues the primary one being that to replace a part required almost total disassembly. There were a few benefits though, one being that because the holder was printed as one part no fit problems emerged with minute construction errors offsetting 

### End Caps

![images](https://github.com/Jweder06/Cad/assets/112961442/fbf0d0ce-a4a2-468d-aa35-59163645e635)

Originally the end caps didn't have a bolt hole and just a stopper, after printing I realized I couldn't have stoppers so I cut off the stoppers and drilled a bolt hole. Which ended up being u unnecessary because I needed a redesign anyway.
### Final fit and finish

![images](https://github.com/Jweder06/Cad/assets/112961442/fbf0d0ce-a4a2-468d-aa35-59163645e635)

The final fit was very good all the gears meshed together properly and all the walls fit perfectly. That is probably the only benefit of the integrated part system because each part is only constrained and affected by one part that is printed to perfect dimensions not constructed which can have some flaws. The wiring organization and planning were also good each wire had a place to go and pre-planned exit and entrance holes that led to the prototyping shield or the control panel.

## Wiring diagram

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/2a74da22-1ff5-4ffb-8fd5-e194c2efdd39)

This is a wiring diagram of what the wiring of the final circuit looks like.

## Code
```python
from time import sleep

while True:
    print("Hello World!") ##Prints "Hello World!" to the serial monitor
    sleep(1)
```
The code still needs some work and once the rest of the project is complete will be done.

## Reflection

This project had many different issues from the beginning I lacked the motivation and excitement I usually have for projects stifling my creative coding abilities that usually make great designs. I followed my usual design process but made a critical flaw in the beginning that cost me a lot of time later in the process redesigning and rebuilding flawed parts of the gearbox. This led me to fall behind and caused me to miss deadlines that further made it more difficult to catch up. In the future, my planning process will have to be more robust and I should also be able to identify a part that is no longer worth trying to fix and instead do a full redesign. I experienced this last year as well with my motor holder for my cyber truck after three attempts at fixing it  I scrapped it and made a part that worked the first time. I should have applied this lesson to this project as well. Finally, the most prominent issue was the lack of help from my partner who did not help with any of the documentation, CAD, Construction, code, or planning. I will take some blame for this because, after a few weeks of almost no help, I gave up trying to get him to do some work and just did it myself. 
