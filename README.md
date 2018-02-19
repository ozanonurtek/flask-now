# flask-now
A simple Flask Application Generator via CLI

## How to test
- clone this repo
- create a virtualenv using py3.x
- activate it
- ``` pip install . ``` Will install flask-now test purpose.
- ``` nano build.py ```
- write following to build.py and save it:
```

import flask_now
flask_now.build()

```
- then try it with your favorite extensions:
``` python3 build.py sqlalchemy wtf bootstrap frozen-flask restless ```

- it will automatically create a simple flask app, config file and requrements.txt for you.
- enjoy!
