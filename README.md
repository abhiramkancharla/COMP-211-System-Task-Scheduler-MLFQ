# COMP-211-System-Task-Scheduler-MLFQ

In this project, I explored how the MLFQ task scheduler works. The MLFQ is a multi-level feedback queue that learns what processes take the most amount of time and organizes processes in the computer accordingly.

For an overview, a multi-level feedback queue is just like a simple queue, but every process that gets added goes to the top of the queue. The MLFQ measures how long the queue takes to run. There is a certain threshold, which is about 10 ms, and if that process takes longer than the threshold, then it demotes that process to the next one. Tasks in this queue run at the top first and at the bottom last, so if it gets demoted, it doesn't run until the top job finishes.

Another addition to this is I/O tasks, which are input-output tasks. For example, if an application is waiting on your input, so you have to enter keys or type something, then what it does is it uses the CPU temporarily, so it has a CPU burst, and then it sleeps right after. While it does use the CPU, it leaves, and it doesn't hit the threshold because it's just a really small period of time that it does use the CPU.

One thing I found interesting is, in 2007, there was a program that hijacked processes and computers, not letting them run by putting itself at the top of the queue. This was possible because the program ran in the task scheduler. Right before it hit the threshold, which was about 10 ms, at 9 ms, the program cut itself and then went to sleep. It just never hit the threshold, and right after it went to sleep, it came back up again and started running.

This caused a lot of issues for people using the computer because your CPU report reported 0% usage while your CPU was actually being used. It didn't allow other processes to run either because it works on a queue basis. 

## Code

mlfq.py accesses one program that you specify from the terminal, and it demotes it on the macOS scheduler depending on how much CPU usage it's using. It doesn't necessarily do much because, on your computer, there are multiple cores, so it's probably running on its own core. Assuming there was only a single core, this Python script would be intended to reduce the priority of the program that you're running on your terminal. 

**Slides:** https://docs.google.com/presentation/d/1is4Kc3UNWYTKfPib5qjYPnkJPTfZ1GKGkDFkDfpMzhw/edit?usp=sharing
