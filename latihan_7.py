Hari_pertama={"keju","tepung","garam","gula","coklat"}
Hari_kedua={"garam","gula","coklat","kecap"}

Hari_kedua.add("keju")
Hari_pertama.remove("garam")

Barang_beda=Hari_pertama.symmetric_difference(Hari_kedua)

print(Barang_beda)