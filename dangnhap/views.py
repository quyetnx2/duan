from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung

# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')


def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')
    dulieu = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau=mk)
    danh_sach = NguoiDung.objects.all()
    context ={
        'ds_nguoidung':danh_sach
    }
    if (dulieu.exists()):
        # return render(request,'themnhanvien.html',context)
        return render(request,'danhsach.html',context)
    else:
        return render(request,'thatbai.html')
    
def chi_tiet(request, nguoidung_id):
    nv = get_object_or_404 (NguoiDung, pk = nguoidung_id)
    context = {
        'nguoi_dung':nv
    }
    return render(request,'chitiet.html', context)

def xuly_capnhat(request):
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    matkhau = request.GET.get('matkhau')
    id_nguoidung = request.GET.get('id_nd')
    
    NguoiDung.objects.filter(id = id_nguoidung).update(
            ten_dang_nhap = ten,
            email = mail,
            mat_khau = matkhau
    )
    danh_sach = NguoiDung.objects.all()
    context ={
        'ds_nguoidung':danh_sach
    }
    return render(request,'danhsach.html',context)

def xoa_nguoidung(request, nguoidung_id):
    dulieu = get_object_or_404(NguoiDung, pk = nguoidung_id)
    
    try:
        dulieu.delete()
    except:
        print("Xóa bị lỗi")
    danh_sach = NguoiDung.objects.all()
    context ={
        'ds_nguoidung':danh_sach
    }
    return render(request,'danhsach.html',context)