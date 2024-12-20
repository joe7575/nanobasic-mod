# NanoBasic

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

## Commands, Statements, and Functions

This section describes the commands and statements that are available in NanoBasic in
alphabetical order.

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

### INPUT

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

### MID$

The MID$ function is used to extract a substring from a string.

Format:

```text
MID$(string, start, length)
```

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