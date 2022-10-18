#!/usr/bin/python3

""" Defines a Locked Class. """

class LockedClass:
    __slots__ = ['first_name']
    def __init__(self, name=""):
        self.first_name = name
