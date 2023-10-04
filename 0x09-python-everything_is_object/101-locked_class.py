#!/usr/bin/python3
"""Locked Class"""
class LockedClass:
    """prevent the dynamic creation of instance"""
    __slot__ = ["first_name"]

