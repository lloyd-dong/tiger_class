# Programming Language


| Features      | Kotlin 1.5.21| Scala 2.12.3 | Go          | Julia 1.6   | Python 3.9.6| J11         | Shell       |   Groovy    |  C++        |   C         |
| -----------   | -----------  | -----------  | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| dependency    | _ | _ | go mod init example/hello => go.mod    | ju   | p | j         | s       |  gr    |  c++        |   c         |
| Class inherit | class  A:B<br> **open** clas | class A extends B | g         | ju  | p| j        | s       |   gr    |  c++        |   c         |
| Class declare | No new<br>[主/次构造][ktl_cnstr]| Scala 2.12.3 | g         | ju  | p| j        | s       |   gr    |  c++        |   c         |
| str           | X '', √ ""   | X '', √ ""   | g         | ju       | ',","""     |  j       | ''!=""      | '',""       | c++         |   c         |  
| str interpolation |  "${a}"  | s"\${a}"<br>f"${a%2.2f}"<br>raw"a\nb" | g         | ju       | f"${a:.2f} |  j| s | gr | c++    |   c         |  
| function      | fun f(a:Int):Int {}|def f(a:int):int | g         | ju  | def f(a:int)->int:| j      | s  |   gr |  c++   |   c         |
| run shell     | Runtime.getRuntime().exec(“cmd”)| “Cmd”.! / .!!<br>**pipe** | g         | ju  |os.system(“cmd”)| j | s | “Cmd”.execute() |  c++    |   c    |
| tempalate     | k | sc | g       | ju   | p | j         | s       |  gr    |  c++        |   c         |

free style

### links:
[ktl_cnstr]:https://www.kotlincn.net/docs/reference/classes.html
			
										
