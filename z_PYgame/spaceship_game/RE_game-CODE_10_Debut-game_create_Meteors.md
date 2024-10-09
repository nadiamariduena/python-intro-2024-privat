
 # 🟡 SPRITES 5.

 <br>

 ### Intro


 - - What **We’ll Be Doing:** [Go to section](#What_We_will_Be_Doing_)



 <!--


 #### 🟨 create the meteor class

 - - create the meteor class [Go to section](#create_class_)


 - - -  #### 🟨 create the event

 - - - - create the event to make the meteor appear [Go to section](#event_meteor_1_)

 <br>


  -->


 <br>
 <br>
 <br>
 <br>

 ---

 <br>


 # 🟡 What We will Be Doing

 <a name="What_We_will_Be_Doing_"></a>


 ## 🫐 🟡 Adding Meteor Rains to Our Space Shooter

 ### In this lesson, we will be focusing on adding meteors to our space shooter game.

 > -  ### Specifically, we will set up a system where meteors fall from the top of the screen, <u>creating obstacles for the player to avoid</u> 💥.

 <br>

 ### 🟤 This will involve using Python's random module, specifically the `range() and uniform()` functions, to control the position and speed of the meteors as they appear and move downwards.

 <br>

 ## 🟡 NEXT

 ###  After completing this lesson, we'll also be ready to tackle meteor collisions!

 - You'll learn how to detect when a meteor hits the player’s spaceship and how to handle those collisions (either) by taking damage or ending the game.

 ---

 <br>
 <br>
 <br>
 <br>
 <br>



 # 🟦 Let's Start:


 ## 🟡 Steps to Implement the *Key* LOGIC


 <a name="create_class_"></a>


 <br>

 ### 🟧 1. Create the 🪨METEOR  class

 ```python
 class Meteor(pygame.sprite.Sprite):
 ```

 ### 🟧 2.  Now Create a Meteor for Every Meteor event

 Here, we set up the `constructor` for the **Meteor** class.

 - In the next step We’ll pass all necessary **parameters** to define the meteor's behavior and appearance.

 ```python
 class Meteor(pygame.sprite.Sprite):
     def __init__(self, )
 ```


 <br>

 ### 🟧 3. Pass all the parameters



 ### 🟤 Parameters: (self, surf, pos, groups)


 These parameters will help us **specify** the meteor's **surface, position**, and the **sprite group it belongs** to.

 ```python
 #🪨 METEOR
 class Meteor(pygame.sprite.Sprite):
     def __init__(self, surf, pos, groups):
         super().__init__(groups)

         try:
             self.image = surf
 ```
 <br>
 <br>

 <br>

 ---

 ### ⚫ RECAP:

 ### 🍭 self:

 This refers to the current instance of the Player class.

 > - - ####  When you call `Laser(laser_surf, self.rect.midtop, all_sprites)`, self is implicitly passed when invoking methods from the Player instance.

 <br>


 ### 🍭 surf 🖼️

 This corresponds to laser_surf, which is the surface you want the Laser to use.

 > - - #### 🌞 It’s the image that you’ve loaded for the laser.


 <br>

 ### 🍭 pos:

 This is `self.rect.midtop`, which provides the position where the laser will be created.

 >  - - #### It uses the player’s current position (specifically the midpoint of the top edge of the player’s rectangle).


 <br>

 ### 🍭 groups:

 > - - #### This refers to all_sprites, which is the group you want the laser instance to be added to.

 - - This allows the laser to be part of the sprite management system for updates and drawing.


 <br>

 ### 🍭 pos:

 This is `self.rect.midtop`, which provides the position where the laser will be created.

 >  - - #### It uses the player’s current position (specifically the midpoint of the top edge of the player’s rectangle).


 <br>

 ### 🍭 groups:

 > - - #### This refers to all_sprites, which is the group you want the laser instance to be added to.

 - - This allows the laser to be part of the sprite management system for updates and drawing.

 ---

<br>
<br>
<br>

## 🟦 Moving Forward:

## 🟧 4.  Set the Image and Position

In this step, we set the**meteor's image** using the provided surface.

- - If the image **isn’t found, we create a fallback** surface. We also define the **position** of the meteor using its rectangle.

```python
#🪨 METEOR
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Meteor image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(center = pos)
        # meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
```


<br>
<br>
<br>

<a name="event_meteor_1_"></a>

## 🟧 5. Handle Meteor Events



### In this step, we listen for events in the game `loop`.

- - #### 🏁 When a `meteor_event` is triggered, we create a new `Meteor` instance using `meteor_surf`, specifying its position and adding it to the sprite group.

