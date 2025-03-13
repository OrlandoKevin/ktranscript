# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
  # Use a breakpoint in the code line below to debug your script.
  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def convertir(seconds):
  h = int(seconds // 3600)
  m = int((seconds % 3600) // 60)
  s = int(seconds % 60)
  return f"{h:02d}:{m:02d}:{s:02d}"

def transcribe_files(project_path, model="turbo", **kwargs):
  import os
  import whisper
  import tqdm

  input_dir = os.path.join("data", project_path, 'inputs')
  output_dir = os.path.join("data", project_path, 'outputs')
  
  # Ensure output directory exists
  os.makedirs(output_dir, exist_ok=True)

  print(f"Transcribing files in {input_dir} and saving to {output_dir}")
  
  # Load model
  model = whisper.load_model(model)

  for input_file in os.listdir(input_dir):
    if input_file.endswith(".m4a"):
      input_file_path = os.path.join(input_dir, input_file)
      print(f"Transcribing {input_file_path}")
      output_file = os.path.join(output_dir, os.path.splitext(input_file)[0] + ".txt")
      transcribed = model.transcribe(input_file_path, **kwargs)
      # Enregistrement de la transcription
      with open(output_file , 'w', encoding='utf-8') as f:
        for segment in transcribed["segments"]:
          start_time = convertir(segment['start'])
          end_time = convertir(segment['end'])
          f.write(f"{start_time} - {end_time}: {segment['text']}\n")

  print("Done!")

# Example usage
# transcribe_files('/path/to/your/project')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  transcribe_files("test", verbose=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
