'''
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributor: Jiatong Wang, Bhaskar Krishnamachari
 *     Read license file in main directory for more details
'''

import requests
import sys
import json
import time
from datetime import datetime


def open_file():
    list=[]
    ip_path = sys.argv[1]

    with open(ip_path, "r") as ins:
        for line in ins:
            line = line.strip('\n')
            r = requests.get("http://"+line+":49155")
            result = json.loads(r.content)
            result['ip']=line
	    result['last_update']=datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            data=json.dumps(result)
            # print '\n'
            # print data
            # print '\n'
            list.append(data)
    # print list
        return list

