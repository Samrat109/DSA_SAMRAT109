#Design a time-based key-value data structure that can store multiple values for the same key at different time 
# stamps and retrieve the key's value at a certain timestamp.

#Implement the TimeMap class:

    #TimeMap() Initializes the object of the data structure.
    #void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    #String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
    # If there are multiple such values, 
    # it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class TimeMap(object):

    def __init__(self):
        # key -> list of [timestamp, value]
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            # values[mid][0] = timestamp
            # values[mid][1] = value

            if values[mid][0] <= timestamp:
                # This timestamp is valid.
                # Save its value and search for a larger valid timestamp.
                result = values[mid][1]
                left = mid + 1

            else:
                # Timestamp is too large.
                right = mid - 1

        return result