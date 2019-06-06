from lumavate_service_util import lumavate_route, SecurityType, RequestType
from flask import render_template, g


@lumavate_route('/', ['GET'], RequestType.page, [SecurityType.jwt])
def root():
  return render_template('home.html', logo='/{}/{}/discover/icons/microservice.png'.format(g.integration_cloud, g.widget_type))

@lumavate_route('/helloworld', ['GET'], RequestType.api, [SecurityType.none])
def helloworld():
  return "hello!"
