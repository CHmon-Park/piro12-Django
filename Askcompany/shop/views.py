import logging
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView
from .models import Item

logger = logging.getLogger(__name__)  # __name__ => "shop.views"


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 기록'.format(year))


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    logger.debug('query : {}'.format(q))

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

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

'''def item_new(request):
    print('GET :', request.GET)
    print('POST :', request.POST)
    print('FILES :', request.FILES)
    return render(request, 'shop/item_form.html')'''

def item_new(request, item = None):
    error_list = []
    values = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_publish = data.get('is_publish') in (True, 't', 'True', '1')

        #유효성 검사
        if len(name) < 2:
            error_list.append('name을 2글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            #저장 시도
            if item is None:
                item = Item()
            else:
                item = Item(name=name, desc=desc, price=price, is_publish=is_publish)
            if photo:
                item.photo.save(photo.name, photo, save=False)
            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)

        values = {
            'name' : name,
            'desc' : desc,
            'price' : price,
            'photo' : photo,
            'is_publish' : is_publish,
        }

    return render(request, 'shop/item_form.html', {
        'error_list' : error_list,
        'values' : values,
    })

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)