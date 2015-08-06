package com.leslie.combiner;

import java.io.IOException;

import org.apache.hadoop.mapreduce.Reducer;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.Vector;
import org.apache.mahout.math.VectorWritable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 *  @author leslie
 */
public class CalUserRecommCombiner extends Reducer<VarLongWritable, VectorWritable, VarLongWritable, VectorWritable>
{
	private static final Logger logger = LoggerFactory.getLogger(CalUserRecommCombiner.class);
	
	@Override
	protected void reduce(VarLongWritable userID, Iterable<VectorWritable> UserRecomPartialVectors, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		Vector userRecomCol = null;
		
		for (VectorWritable vector: UserRecomPartialVectors){
			userRecomCol = (userRecomCol == null) ? vector.get() : userRecomCol.plus(vector.get());
		}
		//logger.info(userID + " " + new VectorWritable(userRecomCol));
		context.write(userID, new VectorWritable(userRecomCol));
	}
	
}
