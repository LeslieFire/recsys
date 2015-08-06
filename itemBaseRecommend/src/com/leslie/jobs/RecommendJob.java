package com.leslie.jobs;

import java.io.IOException;


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
import org.apache.mahout.cf.taste.hadoop.RecommendedItemsWritable;
import org.apache.mahout.cf.taste.hadoop.item.VectorAndPrefsWritable;
import org.apache.mahout.cf.taste.hadoop.item.VectorOrPrefWritable;
import org.apache.mahout.math.VarLongWritable;
import org.apache.mahout.math.VectorWritable;

import com.leslie.Util.HadoopUtil;
import com.leslie.combiner.CalUserRecommCombiner;
import com.leslie.mapper.CalUserRecommMatMapper;
import com.leslie.mapper.CombineCoocMatAndItemUserScoreMapper;
import com.leslie.mapper.ItemCoocMatMapper;
import com.leslie.mapper.ItemUserScoreSplitMapper;
import com.leslie.mapper.UserItemScoreMapper;
import com.leslie.reducer.CalUserRecommReducer;
import com.leslie.reducer.CombineCoocMatAndItemUserScoreReducer;
import com.leslie.reducer.ItemCoocMatReducer;
import com.leslie.reducer.UserItemScoreReducer;


/**
 * @author leslie
 */
public class RecommendJob extends Configured implements Tool{
	String[] dataSourceInputPath = {"itemBaseRecommend/sourceData"};
    String[] userItemScoreMatOutPath = {"itemBaseRecommend/user_vector_output/"};
    String[] itemUserScoreVectorOutPath = {"itemBaseRecommend/user_vector_split_output/"};
    String[] coocMatOutPath = {"itemBaseRecommend/CooccurrenceMatrixOuptPath/"};
    String[] combineCoocMatAndItemUserScoreOutPath = {"itemBaseRecommend/combineUserVectorAndCoocMatrixOutPutPath"};
    String[] calUserRecommendationsOutPath = {"itemBaseRecommend/CaclPartialRecomUserVectorOutPutPath"};
    //String[] dataSourceInputPath = {"train_data0"};
//    String[] userItemScoreMatOutPath = {"user_item_score_mat_output/"};
//    String[] itemUserScoreVectorOutPath = {"item_user_score_vector_output/"};
//    String[] coocMatOutPath = {"cooc_mat_output/"};
//	String[] combineCoocMatAndItemUserScoreOutPath = {"combine_cooc_mat_and_item_user_score_output/"};
//	String[] calUserRecommendationsOutPath = {"cal_user_recommendations_output/"};

	
	@Override
	public int run(String[] arg0) throws Exception {
		// TODO Auto-generated method stub
		Configuration conf=getConf(); 
        setup(conf);
        
        // step 1
        Job SourceDataToUserItemPrefsJob = HadoopUtil.prepareJob(
                  "SourceDataToUserItemPrefsJob",
                    dataSourceInputPath, 
                    userItemScoreMatOutPath[0], 
                    TextInputFormat.class, 
                    UserItemScoreMapper.class, 
                    VarLongWritable.class, 
                    VarLongWritable.class, 
                    UserItemScoreReducer.class, 
                    VarLongWritable.class, 
                    VectorWritable.class, 
                    SequenceFileOutputFormat.class, 
                    conf);
 // step 2
        Job ItemCoocMatJob = HadoopUtil.prepareJob(
                  "ItemCoocMatJob",
                  	userItemScoreMatOutPath, 
                  	coocMatOutPath[0], 
                    SequenceFileInputFormat.class, 
                    ItemCoocMatMapper.class, 
                    IntWritable.class, 
                    IntWritable.class, 
                    ItemCoocMatReducer.class, 
                    IntWritable.class, 
                    VectorOrPrefWritable.class, 
                    SequenceFileOutputFormat.class, 
                    conf);
        // step 3
        Job ItemUserScoreSplitJob = HadoopUtil.prepareJob(
                "ItemUserScoreSplitJob",
                 userItemScoreMatOutPath, 
                  itemUserScoreVectorOutPath[0], 
                  SequenceFileInputFormat.class, 
                  ItemUserScoreSplitMapper.class, 
                  IntWritable.class, 
                  VectorOrPrefWritable.class, 
                  SequenceFileOutputFormat.class, 
                  conf);
        
        String[] combineCoocMatAndItemUserScoreInputPath = {coocMatOutPath[0],itemUserScoreVectorOutPath[0]};
        Job combineCoocMatAndItemUserScoreJob = HadoopUtil.prepareJob(
                  "combineCoocMatAndItemUserScoreJob",
                  combineCoocMatAndItemUserScoreInputPath,
                  combineCoocMatAndItemUserScoreOutPath[0], 
                    SequenceFileInputFormat.class, 
                    CombineCoocMatAndItemUserScoreMapper.class, 
                    IntWritable.class, 
                    VectorOrPrefWritable.class, 
                    CombineCoocMatAndItemUserScoreReducer.class, 
                    IntWritable.class, 
                    VectorAndPrefsWritable.class, 
                    SequenceFileOutputFormat.class, 
                    conf);
        
        Job calUserRecommJob= HadoopUtil.prepareJob(
                "calUserRecommJob",
                combineCoocMatAndItemUserScoreOutPath,
                calUserRecommendationsOutPath[0], 
                SequenceFileInputFormat.class, 
                  CalUserRecommMatMapper.class, 
                  VarLongWritable.class, 
                  VectorWritable.class, 
                 // CalUserRecommCombiner.class,
                  CalUserRecommReducer.class, 
                  VarLongWritable.class, 
                  RecommendedItemsWritable.class, 
                  TextOutputFormat.class, 
                  conf);
  
        
        if(SourceDataToUserItemPrefsJob.waitForCompletion(true)){
            if(ItemCoocMatJob.waitForCompletion(true)){
                if(ItemUserScoreSplitJob.waitForCompletion(true)){
                    if(combineCoocMatAndItemUserScoreJob.waitForCompletion(true)){
                         int rs = calUserRecommJob.waitForCompletion(true) ? 1 :0;
                        return rs;
                    }else{
                        throw new Exception("merge cooc and user split vector failed");
                    }
                }else{
                    throw new Exception("split user vector failed");
                }
            }else{
                throw new Exception("calculate cooc matrix failed");
            }
        }else{
            throw new Exception("compute user item score mat failed");
        }
	}
	
