
import re
import hashlib
import sqlite3
import xml.etree.ElementTree as ET
from datetime import datetime
import os

def f1(a, b="x.xml", c=50, d=None):

    e = sqlite3.connect(a)
    f = e.cursor()
    
    f.execute("""
        SELECT id, name, category, value, status, created_date 
        FROM items 
        WHERE status IN ('active', 'pending', 'review')
    """)
    g = f.fetchall()
    
    f.execute("""
        SELECT category, COUNT(*) as count, AVG(value) as avg_value, SUM(value) as total_value
        FROM items
        GROUP BY category
        HAVING COUNT(*) > 2
    """)
    h = {x[0]: {'count': x[1], 'avg': x[2], 'total': x[3]} for x in f.fetchall()}
    
    f.execute("""
        SELECT DISTINCT category, MAX(value) as max_val, MIN(value) as min_val
        FROM items
        WHERE created_date > date('now', '-30 days')
        GROUP BY category
    """)
    i = f.fetchall()
    
    e.close()
    
    j = []
    k = {}
    
    for _, m in enumerate(g):
        n, o, p, q, r, s = m
        
        if d and p not in d:
            continue
            
        if q is not None and q > c:
            if p in h:
                t = q / h[p]['avg'] if h[p]['avg'] > 0 else 0
                
                if t > 1.5 or (r == 'review' and q > c * 1.2):
                    if p not in k:
                        k[p] = []
                    
                    u = (q * 0.6) + (h[p]['total'] * 0.2 / h[p]['count'])
                    u += 10 if r == 'active' else 5 if r == 'pending' else 2
                    
                    k[p].append({
                        'id': n,
                        'name': o,
                        'value': q,
                        'score': u,
                        'status': r,
                        'created': s,
                        'ratio': t
                    })
    
    for v, w in k.items():
        x = sorted(w, key=lambda y: (y['score'], y['value']), reverse=True)
        
        for z in x[:5]:
            if z['score'] > 100 or (z['ratio'] > 2 and z['status'] == 'active'):
                j.append({
                    'category': v,
                    'data': z,
                    'meta': h.get(v, {}),
                    'rank': x.index(z) + 1
                })
    
    aa = ET.Element("DataExport")
    aa.set("generated", datetime.now().isoformat())
    aa.set("total_records", str(len(j)))
    
    ab = ET.SubElement(aa, "Metadata")
    for ac in i:
        ad = ET.SubElement(ab, "CategoryMeta")
        ad.set("category", str(ac[0]))
        ad.set("max_value", str(ac[1]))
        ad.set("min_value", str(ac[2]))
    
    ae = ET.SubElement(aa, "Aggregations")
    for af, ag in h.items():
        ah = ET.SubElement(ae, "Aggregate")
        ah.set("category", af)
        ai = ET.SubElement(ah, "Count")
        ai.text = str(ag['count'])
        aj = ET.SubElement(ah, "Average")
        aj.text = str(round(ag['avg'], 2))
        ak = ET.SubElement(ah, "Total")
        ak.text = str(ag['total'])
    
    al = ET.SubElement(aa, "FilteredResults")
    
    for am in j:
        an = ET.SubElement(al, "Item")
        an.set("category", am['category'])
        an.set("rank", str(am['rank']))
        
        ao = am['data']
        for ap, aq in ao.items():
            if ap != 'created':
                ar = ET.SubElement(an, ap.capitalize())
                ar.text = str(aq)
        
        if am['meta']:
            as_ = ET.SubElement(an, "CategoryStats")
            for at, au in am['meta'].items():
                av = ET.SubElement(as_, at)
                av.text = str(round(au, 2) if isinstance(au, float) else au)
    
    aw = ET.ElementTree(aa)
    ET.indent(aw, space="  ", level=0)
    aw.write(b, encoding='utf-8', xml_declaration=True)
    
    return {
        'total_processed': len(g),
        'total_filtered': len(j),
        'categories': len(k),
        'output_file': b
    }

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(email_regex, email) is not None



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[\W_]', password):
        return False
    return True


def log_message(message):
    """
    Appends the given message to a log file named 'log.txt'.

    Args:
        message (str): The message to be logged.

    The message is written to the file with a newline character appended.
    """
    with open('log.txt', 'a') as f:
        f.write(message + '\n')

def generate_unique_filename(filename):
    """
    Generates a unique filename by appending a timestamp before the file extension.

    Args:
        filename (str): The original filename (e.g., 'demo.jpg').

    Returns:
        str: A new filename with a timestamp inserted before the extension (e.g., 'demo_20240607123456789012.jpg').
    """
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"{base}_{timestamp}{ext}"


def read_log():
    f = open('log.txt', 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content
