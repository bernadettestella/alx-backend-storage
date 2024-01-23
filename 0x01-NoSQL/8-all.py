#!/usr/bin/env python3
"""
This module contains a function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    lists all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
