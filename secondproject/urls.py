from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

# import functioncrud.urls
# import functioncrud.views
# # import classcrud.urls
# # import classcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),    #crud연습때문에 주석

    path('blog/', include('blog.urls')),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    
    # path('funccrud/', include(functioncrud.urls)),
    # # path('classcrud/', include(classcrud.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
