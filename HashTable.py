class HashTable(object):
    
    def __init__(self):
        ''' initializes hashtable'''
        self.filled_buckets = 0
        self.hashtable = []
        for each in range(1, 7920): 
            self.hashtable.append([])
            
    def _get_bucket(self, word):
        ''' hash algorithm - indexes keyword to find bucket'''
        n = 0
        for i, letter in enumerate(word):
            n += ord(letter) * (31 ** i)
        return n % len(self.hashtable) 
    
    def _rebucket_values(self):
        ''' rehashes keys into new table '''
        old_table = self.hashtable
        self.hashtable = self._resize_table()
        for each in old_table:
            if len(each) == 0:
                pass
            else:    
                k, v = each
                new_bucket = self._get_bucket(k)
                self._collision_detection(k, new_table[new_bucket], v, self.hashtable)
        return new_table        
                        
    def _resize_table(self):
        ''' doubles table size '''
        new_table = []
        for each in range(1, len(self.hashtable)*2):
            new_table.append([])
        return new_table
             
    def _resize_check(self):
        ''' checks to see if table needs to be resized '''
        return self.filled_buckets / len(self.hashtable) > 0.60
        
    def _collision_resolution(self, bucket_no, table, word, value):
        ''' finds next available bucket if collision has occured '''
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
        ''' decides what to do with k/v pair - insert into table, replace existing k/v with new or run collision res to get new bucket'''
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
        ''' finds key in hashtable '''
        bucket_no = self._get_bucket(word)
        bucket = self.hashtable[bucket_no]
        if word != bucket[0]:
            if bucket_no < len(self.hashtable)/2:
                change = lambda x: x + 1
            else:
                change = lambda x: x - 1
            try:
                while word != self.hashtable[bucket_no][0]:
                    bucket_no = change(bucket_no)
            except IndexError:
                return None           
        return self.hashtable[bucket_no][1]        
                                 
    def add_to_table(self, word, value):
        ''' checks size of table  '''
        if self._resize_check():
            self.hashtable = self._rebucket_values()      
        bucket = self.hashtable[self._get_bucket(word)]
        if len(bucket) == 0:
            self.filled_buckets += 1
        return self._collision_detection(word, bucket, value, self.hashtable) 
        

        