#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs
"""
from pymongo import MongoClient


def log_stats():
    # Connect to the MongoDB server and access the logs database and nginx
    # collection
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the number of documents for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of GET requests with path "/status"
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
