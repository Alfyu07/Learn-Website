# array = [101,110,124,156,160,167,215,235,453,976]
# cari = 215
# awal = 0
# akhir = len(array)-1
# # berikut = awal + ((array[akhir]-cari)/(array[akhir]-array[awal]))*(akhir-awal)
# # print(berikut)
# def interpolasi (array,awal,akhir):
#   while(awal<=akhir):
#     berikut = int(awal + ((array[akhir]-cari)/(array[akhir]-array[awal]))*(akhir-awal))
#     if cari is array[berikut]:
#        return berikut
#     if (awal >= akhir and array[berikut] != cari) : 
#       return -1
#     if(array[berikut] < cari):
#       awal = berikut+1
#     elif (array[berikut>cari]):
#       akhir = berikut-1
    
#     print(berikut)

# print(interpolasi(array,awal,akhir))

cari = 51
a = [34,44,51,69,89,106,128,135,139]

awal = 0
akhir = len(a)-1
def biner(awal,akhir,array) :
  i = 1
  while(True):
    mid = int((awal + akhir)/2)
    if(array[mid] == cari) :
      print("ditemukan di",mid)
      return mid
    if(array[mid] != cari and awal >= akhir) :
      return -1
    if(cari<mid):
      akhir = mid-1
    else:
      awal = mid+1
    print(i)
    i+=1

biner(awal,akhir,a)
