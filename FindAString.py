"""In this challenge, the user enters a string and a substring. You have to print
the number of times that the substring occurs in the given string. String
traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

****Input Format****

The first line of input contains the original string. The next line contains
the substring.

****Constraints****
1<=len(String)<=200
 
Each character in the string is an ascii character.

****Output Format****

Output the integer number indicating the total number of occurrences of the
substring in the original string."""




def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i]== sub_string[0]:
            x=i
            flag=True
            for j in range(len(sub_string)):
                if string[x]!=sub_string[j]:
                    flag=False
                    break
                x+=1
            if flag==True:
                count+=1
    return count
string=input("Enter the string:")
sub_string=input("Enter the substring whose frequency has to be found:")
print ("%s occurs in %s %d times" % (sub_string,string,count_substring(string,sub_string)))

