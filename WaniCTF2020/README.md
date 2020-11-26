# WaniCTF 2020 Write-up

WaniCTF2020に参加し、5問通すことができ、256チーム中 150位（507pt）でした。

とても楽しかったです。ありがとうございました。

以下、解いた問題や復習した問題の Write-up を書いていきたいと思います。

# Web

## [Web] DevTools_1 （100pt Beginner）
問題文:
```
ブラウザの開発者ツールを使ってソースコードをのぞいてみましょう！

https://devtools1[.]wanictf[.]org/
```

回答:
```
リンク先ページのHTMLソースに、Flagが書いてありました。
```

Flag:
```
FLAG{you_can_read_html_using_devtools}
```

## [Web] DevTools_2 （101pt Easy）
問題:
```
開発者ツールを使うと表示を書き換えることができます。

5000兆円欲しい！

(5000000000000000円持っていることにするとフラグを手に入れることができます。)

https://devtools2[.]wanictf[.]org
```

回答:
```
デベロッパーツールで該当のJavaScriptのソースを `5000000000000000` に書き換えたら、alert()が出てきました。そこにフラグが書いてあります。
```

Flag:
```
FLAG{you_can_edit_html_using_devtools}
```

## [Web] Simple Memo （101pt Beginner）

問題:
```
問題ページ：https://simple.wanictf.org/

flag.txtというファイルに私の秘密を隠したが、 完璧にサニタイズしたため辿りつける訳がない。

(注意)
simple_memo.zipは問題を解くために必須の情報ではなく、docker-composeを利用してローカルで問題環境を再現するためのものです。

興味のある方は利用してみてください。
```

回答:
```
URLの部分に `./flag.txt` を指定したら、フラグが入っているファイルが表示された。そこにフラグが書いてありました。
```

Flag:
```
FLAG{y0u_c4n_get_hi5_5ecret_fi1e}
```

## [Web] SQL Challenge 2 （105pt Hard）

問題:
```
問題ページ： https://sql2.wanictf.org/index.php?year=2011

やっぱり前のページは危ない気がするからページを作り直したよ。これで大丈夫だね。

sql-chall-2.zipは問題を解くために必須の情報ではなく、docker-composeを利用してローカルで問題環境を再現するためのものです。

興味のある方は利用してみてください。

```

回答:
```
URLのクエリを ?year=years にして送信してみると、フラグが出力されたページが出てきました。
```

Flag:
```
FLAG{5ql_ch4r_cf_ca87b27723}
```


# Crypto

問題文:
```
```

# Pwn

### [Pwn] netcat （101pt Beginner)

問題文:
```
`nc netcat.wanictf.org 9001`

- netcat (nc)と呼ばれるコマンドを使うだけです。
- つないだら何も表示されなくても知っているコマンドを打ってみましょう。

使用ツール例
- netcat (nc)

gccのセキュリティ保護
- Full RELocation ReadOnly (RELRO)
- Stack Smash Protection (SSP)有効
- No eXecute bit(NX)有効
-Position Independent Executable (PIE)有効
```

回答:
lsコマンドを打ち込んだら、
```
chall
flag.txt
redir.sh
```
と出力されたので、
```$ cat flag.txt```
コマンドを打ち込むと、Flagが出てきました。

Flag:
```
FLAG{netcat-1s-sw1ss-4rmy-kn1fe}
```
