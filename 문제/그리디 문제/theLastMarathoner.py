
from collections import *

player = ["조단","현수", "승하", "도우너", "도우너"]
completed = ["조단","현수", "승하", "도우너"]

answer = Counter(player)-Counter(completed)

for i in answer:
    print(i)