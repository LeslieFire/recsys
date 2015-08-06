package com.leslie.mapper;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.mahout.cf.taste.hadoop.item.VectorOrPrefWritable;

/**
*
* mapper input format : <itemID,Vecotor<userID,preferenceValuce>> or <itemID,Vecotor<coocItemID,coocTimes>>
* mapper output format : <itemID,Vecotor<userID,preferenceValuce>/Vecotor<coocItemID,coocTimes>>
* @author leslie
*/
public class CombineCoocMatAndItemUserScoreMapper extends Mapper<IntWritable, VectorOrPrefWritable, IntWritable, VectorOrPrefWritable>{

	@Override
	protected void map(IntWritable key, VectorOrPrefWritable value, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		context.write(key, value);
	}
	
}
