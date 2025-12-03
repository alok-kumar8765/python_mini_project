# Implements Time-To-Live (TTL) caching for efficient data retrieval using 'cachetools'.

import time
from typing import Dict
from cachetools import TTLCache

# --- 1. Initialize the TTLCache ---
# Create a cache with a maximum of 100 items.
# Each item will be valid for 10 seconds (ttl=10).
cache: TTLCache[str, str] = TTLCache(maxsize=100, ttl=10)

# --- 2. Define the Data Fetching Function with Caching ---
def get_data(key: str) -> str:
    """
    Fetches data with TTL caching.
    Returns data from cache if available and not expired; otherwise, computes and caches it.
    
    :param key: The unique identifier for the data.
    :return: A string indicating the source of the data (Cached or Fresh) and its value.
    """
    # Check if the key is already in the cache (and has not expired)
    if key in cache:
        # Data is cached and fresh, return it immediately
        return f"✅ Cached: {cache[key]}"

    # --- Simulate Expensive Operation (Executed only if cache miss or expired) ---
    # In a real application, this would be a database query or an API call.
    value = f"value_for_{key}"
    
    # Store the new (fresh) value in the cache. 
    # The cache automatically tracks the time of insertion.
    cache[key] = value
    
    # Return the fresh data
    return f"✨ Fresh: {value}"

# --- 3. Example Usage ---
if __name__ == "__main__":
    key = "user:1"
    
    # 1. Fresh call (cache miss)
    print(f"Attempt 1: {get_data(key)}")
    
    # 2. Wait 2 seconds (still within the 10s TTL)
    time.sleep(2) 
    
    # 3. Cached call (cache hit)
    print(f"Attempt 2: {get_data(key)}")
    
    # 4. Wait 11 seconds in total (to exceed the 10s TTL)
    print("... Waiting 11 seconds for cache to expire ...")
    time.sleep(11) 
    
    # 5. Expired call (cache miss again, forces a fresh calculation)
    print(f"Attempt 3: {get_data(key)}")