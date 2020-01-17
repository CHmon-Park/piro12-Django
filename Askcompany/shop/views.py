from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
#import request
from io import BytesIO
#from PIL import Image, ImageDraw, ImageFont
# Create your views here.

def archives_year(request, year):

    return HttpResponse('{}년도에 대한 내용'.format(year))

'''def response_pillow_image(request):
    ttf_path = 'C:/Windows/Fonts/malgun.ttf'

    image_url = 'http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg'
    res = request.get(image_url)
    io = BytesIO(res.content)
    io.seek(0)

    canvas = Image.open(io).convert('RGBA')
    font = ImageFont.truetype(ttf_path, 40)
    draw = ImageDraw.Draw(canvas)

    text = 'Ask Company'
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin
    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15, 15), text, font=font, fill=(20,20,20))

    response = HttpResponse(content_type = 'image/png')
    canvas.save(response, format='PNG')
    return response '''

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })