
import json
import testdata

class DataObject(object):
    def __init__():
        self.primary_keys = []

    def as_json(self):
        as_json = {}
        for property in dir(self):
            as_json[property] = getattr(self, property, None)
        return as_json
    
    def __str__(self):
        as_str = ""
        for property in dir(self):
            try:
                as_str += "\n" + property + ": " + getattr(self, property)
            except AttributeError:
                as_str += "\n" + property + ": None"
        return as_str



class RelatedArticle(DataObject):
    def __init__(self, from_doi, to_doi):
        """
        Related article basics are a from_doi and to_doi,
        other properties can be added dynamically
        """
        self.primary_keys = ['from_doi', 'to_doi']
        self.from_doi = from_doi
        self.to_doi = to_doi
        
    def __dir__(self):
        return ['from_doi', 'to_doi', 'ext_link_type', 'related_article_type', 'xlink_href']
    
    
class Article(DataObject):
    def __init__(self, doi):
        """
        Article meta data
        """
        self.primary_keys = ['doi']
        self.doi = doi

    def __dir__(self):
        return ['doi']
        

def related(doi):
    """
    Get related article items by doi
    """
    related_articles = testdata.load_related_article_data()
    return filter(lambda item: item.from_doi == doi, related_articles) 
 
        
def article(doi):
    """
    Get article meta and details by doi
    """
    
    articles = testdata.load_article_data()
    return filter(lambda item: item.doi == doi, articles) 
        
        
        
if __name__ == '__main__':

    records = related("a")
    print "\n"
    print "Found " + str(len(records)) + " matching related article records"
    for item in records:
        print json.dumps(item.as_json(), indent=4)
        print item

    records = article("a")
    print "\n"
    print "Found " + str(len(records)) + " matching article records"
    for item in records:
        print json.dumps(item.as_json(), indent=4)
        print item