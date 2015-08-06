package com.leslie.reducer;

import java.io.IOException;

import org.apache.hadoop.mapreduce.Reducer;
import org.apache.mahout.math.RandomAccessSparseVector;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.Vector;
import org.apache.mahout.math.VectorWritable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * reducer input format : <userID,Iterable<itemID>>
 * reducer output format : <userID,VecotrWriable<index=itemID,valuce=pres>....>
 * @author leslie
 */
public class UserItemScoreReducer extends Reducer<VarLongWritable, VarLongWritable, VarLongWritable, VectorWritable>{
	private static final Logger logger = LoggerFactory.getLogger(UserItemScoreReducer.class);

	@Override
	protected void reduce(VarLongWritable userId, Iterable<VarLongWritable> items, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		
		Vector userVector = new RandomAccessSparseVector(Integer.MAX_VALUE, 100);
		for (VarLongWritable item : items){
			userVector.set((int)item.get(), 1.0f);
		}
		//logger.info(userId + " " + new VectorWritable(userVector));
		context.write(userId, new VectorWritable(userVector));
	}
}
