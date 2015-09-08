#!/usr/bin/env python2

from os.path import isfile

def op(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .op (op self on current chan) | .op nick (op nick on curent chan) | .op #chan (op self on #chan) | .op nick #chan OR .op #chan nick (op nick on #chan)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        nick = input.nick
        chan = input.sender
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            nick = input.nick
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = input.sender
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = splinput[1]
    if not input.sender.startswith("#"):
        phenny.say("OPing {} on {}".format(nick, chan))
    phenny.write(["OP", chan, nick])
op.commands = ['op']
op.priority = 'high'

def deop(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .deop (deop self on current chan) | .deop nick (deop nick on curent chan) | .deop #chan (deop self on #chan) | .deop nick #chan OR .deop #chan nick (deop nick on #chan)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        nick = input.nick
        chan = input.sender
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            nick = input.nick
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = input.sender
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = splinput[1]
    if not input.sender.startswith("#"):
        phenny.say("DEOPing {} on {}".format(nick, chan))
    phenny.write(["DEOP", chan, nick])
deop.commands = ['deop']
deop.priority = 'high'

def quiet(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .quiet nick (quiet nick on curent chan) | .quiet nick #chan OR .quiet #chan nick (quiet nick on #chan)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        return
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            return
        else:
            nick = splinput[0]
            chan = input.sender
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = splinput[1]
    if not input.sender.startswith("#"):
        #phenny.say("QUIETing {} on {}".format(nick, chan))
        pass
    phenny.msg("ChanServ", "quiet {} {}".format(chan, nick))
quiet.commands = ['quiet']
quiet.priority = 'high'

def unquiet(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .unquiet nick (unquiet nick on curent chan) | .unquiet nick #chan OR .unquiet #chan nick (unquiet nick on #chan)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        return
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            return
        else:
            nick = splinput[0]
            chan = input.sender
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = splinput[1]
    if not input.sender.startswith("#"):
        phenny.say("UNQUIETing {} on {}".format(nick, chan))
    phenny.msg("ChanServ", "unquiet {} {}".format(chan, nick))
unquiet.commands = ['unquiet']
unquiet.priority = 'high'

def voice(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .voice (voice self on current chan) | .voice nick (voice nick on curent chan) | .voice #chan (voice self on #chan) | .voice nick #chan OR .voice #chan nick (voice nick on #chan)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        nick = input.nick
        chan = input.sender
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            nick = input.nick
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = input.sender
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = splinput[1]
    if not input.sender.startswith("#"):
        phenny.say("VOICing {} on {}".format(nick, chan))
    phenny.write(["VOICE", chan, nick])
voice.commands = ['voice']
voice.priority = 'high'

def devoice(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .devoice (devoice self on current chan) | .devoice nick (devoice nick on curent chan) | .devoice #chan (dovoice self on #chan) | .devoice nick #chan OR .devoice #chan nick (devoice nick on #chan)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        nick = input.nick
        chan = input.sender
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            nick = input.nick
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = input.sender
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
        else:
            nick = splinput[0]
            chan = splinput[1]
    if not input.sender.startswith("#"):
        phenny.say("DEVOICing {} on {}".format(nick, chan))
    phenny.write(["DEVOICE", chan, nick])
devoice.commands = ['devoice']
devoice.priority = 'high'


def kick(phenny, input):
    splinput = input.split()[1:]
    if len(splinput) > 0:
        if splinput[0] == "help":
            phenny.say("Usage: .kick nick [reason] (kick nick on current chan for reason) | .kick nick #chan [reason] OR .kick #chan nick [reason] (kick nick on #chan for reason)")
            return
    if not isfile("bfs/%s" % (input.nick)):
        phenny.say("Must be admin.")
        return
    if len(splinput) == 0:
        return
    elif len(splinput) == 1:
        if splinput[0].startswith("#"):
            return
        else:
            nick = splinput[0]
            chan = input.sender
            reason = "no_reason"
    else:
        if splinput[0].startswith("#"):
            nick = splinput[1]
            chan = splinput[0]
            if len(splinput) > 2:
                reason = "_".join(splinput[2:])
            else:
                reason = "no_reason"
        elif splinput[1].startswith("#"):
            nick = splinput[0]
            chan = splinput[1]
            if len(splinput) > 2:
                reason = "_".join(splinput[2:])
            else:
                reason = "no_reason"
        else:
            nick = splinput[0]
            chan = input.sender
            reason = "_".join(splinput[1:])
    if not input.sender.startswith("#"):
        phenny.say("KICKing {} on {} for {}".format(nick, chan, reason))
    phenny.write(["KICK", chan, nick, reason])
kick.commands = ['kick']
kick.priority = 'high'
