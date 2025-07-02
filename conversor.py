import os
from pillow_heif import register_heif_opener
from PIL import Image

def convert_heic_to_jpg(input_folder, output_folder=None):
    register_heif_opener()
    
    if output_folder is None:
        output_folder = os.path.join(input_folder, "JPG")
    
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"Convertendo imagens de: {input_folder}")
    print(f"Salvando em: {output_folder}\n")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.heic'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.heic', '.jpg'))
            
            try:
                Image.open(input_path).save(output_path, "JPEG", quality=90)
                print(f"✅ {filename} → {os.path.basename(output_path)}")
            except Exception as e:
                print(f"❌ Erro em {filename}: {str(e)}")

if __name__ == "__main__":
    # Caminho corrigido
    base_dir = os.path.expanduser("~/Desktop/Meus_Trabalhos/Fotos nao convertidas")
    input_dir = os.path.join(base_dir, "Parafuso BLACK-20250627T002207Z-1-001"  )
    
    if os.path.exists(input_dir):
        convert_heic_to_jpg(input_dir)
        print("\n✅ Conversão concluída! Verifique a pasta JPG/")
    else:
        print(f"\n❌ Pasta não encontrada: {input_dir}")
        print("Verifique se:")
        print("1. O nome da pasta está exatamente como mostrado no terminal")
        print("2. As fotos HEIC estão dentro desta pasta")