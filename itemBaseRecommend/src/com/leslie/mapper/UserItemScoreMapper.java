package com.leslie.mapper;

import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.mahout.math.VarLongWritable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * mapper input format : userID itemID1 itemID2 itemID3....
 * mapper ouput format : <userID,itemID>
 * @author leslie
 */
public class UserItemScoreMapper extends Mapper<LongWritable, Text, VarLongWritable, VarLongWritable>{
	private static final Logger logger = LoggerFactory.getLogger(UserItemScoreMapper.class);
	private static final Pattern NUMBER = Pattern.compile("(\\d+)");
	private String line = null;
	@Override
	protected void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		line = value.toString();
		if (line == null || line.length() == 0) return ;
		Matcher matcher = NUMBER.matcher(line);
		matcher.find();
		VarLongWritable userID = new VarLongWritable(Long.parseLong(matcher.group()));
		VarLongWritable itemID = new VarLongWritable();
		
		while(matcher.find()){
			itemID.set(Long.parseLong(matcher.group()));
			context.write(userID, itemID);
		}
		
		
	}
	
	
	
}
