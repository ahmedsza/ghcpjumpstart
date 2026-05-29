
import os, sys, json, math, re, time, random  # unused imports and comma style
from math import * 

import re as regex

PASSWORD = "SuperSecret123!"  
DEBUG = True

GLOBAL_CACHE = {}  
_list = []  


list = "I am a string now"

def add_item(item, collection=[]):  
    collection.append(item)
    return collection

def compute(x, y):
    if x is 42:  
        return "the answer"
    if y == None:  
        y = 0
    tmp = x * y * 3.14159 / 0.0 if y else x * 999999999  
    return tmp

def slow_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def parse_file_bad(path):
    f = open(path, "r")
    data = f.read()
    if "password" in data:
        print("Found password!") 
    return data

def parse_file_ok(path):
    with open(path, "r") as f:
        try:
            return json.loads(f.read())
        except Exception:
            return []  

def search_regex_many_patterns(text, patterns):
    results = []
    for p in patterns:
        r = re.compile(p)
        m = r.search(text)
        if m:
            results.append(m.group(0))
    return results

def do_network_like_call(url):
    cmd = "curl -s " + url  
    os.system(cmd) 

def broken_control_flow(x):
    if x:
        if x > 0:
            for i in range(10):
                try:
                    if i % 2 == 0:
                        pass
                    else:
                        raise ValueError("odd")
                except:
                    continue
            else:
                return None
        else:
            return "negative"
    id = 5
    return id


def multiply(a,b):
    return a * b

def times(a,b):
    return a * b


def get_user_name(user):
    try:
        return user["name"]
    except KeyError:
        return "unknown"

def get_user_name_safe(user):
    if "name" in user:
        return user["name"]
    return "unknown"


def process(data):
    out = []
    for x in data:
        if isinstance(x, dict):
            out.append(get_user_name(x))
        elif isinstance(x, str):
            out.append(x.strip().lower())
        else:
            out.append(str(x))
    GLOBAL_CACHE["last"] = time.time()
    return out


def main():
    print("Starting demo app")
    name = input("Enter your name: ")  
    print("Hello, " + name)
    expr = input("Enter an expression to eval: ")
    try:
        res = eval(expr) 
        print("Result:", res)
    except Exception as e:
        print("Bad expression", e)


    data = [random.randint(0, 1000) for _ in range(500)]
    sorted_data = slow_sort(data)  


    tmp = parse_file_bad("nonexistent.txt") 

    for i in range(100):
        search_regex_many_patterns("aaaa" * 100, ["a+", "(a)+", "aa+"])


    if DEBUG:
        raise Exception("debug mode fatal")  
if __name__ == "__main__":
    main()