from django.shortcuts import render

from nhanvien.models import ThemMoiNV

# Create your views here.
def nhanvien(request):
    return render (request,'themnhanvien.html')
def xuly_nhanvien(request):
    tennv = request.GET.get('tennv')
    chucvunv = request.GET.get('chucvu')
    namsinhnv = request.GET.get('namsinh')
    print(tennv)
    dulieu = ThemMoiNV(
        ten = tennv,
        chucvu = chucvunv,
        namsinh = namsinhnv,
    )
    dulieu.save()
    return render (request,'themthanhcong.html')