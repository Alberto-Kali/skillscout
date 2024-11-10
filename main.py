from flask import Flask, request, jsonify, render_template
from modules.mbti import MBTI
from modules.video import VideoProcessor


app = Flask(__name__, static_folder = "./static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    try:
        if 'video' not in request.files:
            return jsonify({"error": "Видео не загружено"}), 400

        video_file = request.files['video']
        processor = VideoProcessor()

        # Сохраняем видео
        video_path = processor.save_uploaded_video(video_file)
        
        try:
            # Извлекаем аудио
            audio_path = processor.extract_audio(video_path)
            
            # Разбиваем на кадры
            frames_folder = processor.split_video_to_frames(video_path)

            return jsonify({
                "video_path": video_path,
                "audio_path": audio_path,
                "frames_folder": frames_folder
            })
        
        except Exception as e:
            # Очистка в случае ошибки
            processor.cleanup(video_path)
            return jsonify({"error": str(e)}), 500

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Произошла неизвестная ошибка"}), 500


if __name__ == '__main__':
    app.run(debug=True)
