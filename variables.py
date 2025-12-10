s_subjects="maths"
s_subcode="1990"
sub = input("enter the subject :")
code = input("enter the code :")
def student():
    if s_subjects==sub and s_subcode==code:
        return True
    else:
        return False
a = student()
print(a)
     