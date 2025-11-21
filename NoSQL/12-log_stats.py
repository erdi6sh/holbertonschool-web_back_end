#!/usr/bin/env python3
""" Provides stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    log_stats()
