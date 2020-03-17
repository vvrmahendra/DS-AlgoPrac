"""Pretty Json
Given a string A representating json object. Return an array of string denoting json object with proper indentaion. Rules for proper indentaion:
Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional '\t'
Note:
[] and {} are only acceptable braces in this case.
Assume for this problem that space characters can be done away with.

Input Format
The only argument given is the integer array A.
Output Format
Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.
For Example
Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    { 
        A:"B",
        C: 
        { 
            D:"E",
            F: 
            { 
                G:"H",
                I:"J"
            } 
        } 
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo", 
        {
            "bar":
            [
                "baz", 
                null, 
                1.0, 
                2
            ]
        }
    ]"""

def prettyJSON(A):
    indent = 0
    ans = []
    chunk = ""
    for i in A:
        if i == '{' or i == '[':
            if chunk != "":
                ans.append("\t"*indent+chunk)
            
            ans.append("\t"*indent+i)
            indent += 1
            chunk = ""
        elif i == ',':
            if chunk != "":
                ans.append("\t"*indent+chunk+i)
            else:
                ans[-1] = ans[-1]+','
            
                
            chunk = ""
            
        elif i == ']' or i == '}':
            if chunk != "":
                ans.append("\t"*indent+chunk)
            indent -= 1
            ans.append('\t'*indent+i)
            chunk = ""
        else:
            chunk = chunk+i
            
    return ans