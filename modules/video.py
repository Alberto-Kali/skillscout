import os
import cv2
import uuid
import shutil
from flask import Flask, request, jsonify
import moviepy.editor as mp
from werkzeug.utils import secure_filename


class VideoProcessor:
    def __init__(self, upload_folder='uploads'):
        self.upload_folder = upload_folder
        os.makedirs(upload_folder, exist_ok=True)

    def validate_file(self, file):
        """
        Валидация файла:
        - Проверка наличия файла
        - Проверка расширения
        - Проверка размера файла
        """
        if not file:
            raise ValueError("Файл не загружен")
        
        filename = secure_filename(file.filename)
        
        # Список допустимых расширений
        ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
        
        # Проверка расширения
        if not self._allowed_file(filename, ALLOWED_EXTENSIONS):
            raise ValueError(f"Недопустимый формат файла. Используйте: {', '.join(ALLOWED_EXTENSIONS)}")
        
        # Проверка размера (максимум 50 МБ)
        file.seek(0, os.SEEK_END)
        file_length = file.tell()
        file.seek(0)
        
        if file_length > 50 * 1024 * 1024:  # 50 МБ
            raise ValueError("Размер файла не должен превышать 50 МБ")
        
        return filename

    def _allowed_file(self, filename, allowed_extensions):
        """Проверка расширения файла"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in allowed_extensions

    def generate_unique_filename(self, original_filename):
        """Генерация уникального имени файла"""
        unique_id = str(uuid.uuid4())
        ext = original_filename.rsplit('.', 1)[1].lower()
        return f"{unique_id}.{ext}"

    def save_uploaded_video(self, video_file):
        """Сохранение видео с уникальным именем"""
        try:
            filename = self.validate_file(video_file)
            unique_filename = self.generate_unique_filename(filename)
            filepath = os.path.join(self.upload_folder, unique_filename)
            video_file.save(filepath)
            return filepath
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")
            raise

    def extract_audio(self, video_path):
        """Извлечение аудио с обработкой ошибок"""
        try:
            video = mp.VideoFileClip(video_path)
            audio_path = video_path.replace('.mp4', '.wav')
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            print(f"Ошибка при извлечении аудио: {e}")
            raise

    def split_video_to_frames(self, video_path, fps=1):
        """Нарезка кадров с обработкой ошибок"""
        try:
            frames_folder = os.path.join(self.upload_folder, f'frames_{uuid.uuid4()}')
            os.makedirs(frames_folder, exist_ok=True)

            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                raise ValueError("Не удалось открыть видеофайл")

            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                if frame_count % int(cap.get(cv2.CAP_PROP_FPS)) == 0:
                    frame_path = os.path.join(frames_folder, f'frame_{frame_count}.jpg')
                    cv2.imwrite(frame_path, frame)

                frame_count += 1

            cap.release()
            return frames_folder
        except Exception as e:
            print(f"Ошибка при нарезке кадров: {e}")
            raise

    def cleanup(self, video_path, audio_path=None, frames_folder=None):
        """
        Очистка временных файлов
        - Удаление видео
        - Удаление аудио
        - Удаление папки с кадрами
        """
        try:
            # Удаление видео
            if video_path and os.path.exists(video_path):
                os.remove(video_path)
            
            # Удаление аудио
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)
            
            # Удаление папки с кадрами
            if frames_folder and os.path.exists(frames_folder):
                shutil.rmtree(frames_folder)
        except Exception as e:
            print(f"Ошибка при очистке файлов: {e}")
