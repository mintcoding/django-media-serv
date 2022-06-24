from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
import mimetypes
import os

def getMediaFile(request):
    #file_path = request.path.replace("/media","")
    file_path = request.path.replace("../","")
    extension = request.path[-3:]
    #return HttpResponse("TEST", content_type=mimetypes.types_map['.'+str('html')])
    file_name_path = settings.BASE_DIR+file_path
    if os.path.isfile(file_name_path) is True:
              the_file = open(file_name_path, 'rb')
              the_data = the_file.read()
              the_file.close()
              if extension == 'msg':
                  return HttpResponse(the_data, content_type="application/vnd.ms-outlook")
              if extension == 'eml':
                  return HttpResponse(the_data, content_type="application/vnd.ms-outlook")


              return HttpResponse(the_data, content_type=mimetypes.types_map['.'+str(extension)])
    else:
              return
#
