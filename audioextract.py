from moviepy.editor import VideoFileClip
import os

# Meminta input untuk nama folder tujuan
output_folder = input("Masukkan nama folder tujuan: ")

# Pastikan folder tujuan ada atau buat jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Buat list nama file video di folder saat ini
video_files = os.listdir()

# Filter list hanya menampilkan file video
video_files = [file for file in video_files if file.endswith('.mp4')]

# Loop melalui setiap file video
for video_file in video_files:
    # Ekstrak nama file tanpa ekstensi
    video_name = os.path.splitext(video_file)[0]
    
    # Nama file audio keluaran (MP3)
    output_audio_file = os.path.join(output_folder, f"{video_name}.mp3") # Simpan dalam folder tujuan
    
    # Baca video
    video_clip = VideoFileClip(video_file)
    
    # Ekstrak audio dari video
    audio_clip = video_clip.audio
    
    # Simpan audio ke file MP3
    audio_clip.write_audiofile(output_audio_file)
    
    # Tutup clip
    audio_clip.close()
    video_clip.close()

print("Konversi selesai. File-file MP3 disimpan dalam folder:", output_folder)
