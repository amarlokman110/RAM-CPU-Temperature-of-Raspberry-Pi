# RAM & CPU & Temperature of Raspberry Pi

<img src="https://user-images.githubusercontent.com/54172575/64046470-77ff4480-cb9e-11e9-8bd0-f2b5af5d04a8.png" width="100" />

Raspberry pi is a powerful device which can be used in many functions. That is why people are using raspberry pi for performing some intensive tasks that squeeze last drop of CPU power from the Raspberry Pi. 

## RAM usage Raspberry Pi
RAM is an acronym for random access memory, a type of computer memory that can be accessed randomly; that is, any byte of memory can be accessed without touching the preceding bytes.

* use psutil library
* ram = psutil.virtual_memory() = Return statistics about system memory usage as a named tuple including the following fields, expressed in bytes
* ram_percent_used = ram.percent = display in the percentage form.

## CPU usage Raspberry Pi
Central Processing Unit. The CPU is the primary component of a computer that processes instructions. It runs the operating system and applications, constantly receiving input from the user or active software programs.

* psutil library was involved.
* install psutil library by using (pip install psutil)
* psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors)
* psutil.cpu_percent() to show in percentage form

## Temperature Raspberry Pi
Raspberry Pi is a low-end mobile computer. So it doesn’t have fans to cool it down like other desktop/laptop CPUs. If your temperature rises above 80°C, you will see a little thermometer on you Raspbian desktop. That indicates that your Pi is getting hot. Then at 85°C, it changes to a full thermometer. However, that is the maximum recommended operating temperature. After this temperature, your CPU starts throttling and reduces the clock to cool down the temperature. This will decrease the performance.

* Two libraries was involved which are re (regular expression) and commands
* Commands module contains wrapper function thich take a system command as a string. 
* using python language which describe temperature code as follows "commands.getstatusoutput('vcgencmd measure_temp')"
