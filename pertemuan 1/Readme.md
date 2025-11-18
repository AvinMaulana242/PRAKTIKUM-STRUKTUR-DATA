Penjelasan Kode STACK (LIFO)

Kode ini membuat sebuah kelas bernama Stack. Fungsinya untuk meniru cara kerja tumpukan, yaitu data yang terakhir dimasukkan akan menjadi data pertama yang keluar.

Penjelasan per baris (versi manusia)

class Stack:
Bagian ini membuat sebuah blueprint atau “cetakan” untuk membuat objek stack.

def __init__(self):
Ini adalah konstruktor. Setiap kali kita membuat objek Stack, program otomatis membuat list kosong sebagai tempat menyimpan elemen.

self.items = []
Di sinilah semua data stack akan disimpan, bentuknya list.

isEmpty()
Method ini cuma memeriksa apakah list kosong atau tidak. Kalau panjang list 0, berarti stack tidak punya isi.

push(self, item)
Fungsi push dipakai untuk memasukkan data baru ke bagian paling atas stack. Caranya tinggal memakai append(). Setelah itu ditampilkan teks “Push” supaya tahu item apa yang baru masuk.

pop(self)
Method pop berfungsi mengambil data paling atas dan menghapusnya dari stack. Kalau stack lagi kosong, method ini memberikan pesan “Stack kosong!”. Kalau tidak, dia ambil item paling akhir pakai pop().

peek(self)
Fungsi ini hanya melihat isi teratas tanpa menghapusnya. Kalau stack kosong, yang dikembalikan tetap pesan “Stack kosong!”.

display(self)
Digunakan untuk menampilkan seluruh isi stack dalam bentuk list sehingga mudah dilihat.

Penjelasan bagian program utama

stack = Stack()
Membuat sebuah objek stack baru.

stack.push(10), push(20), push(30)
Secara berurutan memasukkan angka 10, 20, dan 30.

stack.pop()
Mengambil elemen paling atas (30), karena prinsipnya LIFO.

stack.peek()
Melihat elemen teratas yang tersisa, yaitu 20.





Penjelasan Kode QUEUE (FIFO)

Kelas Queue digunakan untuk mensimulasikan antrian. Cara kerjanya kebalikan stack: data pertama yang masuk akan keluar lebih dulu.

Penjelasan baris demi baris

class Queue:
Ini adalah deklarasi kelas queue.

__init__
Sama seperti stack, konstruktor ini membuat list kosong sebagai tempat penyimpanan data antrian.

isEmpty()
Mengecek apakah antrian masih kosong atau tidak.

enqueue(self, item)
Method ini menambah data ke bagian belakang antrian. Caranya tetap memakai append(). Setiap data masuk, program mencetak “Enqueue” untuk menunjukkan data apa yang baru ditambahkan.

dequeue(self)
Berfungsi menghapus dan mengambil data paling depan antrian. Pada list, elemen pertama berada pada indeks 0, jadi dipakai pop(0).

front(self)
Untuk melihat siapa yang berada di paling depan antrian tanpa menghapusnya.

display(self)
Menampilkan keseluruhan isi antrian supaya kita tahu urutannya.

Penjelasan program utama

queue = Queue()
Membuat objek antrian.

enqueue("A"), enqueue("B"), enqueue("C")
Memasukkan tiga data secara berurutan: A, B, C.

dequeue()
Mengeluarkan data paling depan, yaitu “A”, karena prinsipnya FIFO.

front()
Mengecek siapa yang sekarang berada di posisi terdepan, yaitu “B”.
