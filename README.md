# 课表导入日历

## 用法

自己登录到学校教务处，把课表保存为`Class Schedule.html`；  
自己按google-calendar的教程搞个GAE，`credentials.json`和脚本放在同个文件夹内；  
最后运行`program.py`。  
成功！

## 事实

上google当然要挂代理啦。然而我用ssr竟然ssl握手错误，也没找到解决方案。  
不过奇妙的是：

+ 连接google api
+ 在linux上 √
+ win+C#+ssr √
+ win+py+sstap √
+ win+py+ssr/v2ray/goproxy ×

……

## 坑

### calendar

最开始想用本地的日历api的，但是没找到。  
遂用google-calendar。

### 课表

本来想直接用教务处下载的`.xls`文件的，我实在不想搞html，但是缺少节数，所以……  
遂不得已用html。

然后py+ssr就出错。不过也没事，我直接放在c9上跑了。

### google-calendar

但是，google也不让我省心。我不就请求频繁了一点吗，就被禁了。不得已，用`time.sleep()`。  
所以非常慢……

### 登录

自己复制html也太傻了吧，于是就想登录教务处。

但是奇妙的是登录统一认证的时候竟然需要验证码……（用浏览器看不到验证码。）

突然心累，虽然可以用tesserocr识别/保存到本地人眼识别，但是我现在不想搞了，就这样吧。

## 未来

要是不怕被我盗号的，我觉得可以挂在服务器上。学生提供学号，密码，google验证文件。

还有就是我改了课表html文件。因为周四全都是第一节，但事实上不是。不知道google-calendar如何检查重复。
