#!/usr/bin/env python3
'''
A script that returns the list of school having a specific topic.
'''


def schools_by_topic(mongo_collection, topic):
    '''
    A function that returns the list of school having a specific topic.
    '''
    value = {"topics": topic}
    return mongo_collection.find(value)