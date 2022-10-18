#!/usr/bin/python3
"""
Create Locked Class
"""

class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
    
    def __init__(self, firat_n):
        self.first_name = first_n
