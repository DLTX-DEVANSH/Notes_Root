In computers data is stored in the form bits and bytes ( 1byte = 8 bits) 
A file that consists of exclusively  ACII characters in known as ***text file*** & all other formats are known as ***binary file*** .

for example :- 
```c
#include <stdio.h> 

int main()
{
	printf("hello, world\n");
	return 0;
}
``` 
`hello.c`

here hello.c is called a text file , each text character corresponds to a ASCII character and each ASCII character corresponds to a Byte . each line is also terminated by a `\n` line termination  
![[Pasted image 20251225140359.png ]]

For the computer to run this file ,it must be first converted into low level `machine instruction`  these instructions are then packed into a form called `Executable object program/file`
This compilation is performed by a `compiler driver` .

```bash
gcc hello.c -o hello
```

Lifecycle of compilation process 
![[Pasted image 20251225142445.png]]
[[GCC commands.pdf#page=1&selection=2,0,2,40|Commands for specific point in the process ]]

- `Preprocessing phase` : In this phase the preprocessor modifies the original C code into a modified file according to the preprocessing directives beginning by `#`
- `Compilation Phase` : the compiler translated *hello.i* into the actual [Assembly Code](https://github.com/DLTX-DEVANSH/CSAPP_Solutions_and_Source_Code/blob/main/Chapter%201/c_1_1/hello.s) 
- `Assembly Phase` : the assembler translates this assembly program into ***Relocatable Object File*** called as `hello.o` 
- `Linking Phase` : here all the object files are merged by the ***linker*** into a *Simple Executable file* hello.exe 


