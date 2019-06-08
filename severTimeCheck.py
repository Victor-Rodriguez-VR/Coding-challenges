def server_time_check(task_config, task_times):
 nums = [int(s) for s in task_times.split(" ")]
 placeHolder = [int (z) for z in task_config.split(" ")]
 spentTime =0
 numberOn =0
 for n in nums:
   spentTime+=n
   numberOn+=1
   if(spentTime > placeHolder[1]):
     
    print(placeHolder[0]-numberOn)
    break
   numberOn+=1
 print(placeHolder[0])
 
  

## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input("Please input the number of tasks, and the maximum total execution time:")
task_times = input("Please input the execution times of each task, seperated with a space:")

server_time_check(task_config, task_times)
