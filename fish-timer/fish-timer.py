import sched, time
from energenie import switch_on, switch_off

ON_DURATION = 5 # * 60
OFF_DURATION = 10 # * 60




def fish_pump_on ():
    switch_on()
    print "Switching on"
    s = sched.scheduler(time.time, time.sleep)
    s.enter(ON_DURATION, 1, fish_pump_off, ())
    s.run()

def fish_pump_off ():
    switch_off()
    print "Switching off"
    s = sched.scheduler(time.time, time.sleep)
    s.enter(OFF_DURATION, 1, fish_pump_on, ())
    s.run()

fish_pump_on()