#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
flood.py - Phenny Flood Protection Module
No liscensing or copyright
COPYLEFT (ɔ)

https://github.com/archmint/phenny_modules/blob/master/flood.py
"""

from time import time

last = [] # last users (in past 10 secs)

def flood(phenny, input):
    """ Every message someone types, phenny will see here.
        If they flood (type six messages in ten seconds), he/she shall be kicked.
        Note: phenny can only kick if she is op.
        Note: you may want to change `phenny.write(['KICK', ...` to phenny.msg(['ChanServ', 'kick'], ...` so that phenny relies on ChanServ and not itself
    """
    splinput = input.encode("utf-8").split() # encode as utf... otherwise... uh-oh
    print u"[{}]({} on {}) {}".format(time(), input.nick, input.sender, input) # debug.. print everything ;)
    now = time()
    last.append((now, input.nick, input.sender)) # add (time, nick, channel) to last[]
    nicknum = dict() # keeps track of nick on chan with `nicknum["nick*chan"] ==> #`
    for ind, usr in enumerate(last): # enumerate last[]
        if now - usr[0] > 10: # if `now` -  `last[time]` > 10, delete it
            del last[ind]
        else: # `now` - `last` < 10 seconds
            if "{}*{}".format(usr[1], usr[2]) in nicknum: # check if `nick*chan` is in the nicknum{}
                nicknum["{}*{}".format(usr[1], usr[2])] += 1
            else: # `nick*chan` not in nicknum{}.. so add it at one
                nicknum["{}*{}".format(usr[1], usr[2])] = 1
    for nick in nicknum: # run through nicknum{}
        if nicknum[nick] >= 6: # nick said something more than 6 times (remember after 10 seconds, they are deleted, so this is 6 times in 10 seconds)
            spnick = nick.split('*') # split up nick into nick, chan
            phenny.write(['KICK', spnick[1], spnick[0], 'spam']) # kick them for spamming
            print 'kicking {} on {}'.format(spnick[0], spnick[1]) # tell 'em that you're kicking them
flood.rule = r'.*' # match everything
flood.priority = 'high'
