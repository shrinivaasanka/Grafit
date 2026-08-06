from sympy.utilities.iterables import kbins
from sympy.utilities.iterables import multiset_partitions 
from collections import defaultdict

def balanced_partitions(listofitems=[],maxdiff=2,bymajorityvote=True):
    #for partition in kbins(listofitems,2):
    for partition in multiset_partitions(listofitems):
        print("----------------------------------------------------------")
        if is_balanced(partition,maxdiff,bymajorityvote=bymajorityvote):
            print(str(len(partition))+"-part Balanced partition:",partition)
        else:
            print("Not a Balanced partition:",partition)

def is_balanced(partition,maxdiff,bymajorityvote):
    partitionbalances=defaultdict(int)
    partitionbalances[True]=partitionbalances[False]=0
    for part1 in partition:
        for part2 in partition:
            if part1 != part2: 
                if abs(sum(part1)-sum(part2)) <= maxdiff:
                    partitionbalances[True]+=1
                else:
                    partitionbalances[False]+=1
    print("partition ",partition," has partitionbalances:",partitionbalances)
    if bymajorityvote:
        if partitionbalances[True] > partitionbalances[False]:
             return True
        else:
             return False
    else:
        if partitionbalances[False] == 0:
             return True
        else:
             return False


if __name__=="__main__":
    print("---------------------------------------------------")
    print("Balanced partitions by roundrobin majority vote:")
    print("---------------------------------------------------")
    balanced_partitions([10,1,3,4,7,2,5],2,bymajorityvote=True)
    print("---------------------------------------------------")
    print("Balanced partitions by consensus:")
    print("---------------------------------------------------")
    balanced_partitions([10,1,3,4,7,2,5],2,bymajorityvote=False)
