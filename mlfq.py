import sys, time, psutil

process = psutil.Process(int(sys.argv[1]))
priorities = [0, 10, 19]
queue = 0

for second in range(1, 31):
  time.sleep(1)
  if second % 10 == 0:
    queue = 0
    if second % 10 == 0:
      queue = 0
      print(second, "BOOST -> Q0")
    elif second % 3 == 0 and queue < 2 and process.cpu_percent() > 50:
      queue += 1
      print(second, "demoted -> Q1 " + str(queue))
    
    process.nice(priorities[queue])
