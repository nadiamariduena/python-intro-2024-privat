## 🟡 Update and Update with arguments


 <br>
 <br>
 <br>


### 1. 👾 🟠 Now that we’ve created the Player class and added the group argument to its constructor, like this:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:
            # self.image = pygame.image.load(image_paths['player']).convert_alpha()
            self.image = images['player']
        except KeyError:
```
<br>

