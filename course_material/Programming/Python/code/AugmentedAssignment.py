##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
# K.Srinivasan
# Krishna iResearch - https://www.krishna-iresearch.org/ 
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io
##############################################################################################################################################

def augmented_assignment():
    x1=[10]
    x2=[10]
    print("1) x1:",x1)
    y1 = x1
    print("2) y1:",y1)
    x1 = x1 + [11]
    print("3) After normal assigment (x1 + [11])  - x1:",x1)
    print("4) After normal assignment (x1 + [11]) - y1 (copy - differs from x1):",y1)
    print("5) x2:",x2)
    y2 = x2
    print("6) y2:",y2)
    x2 += [11] 
    print("6) After augmented assigment (x1 + [11]) - x2:",x2)
    print("7) After augmented assignment (x1 + [11]) - y2 (in place - same as x2):",y2)

if __name__=="__main__":
    augmented_assignment()

