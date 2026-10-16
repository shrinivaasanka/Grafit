import numpy as np
from scipy.linalg import lstsq

def compute_plane_equation(points):
	X_Y = points[:,:2]
	print("points[:]:",points[:])
	print("points[:,:]:",points[:,:])
	print("Select column index 2 - points[:,2]:",points[:,2])
	print("Select upto 1st column - points[:,:1]:",points[:,:1])
	print("Select upto 2nd row - points[:2,:]:",points[:2,:])
	print("Select row index 2 - points[2,:]:",points[2,:])
	print("X_Y:",X_Y)
	Z = points[:,2]
	print("Z:",Z)
	A = np.c_[X_Y, np.ones(X_Y.shape[0])]
	C,residues,rank,s = lstsq(A,Z)
	a,b,c=C
	print(f"Equation of the plane through points: z = {a}x + {b}y + {c}")

if __name__=="__main__":
	ThreeDgridPoints=np.random.rand(10,3)*10
	print("3D grid points:",ThreeDgridPoints)
	compute_plane_equation(ThreeDgridPoints)
