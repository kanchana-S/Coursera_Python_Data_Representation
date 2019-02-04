# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:02:43 2019

@author: Kanchana

Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
IDENTICAL = -1

def singleline_diff(line1, line2):
    
    """Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.  
"""
    if len(line1) < len(line2):
        line1,line2 = line2, line1
    for iterate in range(len(line2)):
        if line1[iterate] != line2[iterate]:
            return iterate
    if len(line1) != len(line2):
        return len(line2)
    return IDENTICAL

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    format_str=""
    if(0<=idx<=min(len(line1),len(line2))):
        format_str= format_str+line1+"\n"
        for _ in range(idx):
            format_str= format_str + "="
        format_str+="^\n"
        format_str=format_str + line2+"\n"
    elif("\n" in line1 or "\n" in line2):
        return ""
    elif("\r" in line1 or "\r" in line2):
        return ""
    elif(idx<0):
        return ""
    return format_str


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    line1_list = lines1[:]
    line2_list = lines2[:]
    iterate=0
    cnt = 0
    if(len(line1_list) < len(line2_list)):
        line1_list,line2_list = line2_list,line1_list
    for iterate in range(len(line2_list)):
        idx = singleline_diff(line1_list[iterate], line2_list[iterate])
        if(idx==-1):
            cnt=1
        else:
            return (iterate,idx)
    if(cnt==1 and len(line1_list)!=len(line2_list)):
        return (len(line2_list),0)
    elif(len(line1_list)!=len(line2_list) and cnt==0):
        return(0,0)
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_=[]
    datafile= open(filename,"rt")
    for line in datafile.readlines():
        line=line.strip("\n")
        line=line.strip("\r")
        list_.append(line)
    datafile.close()
    return list_


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    line,idx = multiline_diff(list1,list2)
    if(line==IDENTICAL or idx==IDENTICAL or filename1==filename2):
        return "No differences\n"
    else:
        final_list = ""
        final_list+= "Line {0}:\n".format(line)
        if(list1=="" or len(list1)<line):
            string_frmt = singleline_diff_format("",list2[line],idx)
            final_list+=string_frmt
            return final_list
        elif(list2=="" or len(list2)<line):
            string_frmt = singleline_diff_format(list1[line],"",idx)
            final_list+=string_frmt
            return final_list
        elif(list1=="" and list2==""):
            string_frmt = singleline_diff_format("","",idx)
            final_list+=string_frmt
            return final_list
        else:
            string_frmt=singleline_diff_format(list1[line],list2[line],idx)
            final_list+=string_frmt
            return final_list