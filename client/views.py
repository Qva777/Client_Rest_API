from django.shortcuts import render


def index(request):
    """Функция возвращает "главную" страницу"""
    return render(request, r'client/index.html')

#
# def about(request):
#     """Функция возвращает "про нас" страницу"""
#     return render(request, 'client/about.html')
#
#
def about(request):
    """Функция возвращает "контакты" страницу"""
    return render(request, 'client/about.html')