	protected void setup(Configuration configuration)
			throws IOException, InterruptedException{
		//FileSystem hdfs = FileSystem.get(URI.create("hdfs://0.0.0.0"), configuration);
		FileSystem hdfs = FileSystem.get(configuration);
		Path p1 = new Path(userItemScoreMatOutPath[0]);
		Path p2 = new Path(itemUserScoreVectorOutPath[0]);
		Path p3 = new Path(coocMatOutPath[0]);
		Path p4 = new Path(combineCoocMatAndItemUserScoreOutPath[0]);
		Path p5 = new Path(calUserRecommendationsOutPath[0]);
		
		if (hdfs.exists(p1)) {
            hdfs.delete(p1, true);
        } 
		if (hdfs.exists(p2)) {
            hdfs.delete(p2, true);
        } 
		if (hdfs.exists(p3)) {
            hdfs.delete(p3, true);
        } 
		if (hdfs.exists(p4)) {
            hdfs.delete(p4, true);
        } 
		if (hdfs.exists(p5)) {
            hdfs.delete(p5, true);
        } 
	}
	public static void main(String[] args) throws IOException, 
			ClassNotFoundException, InterruptedException{
		try{
			int returnCode = ToolRunner.run(new RecommendJob(), args);
			System.exit(returnCode);
		} catch (Exception e){
			
		}
	}
}
