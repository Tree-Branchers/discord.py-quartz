# from datetime import datetime

# start_time = datetime.now()

try:

    from googlesearch import search

except ImportError:

    print("No module named 'google' found")

# to search
query = input()

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)

# end_time = datetime.now()

# print(end_time - start_time)

# result = 9 seconds
