#!/usr/bin/env python

from rtm import createRTM
from rtm_helpers import *
import datetime
import sys

def stats(rtm):
    Today = iterLen(filterTasks(rtm, 'due:"today" status:incomplete'))
    Overdue = iterLen(filterTasks(rtm, 'dueBefore:"today" status:incomplete'))
    Scheduled = iterLen(filterTasks(rtm, 'dueAfter:"yesterday" status:incomplete'))
    Backlog = iterLen(filterTasks(rtm, 'list:backlog status:incomplete'))
    Review = iterLen(filterTasks(rtm, 'list:review status:incomplete'))
    postponed = list(filterTasks(rtm, 'postponed:">0" status:incomplete'))
    Postponed = len(postponed)
    MaxPostpones = maxPostpones(postponed)
    SumPostpones = sumPostpones(postponed)
    #print "date\ttime\tToday\tOverdue\tScheduled\tBacklog\tReview\tPostponed\tMaxPostpones\tSumPostpones"
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M') + "\t" + "\t".join(
        [ str(n) for n in (Today, Overdue, Scheduled, Backlog, Review, Postponed, MaxPostpones, SumPostpones) ]
        )

def test(apiKey, secret, token=None):
    rtm = createRTM(apiKey, secret, token)
    stats(rtm)

def main():
    try:
        api_key, secret = sys.argv[1:3]
    except ValueError:
        sys.stderr.write('Usage: '+sys.argv[0]+' APIKEY SECRET [TOKEN]\n')
    else:
        try:
            token = sys.argv[3]
        except IndexError:
            token = None
        test(api_key, secret, token)

if __name__ == '__main__':
    main()
