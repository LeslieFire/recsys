package com.leslie.mapper;

import java.io.IOException;
import java.util.List;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.mahout.cf.taste.hadoop.item.VectorAndPrefsWritable;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.Vector;
import org.apache.mahout.math.VectorWritable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Matrix Concurrent Computation
 * @author leslie
 */
public class CalUserRecommMatMapper extends Mapper<IntWritable, VectorAndPrefsWritable, VarLongWritable, VectorWritable>
{
	private static final Logger logger = LoggerFactory.getLogger(CalUserRecommMatMapper.class);

	@Override
	protected void map(IntWritable itemId, VectorAndPrefsWritable value, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		Vector coocMatCol = value.getVector();
		List<Long> userIDs = value.getUserIDs();
		List<Float> prefsValues = value.getValues();
		
		for (int i = 0; i < userIDs.size(); ++i){
			Long userId = userIDs.get(i);
			Float prefValue = prefsValues.get(i);
			//logger.info("userId " + userId);
			//logger.info("prefValue " + prefValue);
			
			Vector UserRecomVectorPartialScores = coocMatCol.times(prefValue);
			context.write(new VarLongWritable(userId), new VectorWritable(UserRecomVectorPartialScores));
		}
	}
	
	
}
