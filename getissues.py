# -*- coding: utf-8 -*-
#! /usr/bin/env python
import github3
#gh = github3.login("sdrgroup@sina.com", "Ajgithub123")
owner="IQAndreas"
rep="github-issues-import"
theNumber=29
repo=github3.repository(owner,rep)

if repo.has_issues:
    print "There are some issues in ",rep
    iss=repo.issues(state="closed")
    i = github3.issue(owner, rep, theNumber)
    print "the 513 issue's body is", i.body,"\n"
    print  "the 513 issue's closed at",i.closed_at,"\n"
    print  "the 513 issue's closed by",i.closed_by,"\n"
#    print  "the 513 issue's comments is ",i.comments(),"\n"
#    print  "the 513 issue's comment is ",i.comment(513),"\n"
    print  "the 513 issue's created at ",i.created_at,"\n"
    print  "the 513 issue's id ",i.id,"\n"
    print "the 513 issue is closed? ",i.is_closed(),"\n"
#   print "the 513 issue iter_comments ",i.iter_comments(),"\n"
    lables=i.labels()
    print "the lable of 513 issue is",lables.count, "\n" 
    print "the milestone of 513 issue is  ",i.milestone,"\n" 
    print "the number of 513 issue is  ",i.number,"\n" 
    print "the state of 513 issue is  ",i.state,"\n" 
    print "the user of 513 issue is  ",i.user,"\n" 
    #    iss=repo.issues(state="closed")
#    for i in iss:
#        print i.number,"is", i.state,i.closed_by

#i = github3.issue('sigmavirus24', 'github3.py', 527)
#i = github3.issues()
#print i.state
