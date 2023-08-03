function getPropinsi(negara_id) {
    let $ = django.jQuery;
    $.get('/pasien/cari-propinsi/' + negara_id, function (resp){
        let propinsi_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           propinsi_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_propinsi').html(propinsi_list);
    });
}

function getKota(propinsi_id) {
    let $ = django.jQuery;
    $.get('/pasien/cari-kota/' + propinsi_id, function (resp){
        let kota_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kota_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kota').html(kota_list);
    });
}

function getKecamatan(kota_id) {
    let $ = django.jQuery;
    $.get('/pasien/cari-kecamatan/' + kota_id, function (resp){
        let kecamatan_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kecamatan_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kecamatan').html(kecamatan_list);
    });
}

function getKelurahan(kecamatan_id) {
    let $ = django.jQuery;
    $.get('/pasien/cari-kelurahan/' + kecamatan_id, function (resp){
        let kelurahan_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kelurahan_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kelurahan').html(kelurahan_list);
    });
}