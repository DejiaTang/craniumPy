import cranium
import multiprocessing as mp
import time
import os
import sys
from functools import partial
from random import randint

def transform_file(f): 

	print(f, 'starting')

	tic = time.time()

	s = cranium.brain()
	df = cranium.read_psi(f)
	s.add_aligned_df(df[['x','y','z']])
	s.transform_coordinates()

	cranium.write_data(f,s.df_align)

	print(f,'complete',time.time()-tic)


if __name__=='__main__':

	outdirs = [ "C:\\Users\\zfishlab\\Desktop\\zrf1wt13umyot21um\\yot\\PostThetaFix10_17"
	#"C:\\Users\\zfishlab\\Desktop\\zrf1wt13umyot21um\\wt\\PostThetaFix10_17"
		
	]

	for outdir in outdirs:

		files = os.listdir(outdir)

		os.chdir(outdir)

		n = len(files)
		for i in range(0,n,5):
			if i+5>n:
				L = files[i:n]
			else:
				L = files[i:i+5]

			pool = mp.Pool()
			pool.map(transform_file,L)
			pool.close()
			pool.join()

		print('Processing complete')