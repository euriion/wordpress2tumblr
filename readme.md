# wordpress2tumblr script

A script set to upload wordpress content xml into tumblr.

- you don't need to use email address and password but this script need a set oauth keys and tokens.
you can get the key and tokens from Tumblr registration of application

## Registration Application

> you need to register a dummy application to get oauth key at the below page
> it's not for making application, it's just to have oauth key and tokens

1. go to the below page. and register an application

http://www.tumblr.com/oauth/apps

2. you can find a link 'Explore API' under your dummy application name. click the link.

3. after that, you will be reached the below page with 'Show Keys' buttion right upper place on the page. click the button.

https://api.tumblr.com/console//calls/user/info

4. finally, you can get 5 keys and tokens from a small window as like below.

Consumer Key xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Consumer Secret yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Token Secret xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
API Key xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

5. copy the keys and tokens. and rewrite it into wordpress2tumblr.conf file as follow conf format.

6. don't deploy or give this keys other people.

## References

Tumblr API document

- http://www.tumblr.com/docs/en/api/v2#auth

