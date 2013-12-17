
from rtm import createRTM

def iterLen(iterable):
    return sum(1 for _ in iterable)

def sumPostpones(iterable):
    return sum(int(_.task.postponed) for _ in iterable if hasattr(_, 'task'))

def maxPostpones(iterable):
    return max(int(_.task.postponed) for _ in iterable if hasattr(_, 'task'))

def filterTasks(rtm, filterExpr, deleted=0):
    dottedlist = rtm.tasks.getList(filter=filterExpr)
    return iterTasks(rtm, dottedlist)
    # (not t.task.deleted or deleted):

def iterTasks(rtm, dottedlist):
    if hasattr(dottedlist.tasks, "list") and \
       hasattr(dottedlist.tasks.list, "__getitem__"):
        for l in dottedlist.tasks.list:
            if isinstance(l.taskseries, (list, tuple)): # taskseries *may* be a list
                for t in l.taskseries:
                    if t.task:
                        if isinstance(t.task, list):
                            for t2 in t.task:
                                yield t2
                        else:
                            yield t

