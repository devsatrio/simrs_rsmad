
function getBerkasKaryawan(karyawan_id) {
    let $ = django.jQuery;
    $.get('/karyawan/cari-berkas/' + karyawan_id, function (resp){
        let berkas_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
            berkas_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#berkas_karyawan').html(berkas_list);
    });
}

function getBerkasKaryawanDua(karyawan_id) {
    $.get('/karyawan/cari-berkas/' + karyawan_id, function (resp){
        let berkas_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
            berkas_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#berkas_karyawan').html(berkas_list);
    });
}