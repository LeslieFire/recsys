package com.leslie.reducer;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.mahout.cf.taste.hadoop.item.VectorOrPrefWritable;
import org.apache.mahout.math.RandomAccessSparseVector;
import org.apache.mahout.math.Vector;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ItemCoocMatReducer extends Reducer<IntWritable, IntWritable, IntWritable, VectorOrPrefWritable>{
	private static final Logger logger = LoggerFactory.getLogger(ItemCoocMatReducer.class);

	@Override
	protected void reduce(IntWritable mainItemID, Iterable<IntWritable> coocItems, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		Vector coocVector = new RandomAccessSparseVector(Integer.MAX_VALUE, 100);
		for (IntWritable coocItem : coocItems){
			int itemID = coocItem.get();
			coocVector.set(itemID, coocVector.get(itemID) + 1.0);
		}
		//logger.info(mainItemID + " " + new VectorOrPrefWritable(coocVector));
		context.write(mainItemID, new VectorOrPrefWritable(coocVector));
	}
	
	
}
