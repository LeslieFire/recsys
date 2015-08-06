package com.leslie.reducer;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

import org.apache.hadoop.mapreduce.Reducer;
import org.apache.mahout.cf.taste.hadoop.RecommendedItemsWritable;
import org.apache.mahout.cf.taste.impl.recommender.ByValueRecommendedItemComparator;
import org.apache.mahout.cf.taste.impl.recommender.GenericRecommendedItem;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.Vector;
import org.apache.mahout.math.Vector.Element;
import org.apache.mahout.math.VectorWritable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * merge all partial userRecomVector and generate user recommendation list
 * @author leslie
 */
public class CalUserRecommReducer extends Reducer<VarLongWritable, VectorWritable, VarLongWritable, RecommendedItemsWritable>{
	private static final Logger logger = LoggerFactory.getLogger(CalUserRecommReducer.class);
	private int recommendsPerUser;
	@Override
	protected void reduce(VarLongWritable userID, Iterable<VectorWritable> UserRecomCols, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		
		Vector recommendVector = null;
		for(VectorWritable UserRecomCol: UserRecomCols){
			recommendVector = (recommendVector == null)? UserRecomCol.get() : recommendVector.plus(UserRecomCol.get());
		}
		
		Queue<RecommendedItem> topItems = new PriorityQueue<RecommendedItem>(recommendsPerUser+1, ByValueRecommendedItemComparator.getInstance());
		Iterator<Element> it = recommendVector.iterateNonZero();
		while(it.hasNext()){
			Element e = it.next();
			int itemID = e.index();
			float prefValue = (float) e.get();
			if (topItems.size() < recommendsPerUser){
				topItems.add(new GenericRecommendedItem(itemID, prefValue));
			}else if (prefValue > topItems.peek().getValue()){
				topItems.poll();
				topItems.add(new GenericRecommendedItem(itemID, prefValue));
			}
		}
		
		List<RecommendedItem> recommendations = new ArrayList<RecommendedItem>(topItems.size());
		recommendations.addAll(topItems);
		Collections.sort(recommendations, ByValueRecommendedItemComparator.getInstance());
		
		//logger.info(userID + " " + new RecommendedItemsWritable(recommendations));
		context.write(userID, new RecommendedItemsWritable(recommendations));
	}

	@Override
	protected void setup(Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		super.setup(context);
		recommendsPerUser = context.getConfiguration().getInt("recommendItems.recommendationsPerUser", 10);
	}
	
	
}
