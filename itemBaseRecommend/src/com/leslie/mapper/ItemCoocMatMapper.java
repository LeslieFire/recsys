package com.leslie.mapper;

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.Vector;
import org.apache.mahout.math.VectorWritable;

/**
 * mapper input format : <userID,VecotrWriable<index=itemID,valuce=pres>....>
 * mapper output format :<itemID,itemID>(coocurrence id pair)
 * @author leslie
 */
public class ItemCoocMatMapper extends Mapper<VarLongWritable, VectorWritable, IntWritable, IntWritable>{

	@Override
	protected void map(VarLongWritable key, VectorWritable value, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		Iterator<Vector.Element> it = value.get().iterateNonZero();
		while(it.hasNext()){
			int itemA = it.next().index();
			
			Iterator<Vector.Element> it2 = value.get().iterateNonZero();
			while(it2.hasNext()){
				int itemB = it2.next().index();
				if (itemA == itemB) continue;	
				context.write(new IntWritable(itemA), new IntWritable(itemB));
			}
		}
	}
	
}
