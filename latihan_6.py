Hari_pertama={"keju","tepung","garam","gula","coklat"}
Hari_kedua={"garam","gula","coklat","kecap"}

Hari_kedua.add("keju")
Hari_pertama.remove("garam")

Barang_kedua=Hari_kedua.difference(Hari_pertama)

print(Barang_kedua)