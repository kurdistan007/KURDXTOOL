ó
ÿc           @   s   e  Z e r# d  d  Z   Z n  yÜ d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z WnR e k
 rSe j d  e j d  e j d  e j d	  e j d
  n Xe e  e j d  e j   Z e j e   e j e j j   d d d g e _ d   Z  d   Z! d   Z" d   Z# d Z$ d   Z% d  Z& g  Z' d   Z( d   Z) d   Z* e+ d k re(   n  d S(   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   pip2 install requestss   git pull origin mastert   clears   pip2 install mechanizes   python2 kurdxtool.pyt   utf8t   max_timei   s
   User-Agents·   Mozilla/5.0 (Linux; Android 10; STK-L21; HMSCore 5.0.5.300; GMSCore 20.47.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.4.302 Mobile Safari/537.36c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   395122620o.pyR      s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   395122620o.pyt   acak    s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   395122620o.pyR   )   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   395122620o.pyt   hamza4   s    s  
[1;96m    ______   ____    _____ 
[1;96m   |  ____| |  _ \  |_   _|
[1;96m   | |__    | |_) |   | |  
[1;96m   |  __|   |  _ <    | |  
[1;96m   | |      | |_) |  _| |_ 
[1;96m   |_|      |____/  |_____|

                                                
[1;91m-----------------------------------------------
[1;92mâ£ OWNER      :  KURD X TOOL 
[1;92mâ£ Dev        :  Biyar Hussein
[1;92mâ£ Facebook   :  Biyar Hussein
[1;92mâ£ Telegarm   :  Biyar007
[1;91m-----------------------------------------------c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [â] Logging In i   (   R   R   R   R   R   (   t   titikt   o(    (    s   395122620o.pyt   tik=   s
    c          C   s0  t  j d  t GHt d  }  |  d k rL t  j d  t GHd |  d GHn d GHt j d  t   t d  } | d k r¹ t  j d  t GHd |  d GHd	 | d
 GHt j d  n d GHt j d  t   y  t d d  } t  j d  Wn t t	 f k
 rt
   n Xd GHt j d  t   d  S(   NR   s   [+] TOOL USERNAME: t   byokurds   [â] TOOL USERNAME: s
    (correct)s   [!] Invalid Username.i   s   [+] TOOL PASSWORD: s   [â] TOOL PASSWORD: s     (correct)i   s   [!] Invalid Password.s	   login.txtt   rs   python2 .fbikurd.pys   [!] Invalid Password(   R   t   systemt   bannert	   raw_inputR   R   t   tlogint   opent   KeyErrort   IOErrort   methodlogin(   t   usernamet   passwt   toket(    (    s   395122620o.pyR*   I   s8    c          C   s8  t  j d  t GHd GHd GHd GHd GHt d  }  |  d k rM d GHt   nç |  d	 k rc t   nÑ |  d
 k ré t  j d  t GHt d  } t   t d d  } | j |  | j	   d GHt
 j d  t  j d  t  j d  nK |  d k rt  j d  t  j d  n" |  d k r(t   n d GHt   d  S(   NR   s   [1] Login With ID/Password.s   [2] Login Using Token.s	   [0] Exit.s         s   
Choose Option >>  R
   s   [!]  Wrong Inputt   1t   2s   [+] Give Token : s	   login.txtR   s   
[â] Logged In Successfully.i   s1   xdg-open https://www.facebook.com/biyarHussein007s   python2 .fbikurd.pyt   3s   python2 login.pyt   0s   [!] Wrong Input(   R   R'   R(   R)   R   t   loginR$   R+   R   t   closeR   R   (   t   host   hospt   hopa(    (    s   395122620o.pyR.   k   s>    



c          C   s  t  j d  y  t d d  }  t  j d  WnXt t f k
 rt  j d  t GHt d  t d  d GHt d  } | j d	 d
  } t d  } t	   t
 j d | d | d  } t j |  } d | k r?t d d  } | j | d  | j   d GHt j d  t  j d  t  j d  t  j d  qd | d k rkd GHt j d  t   qd GHt j d  t   n Xd  S(   NR   s	   login.txtR&   s   python2 .fbikurd.pys   [!] KURD X TOOLs'   [!] Use a New Facebook Account To Logins%   -------------------------------------s   [+] Number/Email: t    R
   s   [+] Password : s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokenR   s   
[â] Logged In Successfully.i   s1   xdg-open https://www.facebook.com/biyarHussein007s   www.facebook.comt	   error_msgs*   [!] User Must Verify Account Before Login.i   s&   [!]Number/User Id/ Password Is Wrong !(   R   R'   R+   R,   R-   R(   R!   R)   R   R$   t   brt   jsont   loadR   R7   R   R   R6   (   t   tbt   iidt   idt   pwdt   dataR   t   st(    (    s   395122620o.pyR6      s@    



t   __main__(   s
   User-Agents·   Mozilla/5.0 (Linux; Android 10; STK-L21; HMSCore 5.0.5.300; GMSCore 20.47.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.4.302 Mobile Safari/537.36(,   t   Falset   foot   barR   R   R   t   datetimeR   t   hashlibt   ret	   threadingR?   t   urllibt	   cookielibt   getpasst	   mechanizet   requestst   multiprocessing.poolR    t   requests.exceptionsR   R   t   ImportErrorR'   t   reloadt   setdefaultencodingR>   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   R(   R$   t   backRC   R*   R.   R6   t   __name__(    (    (    s   395122620o.pyt   <module>   sB   
¨
								"	#	$