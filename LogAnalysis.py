test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
  stats = dict()
  #loop over each line in the log
  for log in logs:
    logParts = log.split(" ")
    description = log.split(":")[1][1:]
    
    # find catagory
    catagory = logParts[0][1:-1]
    # find http code
    code = logParts[1]
    # find the code description
        #find beginning 
    start = log.find(code) + len(code) +1
        #find end
    end = log.find(":")
        # apply beginning and end for description
    description = log[start:end]
    # find the actual error msg the [1:] ignores some whitespace
    error = log.split(":")[1][1:]
    # Following IF's determine if all parts of the log are keys.
    if(stats.get(catagory)):
      if(stats[catagory].get(code)):
        if(stats[catagory][code].get(description)):
          if(stats[catagory][code][description].get(error)):
            stats[catagory][code][description][error] +=1
          else:
            stats[catagory][code][description][error] = 1
        else:
          stats[catagory][code][description] = {error:1}
      else:
        stats[catagory][code] = {description : {error:1}}
    else:
      stats[catagory] = {code:{description:{error:1}}}
  return stats
  
    
print(log_stats(test_data))