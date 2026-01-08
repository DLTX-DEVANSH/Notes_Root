
When we have multi-File project in any language (let's say C ) and want to build the project . ofc we do have the option to just press the build button on a modern editor but  when you would do that , you realize that it doesn't work .

why? because it is not a single file system , and the compiler wouldn't risk merging them by itself . 
so it's you job to compile each file , link them correctly and use the terminal or shell to create a correct executable file 

Lets say we have 4 files[(Link to Source Code)](https://github.com/DLTX-DEVANSH/Notes_Utillity/tree/main/Makefiles/SimpleExample)
`getInput.c  getInput.h  printAge.c  printDouble.c`

`printAge.c`  & `printDouble.c`  both uses the `getInput.c` and it's our job to use commands to compile and link them 

we first compile the files into object files
```bash
gcc -c getInput.h
gcc -c printAge.h
gcc -c getDouble.h
```
now link them
```bash
gcc printAge.o getInput.o -o printAge
```

and we are done but what if the project had 10000 files(not rare) then we would have to search for the modified file compile it , then link all 10000 files again , so much work . what if we have  have a command that could just recompile the modified file and then link it together , something like
```bash
recompile -printAge
```

well that's the work of make files ,here is a general syntax
```bash
target : prerequisites/dependencies  
<TAB>command
<TAB>command 
```

`target`  is like a flag that  the makefile uses as checkpoint for the entire process , the `dependencies` are the prerequisites for full filling the target's requirement before starting to execute the commands of that target block , they can be files or other targets too , in the second case , other targets must be full filled before the current target  

`commands` must be indented by a tab  not multiple space. the collection of commands is called a recipe for that target 

so for our 4 files above the correct [MakeFile](https://github.com/DLTX-DEVANSH/Notes_Utillity/blob/main/Makefiles/SimpleExample/Makefile) looks like 
```makefile 
# -*- MakeFile -*-

all: printAge printDouble

printAge: printAge.o getInput.o
	gcc printAge.o getInput.o -o printAge

printAge.o: printAge.c getInput.h
	gcc -c printAge.c

getInput.o: getInput.c
	gcc -c getInput.c

printDouble: printDouble.o getInput.o
	gcc printDouble.o getInput.o -o printDouble

printDouble.o:
	gcc -c printDouble.c

CLEAN: 
	rm -f *.o printDouble printAge
```

`#` tells shell that it is a comment 
`# -*- MakeFile -*-` tells the shell to treat it is a make file 

now lets examine the working of makefile , when we type this in shell
```bash
make printAge
```
the entire execution looks like - 
![[Pasted image 20251223173157.png]]

when we just write 
```bash 
make
```
it would just go to the first target that in our case is 
```
all: printAge printDouble
```

Now this was basic , kids play . now we are going deeper , borderline  Shell scripting (make file is kind of shell scripting )