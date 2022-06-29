#!/usr/bin/python3
class LockedClass:
    """User can only create instance attribute 'first_name'"""
    __slots__ = ['first_name']