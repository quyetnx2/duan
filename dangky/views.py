from django.shortcuts import render

from dangky.models import NguoiDung

# Create your views here.
def dangky(request):
    return render (request,'dangky.html')

def trangchu(request):
    return render (request,'trangchu.html')

def thongbao(request):
    return render (request,'dangky.html')

def test(request):
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    matkhau = request.GET.get('matkhau')
    
    print("ten",ten)
    print("mail",mail)
    print("matkhau",matkhau)

    if (len(ten)<10):
        return render(request,'thongbao.html')
    else:
        dulieu = NguoiDung(
            ten_dang_nhap = ten,
            email = mail,
            mat_khau = matkhau
        )
        dulieu.save()

        return render(request,'dangnhap.html')

     
# def xuly_dangnhap(request):
#     ten = request.GET.get('ten')
#     mk = request.GET.get('matkhau')
#     print(ten)
#     dulieu = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau=mk)
#     if dulieu.exists():
#         return render (request,'thanhcong.html')
#     else:
#         return render (request,'thatbai.html')   