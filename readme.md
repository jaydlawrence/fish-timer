# fish-timer
## A simple timer to control an energenie plug socket with a raspberry pi

### Install requirements
```
pip install -r requirements.txt
```

### Usage
#### Running the timer
Run the fish-timer.py file

It will turn the socket on for `ON_DURATION` and then turn it off for `OFF_DURATION` continuously
```
python fish-timer/fish-timer.py
```
#### Configuring different times
Edit the fish-timer.py file and change the `ON_DURATION` and `OFF_DURATION` constants to change how long the plug socket will be off or on.


#### keeping it running

I used supervisord to keep the file running with the following supervisor.conf entry:

```
...
[program:fish-timer]
command=/usr/bin/env python /home/pi/projects/fish-timer/fish-timer/fish-timer.py
```


Something like run-one would work well as well to keep it running reliably