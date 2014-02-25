class HashTable(object):
    
    def __init__(self):
        self.hashtable = []
        for each in range(1, 7920): 
            self.hashtable.append([])
            
    def _get_bucket(self, word, table):
        n = 0
        p = 1
        for i in word:
            n += ord(i) * (31 ** p)
            p += 1           
        return n % len(table) 
    
    def _rebucket_values(self):
        new_table = self._resize_table()
        for each in self.hashtable:
            if len(each) == 0:
                pass
            else:    
                k, v = each
                new_bucket = self._get_bucket(k, new_table)
                self._collision_detection(k, new_table[new_bucket], v, new_table)
        return new_table        
                        
    def _resize_table(self):
        new_table = []
        for each in range(1, len(self.hashtable)*2):
            new_table.append([])
        return new_table
             
    def _resize_check(self):
        self.n = 0
        for each in self.hashtable:
            if len(each) > 0:
                self.n += 1
        return float(self.n) / float(len(self.hashtable)) > 0.60
        
    def _collision_resolution(self, bucket_no, table, word, value):
        if bucket_no < len(table)/2:    
            while len(table[bucket_no]) != 0:
                bucket_no += 1
                if word in table[bucket_no]:
                    break
        else:
            while len(table[bucket_no]) != 0:
                bucket_no -= 1
                if word in table[bucket_no]:
                    break  
        return bucket_no    
        
    def _collision_detection(self, word, bucket, value, table):
        if len(bucket) == 0:
            bucket.extend([word, value])
        elif word in bucket:
            del bucket[:]
            bucket.extend([word, value])
        elif word not in bucket and len(bucket) != 0:
            bucket_no = self._collision_resolution(table.index(bucket), table, word, value)
            if word in table[bucket_no]:
                del table[bucket_no][:]
            table[bucket_no].extend([word, value])
            
    def hashtable(self):
        # is there a better way of calling my table? Magic Method?
        return self.hashtable    
        
    def get_value(self, word):
        bucket = self._get_bucket(word, self.hashtable)
        bucket_no = self.hashtable[bucket]
        if word not in bucket_no:
            if bucket_no < len(self.hashtable):
                try:
                    while word not in self.hashtable[bucket]:
                        bucket += 1
                except IndexError:
                    return None
            else:
                try:
                    while word not in self.hashtable[bucket]:
                        bucket -= 1
                except IndexError:
                    return None           
        return self.hashtable[bucket]        
                                 
    def add_to_table(self, word, value):
        if self._resize_check() is True:
            self.hashtable = self._rebucket_values()      
        bucket = self.hashtable[self._get_bucket(word, self.hashtable)]
        return self._collision_detection(word, bucket, value, self.hashtable) 
        

        