from django.contrib.syndication.views import Feed
from blog.models import Article
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.feedgenerator import Atom1Feed
from markdown2 import markdown


class ExtendedRSSFeed(Rss201rev2Feed):
    mime_type = 'application/xml'


class RssSiteNewsFeed(Feed):
    feed_type = ExtendedRSSFeed
    author_name = "致怀"
    title = "致怀's Blog | 大好时光！"
    link = "http://blog.tor1024.com/"
    description = "大好时光"
    feed_url = 'http://blog.tor1024.com'

    def items(self):
        return Article.objects.filter(status=0).order_by('-created_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.description)

    def item_link(self, item):
        return '/article/%s' % item.url

    def item_pubdate(self, item):
        return item.created_time

    def item_guid(self, item):
        return


class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description
