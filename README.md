<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2a5e6593-056e-4b71-816a-a9f53cfaec18" />
# Analisis Sentimen Review Produk Menggunakan NLP dan Streamlit

## Deskripsi Proyek
Proyek ini merupakan studi kasus penerapan **Natural Language Processing (NLP) Pipeline**
untuk melakukan **analisis sentimen** terhadap ulasan produk berbahasa Indonesia.
Sistem yang dibangun mampu mengklasifikasikan teks ulasan ke dalam sentimen
**positif** atau **negatif** secara otomatis.

Proyek ini mencakup seluruh tahapan NLP mulai dari **data acquisition**, 
**preprocessing**, **feature extraction**, **modeling**, **evaluation**, 
hingga **deployment model menggunakan Streamlit** dalam bentuk aplikasi web interaktif.

---

## Dataset
Dataset yang digunakan adalah dataset **review produk berbahasa Indonesia**
yang telah memiliki label sentimen.

- Sumber dataset: Hugging Face  
- Link dataset:  
  https://huggingface.co/datasets/siRendy/dataset-analisis-sentimen-review-produk
- Jumlah data: ±10.000 ulasan
- Label sentimen:
  - `1` → Sentimen Positif
  - `0` → Sentimen Negatif

Dataset diakses langsung menggunakan Python tanpa perlu proses download manual.

---

## Tahapan NLP Pipeline

### 1. Data Acquisition
Data diperoleh dari platform Hugging Face menggunakan library `pandas`
dan di-load langsung melalui URL dataset.

### 2. Data Preprocessing
Tahapan preprocessing dilakukan untuk membersihkan teks ulasan, meliputi:
- Case folding (mengubah teks menjadi huruf kecil)
- Menghapus karakter non-alfabet
- Menghapus spasi berlebih

Tahap ini bertujuan untuk meningkatkan kualitas data sebelum proses ekstraksi fitur.

### 3. Feature Extraction
Metode **TF-IDF (Term Frequency–Inverse Document Frequency)** digunakan
untuk mengubah teks menjadi representasi numerik agar dapat diproses oleh model machine learning.

### 4. Modeling
Model klasifikasi yang digunakan adalah **Naive Bayes**, karena:
- Sederhana dan efisien
- Cocok untuk permasalahan klasifikasi teks
- Memberikan performa yang stabil untuk dataset berskala menengah

### 5. Evaluation
Evaluasi model dilakukan menggunakan beberapa metrik, antara lain:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Hasil evaluasi menunjukkan bahwa model mampu mengklasifikasikan sentimen
ulasan produk dengan performa yang baik.

### 6. Deployment
Model yang telah dilatih kemudian disimpan dalam format `.pkl` dan
dideploy menggunakan **Streamlit** sehingga dapat digunakan melalui
antarmuka web secara interaktif.

---

## Desain Antarmuka (User Interface)

Aplikasi web dikembangkan menggunakan Streamlit dengan desain antarmuka
yang sederhana dan mudah digunakan.

### Komponen UI:
- **Judul Aplikasi**  
  Menampilkan nama sistem *Analisis Sentimen Review Produk* sebagai identitas aplikasi.

- **Input Text Area**  
  Digunakan untuk memasukkan teks ulasan produk oleh pengguna.

- **Tombol Prediksi Sentimen**  
  Tombol interaktif untuk menjalankan proses klasifikasi sentimen berdasarkan input pengguna.

- **Output Hasil Prediksi**  
  Menampilkan hasil klasifikasi sentimen:
  - Positif (ditampilkan dengan warna hijau)
  - Negatif (ditampilkan dengan warna merah)

- **Footer Informasi**  
  Menampilkan identitas pengembang dan mata kuliah sebagai dokumentasi aplikasi.

---
