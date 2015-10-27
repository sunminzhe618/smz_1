def new(num_buckets=256):
    """initializes a map with the given key"""
    aMap=[]
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap
def hash_key(aMap,key):
    """a given key this will create a number and the converts to an index for the aMap
    buckets."""
    print hash(key)%len(aMap)
    return hash(key)%len(aMap)

def get_bucket(aMap,key):
    """given a key, find the bucket"""
    bucket_id=hash_key(aMap,key)
    return aMap[bucket_id]
    
def get_slot(aMap,key,default=None):
    """
    return the index,key,and value of a slot found in a bucket.
    return -1,key,and default(None if not set) when not found.
    """
    bucket=get_bucket(aMap,key)
    print"this is bucket:",bucket
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            print"this is i,k,v",i,k,v
            return i,k,v
    return -1,key,default
    
def get(aMap,key,default=None):
    """gets the value in a bucket for the given key or the default"""
    i,k,v=get_slot(aMap,key,default=default)
    return v

def set(aMap,key,value):
    """sets the key to the value, replacing any existing value"""
    bucket=get_bucket(aMap,key)
    i,k,v=get_slot(aMap,key)
    print"i,k,v(set) is",i,k,v
    if i>=0:
        #the key exists,replace it
        bucket[i]=(key,value)
    else:
        # the key does not ,append to create it
        bucket.append((key,value))
        
def delete(aMap,key):
    """deletes the given key from the map"""
    bucket=get_bucket(aMap,key)
    
    for i in xrange(len(bucket)):
        k,v=bucket[i]
        if key==k:
            del bucket[i]
            break

def list(aMap):
    """prints out what's in the map"""
    for bucket in aMap:
        if bucket:
             for k,v in bucket:
                 print k,v