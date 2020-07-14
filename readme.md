## 功能
- 运行run后，浏览器输入localhost或ip地址即可进入页面
- 输入需要显示的单词个数，上传csv文件，即可生成相应词云
- 强烈建议用chrome， ie或edge莫名其妙的慢

## 缺点与改进
- 代码简单，仅适合英文单词，csv形式，无泛化
- 时间精力有限 偷懒直接用pyechart生成html 正常打开姿势应该是js写前端，甚至不需要服务器读取＋出图全部由前端完成
- 选择不同的单词数都要重新提交数据，不利于网络传输，用js做dashboard或者用dash就不会存在这个问题

### L5 flask示例
![image](https://s1.ax1x.com/2020/07/14/UtoZEq.jpg)
![image](https://s1.ax1x.com/2020/07/14/UtoM2F.jpg)
