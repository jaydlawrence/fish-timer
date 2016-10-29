import sched, time
from energenie import switch_on, switch_off
from .logger import logger

ON_DURATION = 5 * 60 # 5 minutes
OFF_DURATION = 10 * 60 # 10 minutes



# turn fishpump on and then schedule it to turn off after ON_DURATION
def fish_pump_on ():
    switch_on()
    logger.info("Switching on")
    s = sched.scheduler(time.time, time.sleep)
    s.enter(ON_DURATION, 1, fish_pump_off, ())
    s.run()

# turn fishpump off and then schedule it to turn on after OFF_DURATION
def fish_pump_off ():
    switch_off()
    logger.info("Switching off")
    s = sched.scheduler(time.time, time.sleep)
    s.enter(OFF_DURATION, 1, fish_pump_on, ())
    s.run()

fish_pump_on()