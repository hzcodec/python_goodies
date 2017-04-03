import fsm_A
import fsm_B
import events

if __name__ == "__main__":


    ev = events.Events()
    print ev.SKIP
    print ev.RUN
    print ev.STOP

    one = fsm_A.StateMachine_A()
    two = fsm_B.StateMachine_B()

    for i in range(0, 12):
        ev = one.go(ev)
	print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)
        ev = two.go(ev)
	print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)

    print 40*'-'

