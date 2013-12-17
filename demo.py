#!/usr/bin/env python

from rtm import createRTM
from rtm_helpers import *

def createApp(rtm):
    rspTasks = rtm.tasks.getList(filter='dueWithin:"1 week of today"')
    tasks = []
    if hasattr(rspTasks.tasks, "list") and \
       hasattr(rspTasks.tasks.list, "__getitem__"):
        for l in rspTasks.tasks.list:
            if isinstance(l.taskseries, (list, tuple)): # taskseries *may* be a list
                for t in l.taskseries:
                    tasks.append(t.name)
                    print "created => ", t.created
                    print "id => ", t.id
                    print "location_id => ", t.location_id
                    print "modified => ", t.modified
                    print "name => ", t.name
                    print "notes => ", t.notes
                    print "participants => ", t.participants
                    print "source => ", t.source
                    if t.tags:
                        if isinstance(t.tags.tag, (list, tuple)):
                            print "tags.tag[] => ", ", ".join(t.tags.tag)
                        else:
                            print "tags.tag => ", t.tags.tag
                    if t.task:
                        print "task.added => ", t.task.added
                        print "task.completed => ", t.task.completed
                        print "task.deleted => ", t.task.deleted
                        print "task.due => ", t.task.due
                        print "task.estimate => ", t.task.estimate
                        print "task.has_due_time => ", t.task.has_due_time
                        print "task.id => ", t.task.id
                        print "task.postponed => ", t.task.postponed
                        print "task.priority => ", t.task.priority
                    print "url => ", t.url
                    print ""
            else:
                tasks.append(l.taskseries.name)
    if not tasks:
        tasks.append('No tasks due within a week')


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
    import datetime
    print datetime.datetime.now().strftime('%Y-%m-%d') + "\t" + "\t".join(
        [ str(n) for n in (Today, Overdue, Scheduled, Backlog, Review, Postponed, MaxPostpones, SumPostpones) ]
        )

def test(apiKey, secret, token=None):
    rtm = createRTM(apiKey, secret, token)
    createApp(rtm)
    stats(rtm)

def main():
    import sys
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
