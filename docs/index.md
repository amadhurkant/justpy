# Justpy docs
Justpy is a collection of random python functions that can be used in development. <br>
Functions are mainly from [Ipsocoin Project](https://github.com/amadhurkant/ipsocoin) <br>
In this simple page you will find details on usage of functions and errors.

## Installation
Just download the files from github: [Justpy](https://github.com/amadhurkant/justpy) <br>
Extract them and rename folder as ```justpy``` and copy folder to directory you are working in. <br>
Source functions in module: ```>>>  from justpy.kfuncs import *``` or ```>>> from justpy.kfuncs import functionName```

## removeData()

_**Working:**_  This function takes two ```str``` type arguments. 
  1. first argument is ```remove```: it takes characters to remove
  2. second argument is ```data``` : this takes data from which characters are to be removed <br>

_**Example:**_  <br>
```
>>> from kfuncs import removeData
>>> remove = "0x"
>>> data = "0x0123456789abcdef"
>>> removeData(remove, data)
>>>'0123456789abcdef' 
``` 
<br>

_**Errors:**_ The following errors are possible: <br>
  1. ```RemoveNotError``` : It implies that the character you want to remove are not present in provided data.

_**Usecase:**_  To remove ```0x``` from hex string.

## checkHx()
_**Working:**_  This function takes one ```str``` hex-type arguments. 

_**Example:**_  <br>
```
>>> from kfuncs import checkHx
>>> data = "33f"
>>>  checkHx("33f")
>>> '033f'
>>> checkHx("323f")
>>> '323f
```
<br>

_**Errors:**_ Currently no errors: <br>

_**Usecases:**_  To convert hex string to even size so that ```bytes.fromhex()``` gives no errors..
