# KyotoExpo CTF Write-up

ハッキングコンテスト in 京都スマートシティエキスポ2020 Write-up

## 参加結果

チーム yu1k で参加しました。5問解くことができ、89チーム中　52位（350ポイント）でした。

以下、解けた問題の Write-up です。

# [Crypto] 0 decode(Very Easy)

## 問題内容

```
RkxBR19reW90b3NtYXJ0Y2l0eWV4cG8=

 ハッカー集団によりハッキングされたホームページに謎の文字列が表示されている。
 調査の結果どうやらbase64でエンコードされているようだ。デコードしてみよう。
```

## 解き方

base64 デコードする。 ソースコードは [こちら（GitHub）](https://github.com/yu1k/ctf/blob/master/KyotoExpoCTF2020/crypto/0decode.py) です。

## フラグ:

```
FLAG_kyotosmartcityexpo
```

# [Network] 1-1 FTP(Very Easy)

## 問題内容

```
NASサーバに対して不正なアクセスの痕跡が見つかった。
通信内容を解析すれば何かが分かるかもしれない。pcapファイルを調べてみよう。
```

## 解き方

pcapファイルが渡される。そのpcapファイルを解析するとパケットのなかに平文でフラグが入っていました。

### フラグ:

```
FLAG_biHehUUnazQPt
```

# [Misc] 1-2 SSH avoidance(Very Easy)

## 問題内容

```
引き続きNASサーバの不正アクセス状況を調査している。
このSSH、簡単に侵入できそうだ。
```

## 解き方

サーバのIPアドレスと接続できるポートが渡される。

脆弱そうかつ適当なパスワードを入力し、侵入を試みてみる。

```
ユーザ:admin
パスワード:password
```

で侵入できた。

で以下の操作をし、フラグを得る。

```
admin@58d2aec14ceb:~$ ls

flag.txt  q6

admin@58d2aec14ceb:~$ cat flag.txt

FLAG_jbSSTdXTLCc4a
```

## フラグ:

```
FLAG_jbSSTdXTLCc4a
```

# [Web] 6-2 authentication avoidance(Easy)

## 問題文

```
ルータのログイン認証は簡単に突破できそうだ。

問題サーバー
http://18.177.208.49/
```

## 解き方

SQLi問題だと予想。

問題サイトのフォームに対して、SQLインジェクションを行う。

ユーザ名に `1' or '1' = '1';--` と入力したらログインをすることができました。

## フラグ:

```
FLAG_RqWGsVKFAQMUn
```

# [Network] 2-1 basic authentication(Easy)

## 問題

```
Webカメラへの不正アクセスの痕跡が見つかった。
通信をキャプチャしたので分析してみよう。
```

## 解き方

pcapファイルが渡される。そのpcapファイルを解析する。

問題の名前から basic認証を用いた認証だと予想。そこでpcapファイルの中に残されている、HTTPの通信のログを解析し、フラグを見つけました。

### フラグ:

```
FLAG_9sdnR5MH4iiGW
```