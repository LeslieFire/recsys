package com.leslie.mapper;

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.mahout.cf.taste.hadoop.item.VectorOrPrefWritable;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.Vector.Element;
import org.apache.mahout.math.VectorWritable;

/**
 * split user vector, for the merge with coocurrence vector
 * mapper input format :<userID,Vector<itemIDIndex,preferenceValuce>....>
 * reducer output format :<itemID,Vecotor<userID,preferenceValuce>....> 
 * @author leslie
 */
public class ItemUserScoreSplitMapper extends Mapper<VarLongWritable, VectorWritable, IntWritable, VectorOrPrefWritable>{

	@Override
	protected void map(VarLongWritable userIDWritable, VectorWritable itemPrefs, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		long userId = userIDWritable.get();
		Iterator<Element> it = itemPrefs.get().iterateNonZero();
		while(it.hasNext()){
			Element e = it.next();
			int itemId = e.index();
			float prefValue = (float)e.get();
			
			context.write(new IntWritable(itemId), new VectorOrPrefWritable(userId, prefValue));
		}
	}
	
	
}
