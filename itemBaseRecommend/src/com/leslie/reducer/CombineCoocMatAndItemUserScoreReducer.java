package com.leslie.reducer;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.mahout.cf.taste.hadoop.item.VectorAndPrefsWritable;
import org.apache.mahout.cf.taste.hadoop.item.VectorOrPrefWritable;
import org.apache.mahout.math.Vector;
import org.apache.mahout.math.Vector.Element;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * 
 * @author leslie
 */
public class CombineCoocMatAndItemUserScoreReducer extends Reducer<IntWritable, VectorOrPrefWritable, IntWritable, VectorAndPrefsWritable>{
	private static final Logger logger = LoggerFactory.getLogger(CombineCoocMatAndItemUserScoreReducer.class);

	@Override
	protected void reduce(IntWritable itemId, Iterable<VectorOrPrefWritable> values, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		
		List<Long> userIDs = new ArrayList<Long>();
		List<Float> prefValues = new ArrayList<Float>();
		Vector coocVector = null;
		Vector coocVectorTemp = null;
		Iterator<VectorOrPrefWritable> it = values.iterator();
		while(it.hasNext()){
			VectorOrPrefWritable e = it.next();
			coocVectorTemp = e.getVector();
			if (coocVectorTemp == null){
				userIDs.add(e.getUserID());
				prefValues.add(e.getValue());
			}else{
				coocVector = coocVectorTemp;
			}
		}
		if (coocVector != null){
			VectorAndPrefsWritable vectorAndPrefsWritable = new VectorAndPrefsWritable(coocVector, userIDs, prefValues);
			//logger.info(itemId.get() + " " + vectorAndPrefsWritable);
			context.write(itemId, vectorAndPrefsWritable);
		}
	}
	
	
}
