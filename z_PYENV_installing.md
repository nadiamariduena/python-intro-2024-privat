## 🟡 PYENV installing

<br>
<br>

### I encountered an issue when trying to run the code on the  [weather api](./z_weather-API.md)


```python
import requests
from dotenv import load_dotenv
#
import os
```

<br>

### Somehow i always ended up having the red underline on the `Weather.py`

<br>

- So i checked the requirements.txt of the project, and when I hovered under the dotenv (you will see 3 dots ) and the charset, I could see the below:

```javascript
Package `charset-normalizer` is not installed in the selected environment.Python-InstalledPackagesCheckernot-installed
//
//
Package `python-dotenv` is not installed in the selected environment.Python-InstalledPackagesCheckernot-installed

```