# NanoBasic

## Table of Contents

* 3.4. [Variables](#variables)
* 3.5. [Array Variables](#array-variables)
* 3.6. [Expressions and Operators](#expressions-and-operators)

## Reference Manual

## Introduction

NanoBasic is a simple BASIC interpreter that runs on the NanoVM. It is based on the
Microsoft (TM) BASIC interpreter, which is available on the Commodore 64 and other
computers of the 1980s.

Information to the Microsoft (TM) BASIC interpreter can be found
[here](https://vtda.org/docs/computing/Microsoft/MS-BASIC/8101-530-11-00F14RM_MSBasic8086XenixReference_1982.pdf).

NanoBasic is available on the Techage TA3 Terminal as part of the techage mod for
Minetest/Luanti. It allows you to monitor and control the Techage machines and devices.
It works similar to the Lua Controller of the Techage mod, but fits more into#
the era of TA3 machines.

NanoBasic is normally not visible on the Techage Terminal. But it can be activated
by means of the Techage Info Tool (open-ended wrench).

### Line Numbers

Every BASIC program line begins with a line number. Line numbers must be ordered
in ascending sequence. Line numbers are mainly used as references for branches
(jump targets) and as line references for compiler error messages.

The terminal has a convenient text editor that allows you to edit and copy entire
BASIC programs. Lines do not have to be entered or edited individually via a command
line.

Line numbers must be in the range 1 to 65535.

### Character Set

NanoBasic supports the ASCII character set, which includes the upper and lower case
letters of the alphabet, the digits 0 through 9, and special characters such as
punctuation marks and mathematical symbols. NanoBasic distinguishes not between
upper and lower case letters. Variable names and BASIC keywords are not case-sensitive.

### Constants

NanoBasic supports integer and string constants. Integer constants are numbers
without a decimal point. String constants are enclosed in double quotes.

Examples:

```text
"Hello"
1234
```

Numeric constants are positive numbers in the range  0 to 2^31-1
(32 bit unsigned integer).

NanoBasic does not support floating point or negative numbers!

#### NIL

NIL is a special constant that represents the absence of a value. It is used to
pass a null value to a function where an array argument is expected.

### Variables

Variables are names used to represent values used program. The value of a variable
may be assigned by the programmer, or it may be assigned as the calculations in
the program. Before a variable a value, its value is assumed to be zero.

Variable names must begin with a letter and may contain letters and digits. Variable
names can have any length, but only the first 7 characters are significant.
If 2 variables differ only after the 7th digit, they are considered equal.

A variable name may not be the same as a reserved word. Reserved words include
all commands, statements, function names, and operator names.

Variables may represent either a numeric value or a string. String variable names
are written with a dollar sign ($) as the last character.
For example:

```text
A$ = "SALES REPORT"
```

The dollar sign is a variable type declaration character; that
is, it "declares" that the variable will represent a string.

### Array Variables

An array is a group or table of values referenced by the same variable name.
Each element in an array is referenced by an array variable that is subscripted
with an integer or an integer expression. An array variable name has as many
subscripts as there are dimensions in the array.
For example:

```text
DIM A(10)
```

This statement creates an array named A with 11 elements, A(0) through A(10).
The maximum number of elements in limited by the available heap memory.
Heaps are shared between arrays and strings. The heap size is 8KB.

NanoBasic supports only one-dimensional arrays.

### Expressions and Operators

An expression is a combination of variables, constants, and operators that
the interpreter evaluates to produce a value. Expressions can be used in
statements that require a value, such as assignment statements, PRINT statements,
and IF statements.

Operators perform mathematical or logical values. The Microsoft BASIC operators may
be divided into four categories:

1. Arithmetic
2. Relational
3. Logical
4. Functional

The following table lists the operators in each category:

| Category    | Operator | Description |
|-------------|----------|-------------|
| Arithmetic  | +        | Addition    |
|             | -        | Subtraction |
|             | *        | Multiplication |
|             | /        | Division    |
|             | MOD      | Modulus     |
|             | ^        | Exponentiation |
| Relational  | =        | Equal       |
|             | <>       | Not equal   |
|             | <        | Less than   |
|             | <=       | Less than or equal |
|             | >        | Greater than |
|             | >=       | Greater than or equal |
| Logical     | AND      | Logical AND |
|             | OR       | Logical OR  |
|             | NOT      | Logical NOT |
| Functional  | RND      | Random number |
|             | LEN      | Length of string |
|             | MID      | Substring   |
|             | LEFT$    | Left part of string |
|             | RIGHT$   | Right part of string |
|             | STR$     | Convert to string |
|             | VAL      | Convert to number |
|             | INSTR    | Find substring |
|             | CHR$     | Convert to character |
|             | ASC      | Convert to ASCII code |
|             | SPC      | Print spaces |

The precedence of operators is as follows:

1. Multiplication (*), Division (/), Modulus (MOD)
2. Addition (+), Subtraction (-)
3. Relational operators (=, <>, <, <=, >, >=)
4. Logical NOT operator
5. Logical AND operator
6. Logical OR operator

If, during the evaluation of an expression, division by zero is encountered,
the "Division by zero" error message is displayed and the program is terminated.

Relational operators are used to compare two values. The result of the comparison
is either "true" (1) or "false" (0). This result may then be used to make a decision
regarding program flow. (See "IF" statements)

Examples:

```text
IF RND(100)<1O GOTO 1000
IF I MOD J<>O THEN K=K+1
```

#### Functional Operators

The functional operators are used to manipulate strings and numbers. They are
used in expressions to convert between numbers and strings, to extract substrings,
to find substrings, and to convert between ASCII codes and characters.

NanoBasic has "intrinsic" functions that reside in the interpreter.
In addition, NanoBasic allows to define "external" functions that are written in Lua
to extend the functionality of the interpreter.

All these functions are called by name and are followed by a list of arguments
enclosed in parentheses. The arguments are separated by commas.

NanoBasic has a strong type system. The type of the arguments and the return value
of a function is determined by the function name. If, for example, the function
name is "STR$", the argument is converted to a string and the return value is a string.

#### String Operations

Strings may be concatenated by using +.

Example:

```text
10 A$="FILE" : B$="NAME"
20 PRINT A$+B$
30 PRINT "NEW "+A$+B$

>> FILENAME
>> NEW FILENAME
```

Strings may be compared using the same relational operators that are used with numbers:

```text
    =   <>   <   >   <=   >=
```

String comparisons are made by taking one character at a time from each string and
comparing the ASCII codes. If all the ASCII codes are the same, the strings are equal.
If the ASCII codes differ, the lower code number precedes the higher. If during string
comparison the end of one string is reached, the shorter string is said to be smaller.
Leading and trailing blanks are significant.

## Commands and Statements

This section describes the commands and statements that are available in NanoBasic in
alphabetical order.

### CONST

The CONST statement is used to define constants that are used in the program.
The CONST statement is nonexecutable and can be placed anywhere in the program.

Example:

```text
10 CONST MAX=100
20 DIM A(MAX)
```

### DATA

The DATA statement is used to define data that is used by the READ statement.

DATA statements are nonexecutable and must be placed at the end of the program.
A DATA statement may contain as many constants as will fit on a line (separated by commas). 
Up to 200 DATA statements may be used in a program.

This list of constants may contain numeric or string constants. String constants
must be enclosed in double quotes.

READ statements access DATA statements in the order in which they are encountered.
The variable type (numeric or string) in the READ statement must correspond to the
corresponding constant in the DATA statement.

### DIM

The DIM statement is used to dimension arrays. The DIM statement must be used before
the array is referenced in the program.

For instance, DIM A(5) defines a single-dimension array A. In standard BASIC, the
lower bound of any array was normally 1, so in this case, the variable A has five "slots",
numbered 1 though 5. In NanoBasic, the lower bound is always 0, so the variable A has
six "slots", numbered 0 through 5.

If a subscript is used that is greater than the maximum specified, a "Array index out of bounds"
error occurs. The minimum value for a subscript is always 0.

Example:

```text
10 DIM A(20)
20 FOR I=O TO 20
30 READ A(I)
40 NEXT I

DATA 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
```

### END

The END statement is used to terminate the program. END statements may be placed
anywhere in the program to terminate execution. Unlike the BREAK statement, END
does not cause a "Break in line nnnnn" message to be printed. An END statement
at the end of a program is optional.

### ERASE

The ERASE statement is used to delete an array.

Arrays may be redimensioned after they are ERASEd, or the previously allocated
array space in memory may be used for other purposes.

Example:

```text
10 DIM A(20)
20 ERASE A
30 DIM A(10)
40 END
```

### FOR...NEXT

Format:

```text
FOR variable = start TO end [STEP increment]
    statements
NEXT variable
```

`start`, `end`, and `increment` are numeric expressions. The `STEP` clause is optional.

The FOR statement is used to set up a loop that will execute a specified number of times.
The variable is assigned the value of `start` and is incremented by `increment` each time
through the loop. The loop continues until the variable is greater than `end`.

If the `STEP` clause is omitted, the increment is assumed to be 1.

Example:

```text
10 FOR I=1 TO 10
20 PRINT I
30 NEXT I
```

The program lines following the FOR statement are executed until the NEXT statement
is encountered. Then the counter is adjusted by the amount specified by STEP.
A check is performed to see if the value of the counter is now greater than the
final value (y). If it is not greater, NanoBasic branches back to the statement
after the FOR statement and the process is repeated. If it is greater, execution
continues with the statement following the NEXT statement.

### FREE

The FREE statement outputs the number of free bytes in the code, variable, and heap
areas of the NanoBasic interpreter to the terminal.

Example:

```
FREE

>> 16345/1020/8192 bytes free (code/data/heap)
```

### GOSUB...RETURN

Format:

```text
GOSUB line
.
.
.
RETURN
```

The GOSUB statement is used to branch to a subroutine. The RETURN statement is used
to return to the statement following the GOSUB statement.

A subroutine may be called any number of times in a program. A subroutine also may
be called from within another subroutine. Up to 8 levels of subroutine nesting are
allowed. If the limit is exceeded, an "Call stack overflow" error occurs.

Example:

```text
10 GOSUB 100
20 PRINT "END"
30 END
100 PRINT "SUBROUTINE"
110 RETURN
```

### GOTO

The GOTO statement is used to branch to a specified line number.
If the line number is not found, a "Line number not found" error occurs.

Example:

```text
10 GOTO 100
20 PRINT "END"
30 END
100 PRINT "GOTO"
110 END
```

### IF...THEN

Format:

```text
IF expression THEN statement [ELSE statement]
```

Or:

```text
IF expression GOT0 line [ELSE statement]
```

Or:

```text
IF expression THEN 
    statement
    .
    .
[ELSE 
    statement
    .
    .]
ENDIF
```

The IF statement is used to make a decision based on the value of an expression.
If the expression is true (nonzero), the THEN or GOTO clause is executed.
If the expression is false (zero), the statement following the ELSE keyword is executed.

The ELSE clause is optional.

Example:

```text
10 IF A=0 THEN 100
20 PRINT "
30 END
100 PRINT "A=0"
110 END
```

### LET

The LET statement is used to assign a value to a variable.
Notice the word LET is optional. The equal sign is sufficient for assigning
an expression to a variable name.

Example:

```text
10 LET A=10
20 LET B$="STRING"
20 PRINT A,B$
30 END
```

Or:

```text
10 A=10
20 B$="STRING"
20 PRINT A,B$
30 END
```

### ON...GOSUB and ON...GOTO

Format:

```text
ON expression GOSUB line1, line2, line3, ...

ON expression GOTO line1, line2, line3, ...
```

The ON statement is used to branch to a specified line number based on the value
of the expression. The expression must be an integer value.

For example, if the value is three, the program branches to line3.

In the ON...GOSUB statement, each line number in the list must be' the first line
number of a subroutine.

If the value of expression is zero or greater than the number of items in the list
NanoBasic continues with the next executable statement.

Example:

```text
10 ON A GOSUB 100,200,300
20 PRINT "END"
30 END
100 PRINT "GOSUB 100"
110 RETURN
200 PRINT "GOSUB 200"
210 RETURN
300 PRINT "GOSUB 300"
310 RETURN
```

### PRINT

The PRINT statement is used to display output on the screen.

Format:

```text
PRINT [<list of expressions>]
```

If \<list of expressions> is omitted, a blank line is printed. If \<list of expressions>
is included, the values of the expressions are printed at the terminal. The expressions
in the list may be numeric and/or string expressions.
(Strings must be enclosed in quotation marks.)

The position of each printed item is determined by the punctuation used to separate
the items in the list. NanoBasic divides the line into print zones of 10 spaces each
(tabs). In the list of expressions, a comma causes the next value to be
printed at the beginning of the next tab.

A semicolon causes the next value to be printed immediately after the last value.
Typing one or more spaces between expressions causes the next value to be printed
with one space between it and the last value.

If a comma or a semicolon terminates the list of expressions, the next PRINT
statement begins printing on the same line, spacing accordingly.

If the list of expressions terminates without a comma or a semicolon- a carriage
return is printed at the end of the line.

If the printed line is longer than the terminal width, the line is cut off at the
right edge of the terminal.

Example:

```text
10 PRINT "HELLO",
20 PRINT "WORLD"
30 END

>> HELLO     WORLD
```

### READ

The READ statement is used to read data from a DATA statement and assign them to
variables.

Format:

```text
READ variable1, variable2, ...
```

A READ statement must always be used in conjunction with a DATA statement. READ
statements assign variables to DATA statement values on a one-to-one basis. READ
statement variables may be numeric or string, and the values read must agree with
the variable types specified. If they do not agree, a "Data type mismatch" will
result.

A single READ statement may access one or more DATA statements (they will be
accessed in order), or several READ statements may access the same DATA statement.
If the number of variables the list of variables exceeds the number of elements
in the DATA statement(s), an "Out of data" error message is printed. If the
number of variables specified is fewer than the number of elements in the DATA
statement(s), subsequent READ statements will begin reading data at the first
unread element. If there are no subsequent READ statements, the extra data is
ignored.

To reread DATA statements from the start, use the RESTORE statement.

Example:

```text
10 READ A,B$
20 PRINT A,B$
30 END
40 DATA 10,"STRING"
```

### REM

The REM statement is used to insert comments in a program. REM statements are
nonexecutable and may be placed anywhere in the program.

Example:

```text
10 REM THIS IS A COMMENT
20 PRINT "END"
30 END
```

### RESTORE

Format:

```text
RESTORE [offset]
```

To allow DATA statements to be reread from a specified offset.
After a RESTORE statement is executed, the next READ statement accesses the first
item in the first DATA statement in the program. If offset is specified, the next
READ statement accesses the item at the given offset.
Offset is a value from 0 (first DATA statement) to the offset of the last DATA
statement.

Example:

```text
110 READ A,B$
20 RESTORE
30 READ C,D$
40 PRINT A B$ C D$
50 END
60 DATA 10,"STRING"

>> 10 STRING 10 STRING
```

### TRON and TROFF

The TRON and TROFF statements are used to turn on and off the trace mode.
When trace mode is on, the line number of each executed statement is printed.
This is useful for debugging programs.

Example:

```text
10 TRON
20 FOR I=1 TO 4
30 PRINT "HELLO"
40 NEXT I
50 PRINT "WORLD"
60 END

>> [20] [30] HELLO
>> [30] HELLO
>> [30] HELLO
>> [30] HELLO
>> [50] WORLD
>> [60] Ready.
```

### WHILE...LOOP

Format:

```text
WHILE expression
    statements
LOOP
```

The WHILE statement is used to set up a loop that will execute as long as the
expression is true (nonzero). The loop continues until the expression is false (zero).

WHILE/LOOP loops may be nested to any level. Each LOOP will match the most recent WHILE.

Example:

```text
10 LET I = 0
20 WHILE I < 10
30   PRINT "I =" I
40   I = I + 1
50 LOOP
60 END
```

## Internal Functions

This section describes the functions that are available in NanoBasic in alphabetical order.

### CLRLINE

Format:

```text
CLRLINE(y-position)
```

The CLRLINE function is used to clear a line on the terminal. The cursor is positioned
at the beginning of the line.
`y-position` is the vertical position (1-20).

Example:

```text
10 CLRLINE(10)
20 PRINT "HELLO"
30 END
```

### CLRSCR

Format:

```text
CLRSCR()
```

The CLRCRS function is used to clear the screen.

### HEX$

Format:

```text
HEX$(number)
```

The HEX$ function is used to convert a number to a hexadecimal string.

Example:

```text
10 PRINT HEX$(255)

>> FF
```

### INPUT

Format:

```text
variable = INPUT("prompt")
```

The INPUT function is used to accept input from the user. This input accepts
numeric values only. The input is terminated by pressing the Enter key.

When an INPUT function is encountered, program execution pauses and a question
mark is printed to indicate the program is waiting for data.

The data that is entered is returned as the value of the INPUT function.

Example:

```text
10 A = INPUT("ENTER A NUMBER")
20 PRINT A
30 END
```

### INPUT$

Format:

```text
variable$ = INPUT$("prompt")
```

The INPUT$ function is used to accept input from the user. This input accepts
string values only. The input is terminated by pressing the Enter key.

When an INPUT$ function is encountered, program execution pauses and a question
mark is printed to indicate the program is waiting for data.

The data that is entered is returned as the value of the INPUT$ function.

Example:

```text
10 A$ = INPUT$("ENTER A STRING")
20 PRINT A$
30 END
```

### INSTR

Format:

```text
INSTR(string1, string2)
```

The INSTR function is used to find the position of a substring within a string.
The function returns the position of the first occurrence of string2 in string1.
If string2 is not found in string1, the function returns 0.

Example:

```text
10 PRINT INSTR("HELLO","L")

>> 3
```

### LEFT$

Format:

```text
LEFT$(string, length)
```

The LEFT$ function is used to extract the left part of a string.

Example:

```text
10 A$="HELLO"
20 PRINT LEFT$(A$,2)
30 END

>> HE
```

### LEN

Format:

```text
LEN(string)
```

The LEN function is used to determine the length of a string.

Example:

```text
10 A$="HELLO"
20 PRINT LEN(A$)
30 END

>> 5
```

### MID$

Format:

```text
MID$(string, start, length)
```

The MID$ function is used to extract a substring from a string.

`string` is the string from which the substring is to be extracted.
`start` is the starting position of the substring (0-n).
`length` is the length of the substring (1-n).

Example:

```text
10 A$="HELLO"
20 PRINT MID$(A$,2,2)
30 END

>> LL
```

### RIGHT$

Format:

```text
RIGHT$(string, length)
```

The RIGHT$ function is used to extract the right part of a string.

Example:

```text
10 A$="HELLO"
20 PRINT RIGHT$(A$,2)
30 END

>> LO
```

### RND

Format:

```text
RND(number)
```

The RND function is used to generate a random number between 0 and number-1.

Example:

```text
10 PRINT RND(100)
20 END
```

### SERCUR

Format:

```text
SERCUR(x-position, y-position)
```

The SERCUR function is used to set the cursor position on the terminal.
`x-position` is the horizontal position (1-60).
`y-position` is the vertical position (1-20).

Example:

```text
10 SERCUR(10,10)
20 PRINT "HELLO"
30 END
```

### SLEEP

Format:

```text
SLEEP(seconds)
```

The SLEEP function is used to pause program execution for a specified number of seconds.

### SPC

Format:

```text
SPC(number)
```

The SPC function is used to print a number of spaces.

Example:

```text
10 PRINT "HELLO";SPC(5);"WORLD"
20 END

>> HELLO     WORLD
```

### STR$

Format:

```text
STR$(number)
```

The STR$ function is used to convert a number to a string.

Example:

```text
10 PRINT STR$(100)
20 END

>> 100
```

### STRING$

Format:

```text
STRING$(number, character)
```

The STRING$ function is used to create a string of a specified length filled
with a specified character.

Example:

```text
10 PRINT STRING$(5,"*")
20 END

>> *****
```

### TIME

Format:

```text
TIME()
```

The TIME function is used to return the current time in seconds since start of the Minetest server.

### VAL

Format:

```text
VAL(string)
```

The VAL function is used to convert a string to a number.

Example:

```text
10 PRINT VAL("100")
20 END

>> 100
```

## Techage Functions

This section describes the functions that are available in NanoBasic to interact with
the Techage machines and devices.

### BCMD

Format:

```text
BCMD(node_number, cmnd, pay_load_array)
```

The BCMD function is used to send Beduino-like commands to a Techage machine.
`node_number` is the number of the machine.
`cmnd` is the numeric command to be sent.
`pay_load_array` is an array of numeric values to be sent.
If no payload data is to be sent, NIL is used.

The BCMD function uses the Techage commands from the Beduino Controller.
Instead of string commands, Beduino uses numeric commands and responses.
This can make it easier to compose commands and evaluate the response.

But NanoBasic functions are strongly typed. The `BCMD` function expects a numeric
command and a numeric response. Not all Beduino commands are numeric.
If the command is not numeric, the `CMD$` function must be used.

All Beduino commands are described in [BEP 005: Techage Commands](https://github.com/joe7575/beduino/blob/main/BEPs/bep-005_ta_cmnd.md)

The return value of the `BCMD` function is the response status from the machine.
The status is a numeric value that indicates the success or failure of the command.

Return values:

- 0 = success
- 1 = error: Invalid node number or machine has no command interface
- 2 = error: Invalid command or payload data
- 3 = error: command execution failed
- 4 = error: Machine is protected (no access)
- 5 = e
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
rror: Invalid command response type (e.g. string)

Example:

```text
10 DIM arr(2)
20 arr(0)=1
30 PRINT BCMD(2331, 2, arr)
40 END

>> 0
```

### CMD$

Format:

```text
CMD$(node_number, "cmnd", "payload")
```

The CMD$ function is used to send a command to a Techage machine.
`node_number` is the number of the machine.
`cmnd` is the command to be sent.
`payload` is the data to be sent. If no data is to be sent, an empty string is used.

The return value of the CMD$ function is the response string from the machine.

The CMD$ function uses the Techage commands from the Lua Controller. The commands
from the Lua Controller are typically string commands. The `CMD$` function is used
to send these commands and evaluate the response.
If the command and/or response is numeric, the `BCMD` function must be used.

The commands re described in the Techage documentation.
See [Techage Command Functions](https://github.com/joe7575/techage/blob/master/manuals/ta4_lua_controller_EN.md#techage-command-functions)

Example:

```text
10 PRINT CMD$(426, "state", "")
20 END

>> blocked
```

