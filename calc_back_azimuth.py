import numpy as np

def baz(x0,y0,z0,x1,y1,z1):
	r0 = np.sqrt(x0**2+y0**2+z0**2)
	r1 = np.sqrt(x1**2+y1**2+z1**2)
	x0/=r0;y0/=r0;z0/=r0
	x1/=r1;y1/=r1;z1/=r1
	polevector = np.array([-z0*x0,-z0*y0,1-z0**2])
	poleaux = np.cross(polevector,[x0,y0,z0])
	print(polevector,poleaux)
	tmp = x0*x1+y0*y1+z0*z1
	targetvectors = np.array([x1-tmp*x0,y1-tmp*y0,z1-tmp*z0])
	proj = np.dot(targetvectors,polevector)
	proj_aux = np.dot(targetvectors,poleaux)
	return np.degrees(np.arctan2(proj_aux*np.sqrt(np.dot(polevector,polevector)),proj*np.sqrt(np.dot(poleaux,poleaux))))

print(baz(0,1,1,np.sqrt(2),0,2))
