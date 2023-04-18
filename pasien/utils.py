import random
from django.db.models import Max

def create_new_ref_number():
      last_pasien = pasien.objects.aggregate(Max('no_rkm_medis'));
      print(last_pasien)
      return str(random.randint(1000000000, 9999999999))