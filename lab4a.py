#!/usr/bin/env python3

def join_sets(s1, s2):
    return s1 | s2  # Union of two sets

def match_sets(s1, s2):
    return s1 & s2  # Intersection of two sets

def diff_sets(s1, s2):
    return s1 ^ s2  # Symmetric difference of two sets
