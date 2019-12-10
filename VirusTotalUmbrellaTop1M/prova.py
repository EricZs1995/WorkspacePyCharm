import sys
import os
from datetime import datetime,timedelta


path = sys.argv[1]


dirName = os.path.basename(path)
basename = dirName.split("/")

print(basename[-1])




