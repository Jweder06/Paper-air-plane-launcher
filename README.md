# Paper Air plane launcher

This was a relatively complex project that aimed to launch a paper air plane with a geared robotic arm.
## Planing

There was a thorough and set out plan which included drawings and a schedule.  this plan was used as a basis for all the work for the project and the drawings were fundamental to the creation of the onshape model. These drawings were made in Ms paint as a quick reference tool for when the CAD work needed to be completed. It was also used to explain our project to Mister H and to make a proof of concept that would help validate the initial idea.


### Here are some inital drawings

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a22f814b-a53b-4a0b-9ef8-88d4e8045bfc)

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/d1ba5a72-2022-4801-b321-48f045ee277f)

These were the initial drawings made in MS Paint they were used as reference points for onshape and Design and were overall simple summaries of the project. I do this for every project so I know what needs doing and what has been completed by referencing the image.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/a8e4fefe-ad51-498b-afbc-188c744aa3a2)

This this the drawing for the paper air plane holder wich was worked by pushing a servo with a pad into a upright push pad wich would clamp it down.

### Schedule

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/aa6812a5-25f6-440f-980c-f279e4d6cd4a)

Their where manny diffrent issues with this project that dident allow it to be completed this will be revewed in the reflection.
## Cad

The cad was realtivly difucult creating 1 part that could hold 3 gears and the top of the box together. The Complicated and compact part that would hurt the consturction process later. 

### Gears

![image](https://user-images.githubusercontent.com/112961442/234099095-6adc4385-2095-47c9-b666-65f3ca1e5cb2.png)

The gears where by far the most complicated part of the design process. It included two nut traps 3 interchanging gears a 1 arm mount. It was also heavly intagrated meaning allmost all of the moving parts interacted with one part. Later on I would find out this was a mistake as a reprint or repair would require total disasembily. In onshape I had the most difucuty creating the nut traps as I used a nut in the assembily context as refrance. When I finished this nut trap I constrained the part with a revolute mate, but when I updated the context the refrence nut had rotated runining my nut trap. I fixed this by un contexting the nut and fixing the rlative skech variables.

![image](https://user-images.githubusercontent.com/112961442/234100001-78696cd9-1386-4406-b197-9892231fd08b.png)

The nut trap was needed to connect the paralell gear and make sure that they where spining in unison not figting against eachother.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/49b8b6ee-03f6-41b2-b1c9-904506accbc1)

Overall I should have scrapped most of the design but becasue I had became too invested in this design I had not scrapped it.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/9e04b531-347c-454f-b820-8ce5c71b38bf)

This is a battery pack holder that I made for my last project and now use as standaed across all my projects. This is to speed up the design process and to make construction easer. I have also standerdized my control panel and arduino placement

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/dcb49d4c-6127-485a-a17d-aeec585e7870)

These are both of the gear lock shafts that where used to hold the gears in place. These had a lot of iterations and required lots of tweaking. The end caps where redone aswell as the sperarting rings for a smother fit. These also had a complete redisgn that will be discused in the construction portion.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/c9f1956c-1655-4802-812d-6ecd1b9c3af6)

## Construction

### Arm construction

![IMG_0597 1](https://github.com/Jweder06/circuitpython-/assets/112961442/2ab5d763-eacb-4372-9f40-fa21383f205f)

### Soldering

![IMG_0515 1](https://github.com/Jweder06/circuitpython-/assets/112961442/6ea91122-912c-4ff2-898e-a660f6a82223)

### Interated parts

![IMG_0500](https://github.com/Jweder06/circuitpython-/assets/112961442/8ff74daf-3286-4b34-b404-d6fdb89d55ad)

The integrated parts had a lot of issues the primary one being that to replace a part required allmost total disasembily. There where a few benifits though, one being that becasue the holder was printed as one part no fit problems emerged with minute construction errors offseting 

### End Caps

### Final fit and finish


## Wiring diagram

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/2a74da22-1ff5-4ffb-8fd5-e194c2efdd39)

This is a wiring digram of what the wiring of the final circut would have looked like

## Code
```python
from time import sleep

while True:
    print("Hello World!") ##Prints "Hello World!" to the serial monitor
    sleep(1)
```
The code was verry limited and required and was verry bare bones.

## Reflection

This project had many diffrent issues from the begining i lacked motivation and excitemnt I usaly have for projects stifilig my creative cading abilities that usaly make great designs.
# partner
