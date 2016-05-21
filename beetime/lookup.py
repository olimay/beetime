from util import getDayStamp

def getDataPointId(col, goal_type, timestamp):
    """ Compare the cached dayStamp with the current one, return
    a tuple with as the first item the cached datapoint ID if
    the dayStamps match, otherwise None; the second item is
    a boolean indicating whether they match (and thus if we need
    to save the new ID and dayStamp.
    Disregard mention of the second item in the tuple.
    """
    if mw.col.conf[BEE]['overwrite'] and \
       mw.col.conf[BEE]['lastupload'] == getDayStamp(timestamp):
        return mw.col.conf[BEE]['did']
    else:
        return None

def formatComment(numberOfCards, reviewTime):
    # 2 lines ripped from the anki source
    msgp1 = ngettext("%d card", "%d cards", numberOfCards) % numberOfCards
    return comment = _("studied %(a)s in %(b)s") % dict(a=msgp1,
            b=fmtTimeSpan(reviewTime, unit=1))

def lookupReviewed(col):
    """Lookup the number of cards reviewed and the time spent reviewing them."""
    numberOfCards, reviewTime = col.db.first("""
select count(), sum(time)/1000 from revlog
where id > ?""", (col.sched.dayCutoff - 86400) * 1000)

    numberOfCards = numberOfCards or 0
    reviewTime = reviewTime or 0

    return (numberOfCards, reviewTime)

def lookupAdded():
    pass