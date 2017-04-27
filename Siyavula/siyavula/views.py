from pyramid.response import Response
from pyramid.view import view_config
from .scraper import Scraper


@view_config(route_name='hello', request_method='GET')
def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


@view_config(route_name='index', renderer='templates/index.jinja2', request_method=['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        search = str(search_text)
        #     DO THIS
        contents = Scraper.scrapwiki(search)
        return {'contents': contents}
    else:
        contents = ['No data to show', 'Enter search  on test field above']
        return {'contents': contents}
