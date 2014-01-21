import urllib, urllib2, time, sys, os, getopt, types
import optparse
from xml.dom import minidom
from urllib2 import URLError, HTTPError
import pytumblr
import pprint
import json

'''
@Reference
https://github.com/tumblr/pytumblr
'''

class WordpressToTumblr:
    def __init__(self):
        self._tumblr_client = None
        self._config = None

    def connect(self):
        self._tumblr_client = pytumblr.TumblrRestClient(
            self._config['customer_key'],
            self._config['customer_secret'],
            self._config['token'],
            self._config['token_secret']
        )

        if self._tumblr_client is None:
            return False
        else:
            return True

    def load_config(self, config_filename):
        self._config = json.loads(open(config_filename).read())
        return

    def get_client_info(self):
        return (self._tumblr_client.info())

    def display_client_info(self):
        pprint.pprint(self.get_client_info())
        return

    def get_blog_posts(self, blog_name):
        return (self._tumblr_client.posts(blog_name, id=0, offset=0, limit=999999))

    def create_text(self, blog_name, title, body, date, tags):
        # res = self.client.create_text('euriion', tags=['hello', 'world'], body="asdfsdf")
        res = self._tumblr_client.create_text(blog_name, title=title, body=body, date=date, tags=tags)
        return (res)

    def upload_wordpress_file(self, wordpress_xml_filename):
        if not os.path.exists(wordpress_xml_filename):
            print 'WordPress xml file ' + wordpress_xml_filename + ' not found!'
            sys.exit(2)

        try:
            dom = minidom.parse(wordpress_xml_filename)
        except Exception, detail:
            print 'XML file must be well-formed. You\'ll need to edit the file to fix the problem.'
            print detail
            sys.exit(2)

        items = dom.getElementsByTagName('item')
        total_post = items.length
        print "Total posts " + str(total_post)
        for x in xrange(start_loop, total_post):
            print "start post number " + str(x)
            item = items[x]
            # only import published
            if item.getElementsByTagName('wp:status')[0].firstChild.nodeValue != 'publish':
                continue;

            # only import posts, not pages or other stuff
            if item.getElementsByTagName('wp:post_type')[0].firstChild.nodeValue != 'post':
                continue;

            if len(item.getElementsByTagName('title')[0].childNodes) == 0:
                continue;

            # post = tumblr_credentials
            # post['type'] = 'text';
            post_title = item.getElementsByTagName('title')[0].firstChild.nodeValue.strip().encode('utf-8',
                                                                                                   'xmlcharrefreplace')
            post_date = item.getElementsByTagName('pubDate')[0].firstChild.nodeValue
            post_content = item.getElementsByTagName('content:encoded')[0].firstChild

            if post_content.__class__.__name__ != 'CDATASection':
                continue

            post_body = item.getElementsByTagName('content:encoded')[0].firstChild.nodeValue.encode('utf-8',
                                                                                                    'xmlcharrefreplace')
            print "title: %s" % post_title

            # tumblrClient.create_text(blog_name="euriion", title=post_title, body=post_body, date=post_date, tags=[])
            wordpress_uploader.create_text(blog_name="berrybox-design", title=post_title, body=post_body, date=post_date, tags=[])

            # # deal with WordPress's stupid embedded Unicode characters
            # post = dict([(k,v.encode('utf-8') if type(v) is types.UnicodeType else v) for (k,v) in post.items()])

            # data = urllib.urlencode(post) # Use urllib to encode the parameters

            # try:
            # 	request = urllib2.Request(tumblr_api, data)
            # 	response = urllib2.urlopen(request) # This request is sent in HTTP POST

            # 	page = response.read(200000)
            # 	print page
            # except HTTPError, e:
            #     print 'The server couldn\'t fulfill the request.'
            #     print 'Error code: ', e.code
            #     print e.read()
            #     sys.exit(2)
            # except URLError, e:
            #     print 'We failed to reach a server.'
            #     print 'Reason: ', e.reason
            #     sys.exit(2)

            time.sleep(1) # don't overload the Tumblr API

    def display_blog_posts(self, blog_name):
        pprint.pprint(self.get_blog_posts(blog_name))


if __name__ == "__main__":
    usage = """
[Usage]: %prog [options] config-filename wordpress-xml-filename

ex) %prog -c COMMAND-NAME ./wordpress2tumblr.conf ./my_wordpress_content.xml

[COMMAND-NAME list]

display-client-info : connect to Tumblr and display client information
upload : upload the Wordpress XML file to Tumblr
    """
    parser = optparse.OptionParser(usage=usage, version="%prog 0.1")
    parser.add_option('-c', '--command', dest='command', help="command name to execute")
    (options, args) = parser.parse_args()

    if options.command is None:
        parser.print_help()
        sys.exit(2)

    config_filename = None
    wordpress_xml_filename = None

    if options.command == 'upload':
        if len(args) < 2:
            parser.print_help()
            sys.exit(2)
        else:
            config_filename = args[0]
            wordpress_xml_filename = args[1]
            if not os.path.exists(config_filename):
                print "config file does not exist!"
                print " - %s" % config_filename
            if not os.path.exists(wordpress_xml_filename):
                print "wordpress xml file does not exist!"
                print " - %s" % wordpress_xml_filename
    else:
        if len(args) < 1:
            parser.print_help()
            sys.exit(2)
        else:
            config_filename = args[0]
            if not os.path.exists(config_filename):
                print "config file does not exist!"
                print " - %s" % config_filename

    wordpress_uploader = WordpressToTumblr()
    wordpress_uploader.load_config(config_filename)
    wordpress_uploader.connect()
    if options.command == 'display-client-info':
        wordpress_uploader.display_client_info()
    elif options.command == 'display-blog-posts':
        print "blog name: %s" % args[1]
        wordpress_uploader.display_blog_posts(args[0])
    elif options.command == 'upload':
        wordpress_uploader.upload_wordpress_file(wordpress_xml_filename)
    del wordpress_uploader
