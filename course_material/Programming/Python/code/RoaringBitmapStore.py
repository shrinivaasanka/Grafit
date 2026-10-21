from roaringbitmap import RoaringBitmap

def execute_3SAT_query(ThreeCNFdatasets):
	queryresult=ThreeCNFdatasets[0][0] | ThreeCNFdatasets[0][1] | ThreeCNFdatasets[0][2]
	print("Clause 1 result:",queryresult)
	n=2
	for clause in ThreeCNFdatasets[1:]:
		clauseresult=clause[0] | clause[1] | clause[2]
		print("Clause",n,"result:",clauseresult)
		queryresult=queryresult & clauseresult
		n+=1
	print("Query result for the datasets in 3CNF:",queryresult)

if __name__=="__main__":
	dataset1=RoaringBitmap(range(10))
	dataset2=RoaringBitmap(range(9,20))
	dataset3=RoaringBitmap(range(1,7))
	dataset4=RoaringBitmap(range(5,30))
	dataset5=RoaringBitmap(range(5,10))
	dataset6=RoaringBitmap(range(1,20))
	dataset7=RoaringBitmap(range(10,100))
	dataset8=RoaringBitmap(range(1,40))
	dataset9=RoaringBitmap(range(10,60))
	#datasets is a 3CNF conjunctive formula with 3 bitmaps per disjunctive clause 
	datasets=[[dataset1,~dataset2,dataset3],[~dataset4,dataset5,dataset6],[dataset7,dataset8,~dataset9]]
	execute_3SAT_query(datasets)
