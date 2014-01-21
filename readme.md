# wordpress2tumblr script

A script set to upload wordpress content xml into tumblr.

- You don't need to use email address and password but this script need a set oauth keys and tokens.
- You can get the key and tokens from Tumblr registration of application.

## How to use

### Getting Oauth key and tokens from Tumblr

you need to register a dummy application to Tumblr. It's not for making an real application, it's just to have keys and tokens to use this script. without this step, it's too comlicated to use Oauth to connect Tumblr.

1. go to the below page. and register a dummy application

	[http://www.tumblr.com/oauth/apps](http://www.tumblr.com/oauth/apps)

2. you can find a link 'Explore API' under your dummy application name. click the link.

3. after that, you will be reached the below page with 'Show Keys' buttion right upper place on the page. click the button.

	[https://api.tumblr.com/console//calls/user/info](https://api.tumblr.com/console//calls/user/info)

4. finally, you can get 5 keys and tokens from a small window as like below.
	<pre><code>Consumer Key xxxxx.......
Consumer Secret xxxxx.......
Token xxxxx........
Token Secret xxxxx.......
API Key xxxxx.......
</code></pre>
	> Cunsumer Key has same value with API key
5. Copy the keys and tokens. and then, paste it into wordpress2tumblr.conf file.
6. **Warning!** don't deploy or give this keys other people.

### Download Wordpress content XML file

1. Go to the admin page of your Wordpress blog
2. Download the XML file using Tool menu in the admin page

### Run script

<pre><code>wordpress2tumblr.py -c upload my-config.conf wordpress-xml-file
</code></pre>

## References

Tumblr API document

- [http://www.tumblr.com/docs/en/api/v2#auth](http://www.tumblr.com/docs/en/api/v2#auth)
