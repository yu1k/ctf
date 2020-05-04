## De1CTF 2020

チームyuikで参加してました。Welcome問題，Web1問，Crypto1問の合計3個フラグを通せました。

### [Misc] this_is_flag

問題文 : Most flags are in the form flag{xxx}, for example:flag{th1s_!s_a_d4m0_4la9}

これはWelcome問題だと思います。フラグが問題文に書いてあったので、それを提出。

frag : flag{th1s_!s_a_d4m0_4la9}

### [Web]view_sourse

問題文 : 

X老师让小宁同学查看一个网页的源代码，但小宁同学发现鼠标右键好像不管用了。

指定のリンク先にアクセスしてサイトのソースコードを見てみるとフラグが書いてありました。それを提出。

flag : cyberpeace{9dba54ea370140048d7d15db71018cdb}

### [Crypto]base64

問題文 :

Description：元宵节灯谜是一种古老的传统民间观灯猜谜的习俗。 因为谜语能启迪智慧又饶有兴趣，灯谜增添节日气氛，是一项很有趣的活动。 你也很喜欢这个游戏，这不，今年元宵节，心里有个黑客梦的你，约上你青梅竹马的好伙伴小鱼， 来到了cyberpeace的攻防世界猜谜大会，也想着一展身手。 你们一起来到了小孩子叽叽喳喳吵吵闹闹的地方，你俩抬头一看，上面的大红灯笼上写着一些奇奇怪怪的 字符串，小鱼正纳闷呢，你神秘一笑，我知道这是什么了。

ファイルのリンクが貼ってあるので、そのリンクを踏んでファイルをダウンロード。

ダウンロードしたファイルに base64でエンコードされた文字列が入ってるので、その文字列をbase64でデコードしたらフラグが出てくるので、それを提出。

base64でデコードする前の文字列
Y3liZXJwZWFjZXtXZWxjb21lX3RvX25ld19Xb3JsZCF9

flag : cyberpeace{Welcome_to_new_World!}

ソースコードは [こちら](https://github.com/yu1k/ctf/blob/master/De1CTF2020/base64.py "こちら") です。