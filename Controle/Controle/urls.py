from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Controle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^acesso/', include('acesso.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','acesso.views.home',name='pagina_inicial'),
    url(r'^/cadastrocarro/$','acesso.views.cadcarro',name='cadcarro'),
    url(r'^/cadastrocliente/$','acesso.views.cadcliente',name='cadcliente'),
    url(r'^/cadastrovaga/$','acesso.views.cadvaga',name='cadvaga')
)
