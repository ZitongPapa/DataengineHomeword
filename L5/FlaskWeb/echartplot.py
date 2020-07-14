import pyecharts.options as opts
from pyecharts.charts import WordCloud
import collections


# 输入csv，输出列表
def csv2list(csv):
    # 依次读取csv每行，将每行用','连接每行
    items=''
    with open(csv,'r') as f:
        for line in f.readlines():
            items=','.join([items,line.strip()])
    # 将字符串转为list   并使用切片去除首个空元素   
    word_list=items.split(',')
    word_list=word_list[1:]
    print('总共汇总 %s 个词汇'%len(word_list))
    return word_list


# 输入csv，获取词云html格式图
def get_html(in_csv,out_html,max_words):

  word_list=csv2list(in_csv)
  # 词频统计
  word_counts = collections.Counter(word_list) # 对分词做词频统计
  word_counts_top10 = word_counts.most_common(max_words) # 获取前10最高频的词
  print (word_counts_top10) # 输出检查
   

  data = word_counts_top10

  (
      WordCloud()
      .add(series_name="采购分析", data_pair=data)
      .set_global_opts(
          title_opts=opts.TitleOpts(
              title="采购分析", title_textstyle_opts=opts.TextStyleOpts(font_size=20)
          ),
          tooltip_opts=opts.TooltipOpts(is_show=True),
      )
     
      .render(out_html)
      
  )




if __name__ == '__main__':

	get_html('test.csv','test.html')



