from PIL import Image
from tkinter import filedialog
import os
import piexif

def compress_and_save_with_exif(input_path, output_path, quality=80):
    try:
        with Image.open(input_path) as img:
            exif_dict = piexif.load(img.info.get('exif', b''))
            img.save(output_path, quality=quality, exif=piexif.dump(exif_dict))
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

def compress_images_in_folder(folder_path, output_folder, quality=80):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print ("画像圧縮を開始します。")
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            print("処理中の項目 : " + os.path.basename(filename))
            compress_and_save_with_exif(input_path, output_path, quality)

def main():
    # ダイアログでフォルダを選択
    folder_selected = filedialog.askdirectory(title="Select Folder with Images")
    print("画像フォルダ : " + folder_selected)
    
    if folder_selected:
        # 出力先フォルダを指定
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        print("出力フォルダ : " + output_folder)
        if output_folder:
            # 画像を指定の圧縮率で保存（Exifデータを保持）
            compress_images_in_folder(folder_selected, output_folder)
            print("圧縮が完了しました")

if __name__ == "__main__":
    main()
