
def list_comprehension(arrayx,arrayy):
    z = [[x,y] for x in arrayx for y in arrayy]
    print("z:",z)
    z1 = [y for x in arrayx for y in x if y%2==0] 
    print("z1:",z1)
    z2 = [y for x in arrayy for y in x if y%2==0] 
    print("z2:",z2)
    string="thisisastring"
    z3 = [list(bin(ord(x)))[2:] for x in string]
    print("z3:",z3)
    z4 = [y for x in z3 for y in x]
    print("binary of ",string,":","".join(z4))

if __name__=="__main__":
    list_comprehension([[1,2],[3,4,5]],[[6,7,8],[9,10]])
