from fractions import Fraction

def toint(literal):
	#print("literal:",literal)
	literaltointegerdict={key:value for key,value in zip(['a','b','c','d','e','f','g','h','i','j'],[0,1,2,3,4,5,6,7,8,9])}
	#print("literaltointegerdict:",literaltointegerdict)
	return literaltointegerdict[literal]

def sequence_to_fraction(stringsequence):
	integersequence=[str(toint(x)) for x in stringsequence]
	print("integersequence:",integersequence)
	decimalfraction=float(int("".join(integersequence))/(10**len(integersequence)))
	print("decimalfraction:",decimalfraction)
	fraction=Fraction(decimalfraction)
	return fraction

if __name__=="__main__":
	#With no repetitions
        fraction=sequence_to_fraction("abcdefghijjabcdfghifghiabcdeffghiabcddcefaeeffggabcdefghijjabcdfghifghiabcdeffghiabcddcefaeeffggabcdefghijjabcdfghifghiabcdeffghiabcddcefaeeffgg")
        print("Non-repeating sequence - fraction:",fraction)
        print("----------------------------------------------------------")
	#With repetitions
        fraction=sequence_to_fraction("abbabbabbabbabbabbabbabbabbabbabbabbabbabbabb")
        print("Repeating sequence - fraction:",fraction)
        print("----------------------------------------------------------")
	#With no repetitions
        fraction=sequence_to_fraction("abcdefghijjbcdfegabbcddfgghhhabbiiijjjddccchhaabbjjaaaa")
        print("Non-repeating sequence - fraction:",fraction)
        print("----------------------------------------------------------")
	#With repetitions
        fraction=sequence_to_fraction("abababababababababababababababababababababababababababababababababababababababababab")
        print("Repeating sequence - fraction:",fraction)
        print("----------------------------------------------------------")
	#With repetitions
        fraction=sequence_to_fraction("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
        print("Repeating sequence - fraction:",fraction)
        print("----------------------------------------------------------")
	#With no repetitions
        fraction=sequence_to_fraction("abcdefghij")
        print("Non-repeating sequence - fraction:",fraction)
        print("----------------------------------------------------------")
