from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    return render(
        request=request,
        template_name='homepage/index.html',
        context={
            'ice_cream_list': IceCream.objects.values(
                'id', 'title', 'price', 'description',
            ).filter(
                is_on_main=True,
                is_published=True,
                category__is_published=True,
            )
        },
    )
